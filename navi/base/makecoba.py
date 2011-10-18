from xml.dom import minidom
from persistence import Persistence
from matrices import SimilarityMatrix, AdjacencyMatrix, NeighbourhoodMatrix
from analysis import Distance, NewmanGirvan, Clustering
from Bio import SeqIO
import os
import glob
import tempfile
import subprocess
import time
import shutil


class Project:
    '''
    name
    description
    path
    database_path
    database_date
    Persistence 1
    BioHandler 1
    SimilarityMatrix 1
    AdjacencyMatrix *
    NeighbourhoodMatrix *
    '''
    
    def __init__(self, name, path, database_path):
        #TODO: it is better if we override __new__ method in Project class instead of receive None args
        if name != None and database_path != None: #new project called
            if name[:-4] != '.nav':
                name += '.nav'
            self.name = name
            self.path = path
            self.database_path = database_path
            self.adjacency_matrices = []
            self.neighbourhood_matrices = []
            self.analysis = []
            self.state = 'new'
            self.persistence = Persistence()
            self.save_file('w')
            self.bio_handler = BioHandler(database_path)
            self.save_project()
        else: #open project called
            self.path = path
            self.persistence = Persistence()
        
    def save_file(self, mode):
        return self.persistence.save_project_file(self, mode)
        
    def save_project(self):
        self.persistence.update_data(self)
        
    def load_data(self):
        return self.persistence.load_project_data(self)
    
    def end(self):
        self.persistence.update_data(self)
        
    def get_sequences(self):
        return self.bio_handler.get_sequences()
        
    def get_adjacency_matrices(self):
        adj_matrices = {}
        for matrix in self.adjacency_matrices:
            adj_matrices[matrix.threshold] = matrix
            
        return adj_matrices
        
    def get_neighbourhood_matrices(self):
        nbh_matrices = {}
        for matrix in self.neighbourhood_matrices:
            nbh_matrices[matrix.threshold] = matrix
            
        return nbh_matrices
        
    def generate_adjacency_matrices(self, adj_matrix_gen):
        if adj_matrix_gen:
            for threshold in range(adj_matrix_gen['begin'], adj_matrix_gen['end'] + 1):
                adj_matrix = AdjacencyMatrix(self.similarity_matrix, threshold)
                adj = self.get_adjacency_matrix(adj_matrix.threshold)
                if adj:
                    self.adjacency_matrices.remove(adj)
                self.adjacency_matrices.append(adj_matrix)
                
    def generate_neighbourhood_matrices(self, nbh_matrix_gen):
        if nbh_matrix_gen:
            for threshold in range(nbh_matrix_gen['begin'], nbh_matrix_gen['end'] + 1):
                nbh_matrix = NeighbourhoodMatrix(self.similarity_matrix, threshold)
                if nbh_matrix_gen['rearrange']:
                    #TODO
                    #pass matrix and call minener
                    #receive new matrix and list with new order
                    #call method to rearrange nbh_matrix
                    pass
                nbh = self.get_neighbourhood_matrix(nbh_matrix.threshold)
                if nbh:
                    self.neighbourhood_matrices.remove(nbh)
                self.neighbourhood_matrices.append(nbh_matrix)
                
    def get_adjacency_matrix(self, threshold):
        for matrix in self.adjacency_matrices:
            if matrix.threshold == threshold:
                return matrix
        return None
        
    def get_neighbourhood_matrix(self, threshold):
        for matrix in self.neighbourhood_matrices:
            if matrix.threshold == threshold:
                return matrix
        return None
        
    def analyse_thresholds(self, analysis_type):
        if analysis_type == 'distance':
            th_analysis = Distance()
            distance_data = None
            if len(self.neighbourhood_matrices) == 101:
                distance_data = th_analysis.do_analysis(self.similarity_matrix, self.neighbourhood_matrices)
                self.analysis.append(th_analysis)
            else:
                print len(self.neighbourhood_matrices)
            
            self.state = 'threshold'
            return distance_data
            
    def get_clustering_analysis(self, threshold):
        for analysis in self.analysis:
            if isinstance(analysis, Clustering) and analysis.threshold == threshold:
                return analysis
                
        return None
            
    def clusterize(self, threshold, method):
        if method == 'newmangirvan':
            clus_analysis = NewmanGirvan()
            nbh_matrix = self.get_neighbourhood_matrix(threshold)
            clus_analysis.clusterize(nbh_matrix)
            old_clus_analysis = self.get_clustering_analysis(threshold)
            if old_clus_analysis:
                self.analysis.remove(old_clus_analysis)
            self.analysis.append(clus_analysis)
        
    def generate_similarities(self, sequences):
        self.similarity_matrix = self.bio_handler.generate_similarities(sequences)
        self.state = 'similarity_matrix'
        return True
        
