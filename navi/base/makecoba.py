from xml.dom import minidom
from persistence import Persistence
from Bio import SeqIO
import os
import glob


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
                    seq_record.id, #locus
                    file_name,
                    '%s' % seq_record.seq.alphabet,
                    seq_record.seq,
                    seq_record.annotations,
                    organism
                )
                
                organism.add_sequence(sequence)
                self.add_organism(organism)
        
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
    
    def add_sequence(self, sequence):
        self.sequences.append(sequence)
    
class Sequence:
    '''
    accessions
    gi
    community
    name
    description
    locus
    file
    alphabet
    code
    Organism 1
    '''
    
    def __init__(self, accessions, gi, community, name, description, locus, 
            file_name, alphabet, code, annotations, organism):
        self.accessions = accessions
        self.gi = gi
        self.community = community
        self.name = name
        self.description = description
        self.locus = locus
        self.file = file_name
        self.alphabet = alphabet
        self.code = code
        self.annotations = annotations
        self.organism = organism
    
    
    
    
    
    
    
