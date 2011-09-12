from xml.dom import minidom
from persistence import Persistence
from Bio import SeqIO
import os
import glob
import tempfile
import subprocess


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
        if name[:-4] != '.nav':
            name += '.nav'
        self.name = name
        self.path = path
        self.database_path = database_path
        self.persistence = Persistence()
        self.save_file('w')
        self.bio_handler = BioHandler(database_path)
        self.save_project()
        
    def save_file(self, mode):
        return self.persistence.save_project_file(self, mode)
        
    def save_project(self):
        self.persistence.update_data(self)
    
    def end(self):
        self.persistence.update_data(self)
        
    def get_sequences(self):
        return self.bio_handler.get_sequences()
        
    def generate_similarities(self, sequences):
        return self.bio_handler.generate_similarities(sequences)
        
        
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
        import time
        blast_directory = tempfile.mkdtemp(prefix='navi-blast-', dir=tempfile.gettempdir())
        database_file = tempfile.NamedTemporaryFile(mode='w', prefix='navi-', dir=blast_directory)
        for sequence in sequences:
            database_file.write('>' + sequence.locus + '\n' + '%s' % sequence.code + '\n')
        
        database_file.flush()
        
        subprocess.check_call(['formatdb', '-i', database_file.name])
        
        for sequence in sequences:
            seq_file = tempfile.NamedTemporaryFile(mode='w', prefix='navi-', dir=blast_directory)
            seq_file.write('>' + sequence.locus + '\n' + '%s' % sequence.code + '\n')
            seq_file.flush()
            subprocess.check_call(['blastall', '-d', database_file.name, '-i',
                seq_file.name, '-p', 'blastp', '-o',  seq_file.name + '-blast-res'])
            #f = open(seq_file.name + '-blast-res', 'r')
            #remove seq_file blast result file
        #remove blast directory
        #>>> from subprocess import Popen, PIPE, STDOUT
        #>>> cmd = 'ls -la'
        #>>> p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        #>>> output = p.stdout.read()
        #>>> print output

        
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
    
    
    
    
    
    
    