class BioHandler:
    '''
    database_path
    database_date
    Blast 1
    Organism *
    Matrix 1..*
    '''

    def __init__(self, database_path):
        self.database_path = database_path
        self.organisms = []
        self.matrices = []
        self.filter_files()
        
    def add_organism(self, organism):
        self.organisms.append(organism)
        
    def get_sequences(self):
        sequences_map = {}
        for organism in self.organisms:
            sequences_map[organism] = organism.get_sequences()
            
        return sequences_map
        
    def filter_files(self):
        #TODO: this should be done by persistence
        for file_name in glob.glob(os.path.join('%s' % self.database_path, '*')):
            for seq_record in SeqIO.parse(file_name, "genbank"):
            
                #TODO: implement the situation when we have more than one sequence for a organism
                organism = Organism(seq_record.annotations['organism'], seq_record.annotations['taxonomy'])
                
                sequence = Sequence(
                    seq_record.annotations['accessions'],
                    seq_record.annotations['gi'],
                    0,
                    seq_record.name,
                    seq_record.description,
                    seq_record.id, #version
                    file_name,
                    '%s' % seq_record.seq.alphabet,
                    seq_record.seq,
                    seq_record.annotations,
                    organism
                )
                
                organism.add_sequence(sequence)
                self.add_organism(organism)
                
    def generate_similarities(self, sequences):
        blast_directory = tempfile.mkdtemp(prefix='navi-blast-', dir=tempfile.gettempdir())
        database_file = tempfile.NamedTemporaryFile(mode='w', prefix='navi-', dir=blast_directory)
        
        similarity_array = []
        for t in range(0, len(sequences)):
            columns = []
            for v in range(0, len(sequences)):
                 columns.append(0)
            similarity_array.append(columns)

        sequence_position_map = {}
        
        count = 0
        for sequence in sequences:
            database_file.write('>' + sequence.locus + '\n' + '%s' % sequence.code + '\n')
            sequence_position_map[sequence.locus] = count
            count += 1
        
        database_file.flush()
        
        subprocess.check_call(['formatdb', '-i', database_file.name])
        
        for sequence in sequences:
            seq_file = tempfile.NamedTemporaryFile(mode='w', prefix='navi-', dir=blast_directory)
            
            seq_file.write('>' + sequence.locus + '\n' + '%s' % sequence.code + '\n')
            seq_file.flush()
            #subprocess.check_call(['blastall', '-d', database_file.name, '-i',
            #    seq_file.name, '-p', 'blastp', '-o',  seq_file.name + '-blast-res'])
            command = ' '.join(['blastall', '-d', database_file.name, '-i',
                seq_file.name, '-p', 'blastp'])
            process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, close_fds=True)
            blast_res = process.stdout.read().split('\n')
            
            for i in range(0, len(blast_res)):
                if '>' in blast_res[i]:
                    #print blast_res[i].split('>')[1].strip(),
                    sequence_locus = blast_res[i].split('>')[1].strip()
                    percent = int(blast_res[i + 4].split()[3].strip('(').strip('%,)'))
                    
                    if sequence_locus != sequence.locus:
                        if similarity_array[sequence_position_map[sequence.locus]][sequence_position_map[sequence_locus]] < percent:
                            similarity_array[sequence_position_map[sequence.locus]][sequence_position_map[sequence_locus]] = percent
                            similarity_array[sequence_position_map[sequence_locus]][sequence_position_map[sequence.locus]] = percent
                    else:
                        similarity_array[sequence_position_map[sequence.locus]][sequence_position_map[sequence_locus]] = 0
                        similarity_array[sequence_position_map[sequence_locus]][sequence_position_map[sequence.locus]] = 0
        #remove seq_file blast result file
        shutil.rmtree(blast_directory)
        for i in range(0, len(similarity_array)):
            for j in range(0, len(similarity_array[i])):
                print similarity_array[i][j],
            print '\n'
            
        sim_matrix = SimilarityMatrix(similarity_array, sequence_position_map)
        self.matrices.append(sim_matrix)
        return sim_matrix
        
class Organism:
    '''
    name
    taxonomy
    Sequence 1..*
    '''
    
    def __init__(self, name, taxonomy):
        self.sequences = []
        self.name = name
        self.taxonomy = taxonomy
        
    def __repr__(self):
        return ' '.join(self.taxonomy)
    
    def add_sequence(self, sequence):
        self.sequences.append(sequence)
        
    def get_sequences(self):
        return self.sequences
    
class Sequence:
    '''
    accessions
    gi
    community
    locus
    description
    version
    file
    alphabet
    code
    Organism 1
    '''
    
    def __init__(self, accessions, gi, community, locus, description, version, 
            file_name, alphabet, code, annotations, organism):
        self.accessions = accessions
        self.gi = gi
        self.community = community
        self.locus = locus
        self.description = description
        self.version = version
        self.file = file_name
        self.alphabet = alphabet
        self.code = code
        self.annotations = annotations
        self.organism = organism
    
    
    
    
    
    
    
