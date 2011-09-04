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
        
    def save_file(self, mode):
        return self.persistence.save_project_file(self, mode)
        
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
        self.filter_files()
        
    def filter_files(self):
        #TODO: this should be done by persistence
        for file_name in glob.glob(os.path.join('%s' % self.database_path, '*')):
            for seq_record in SeqIO.parse(file_name, "genbank"):
                print file_name
                print seq_record.id #locus
                print seq_record.description #definition
                print seq_record.name
                #print seq_record.locus
                #print seq_record.gi
                #print seq_record.keywords
                print seq_record.seq.alphabet #alphabet
                #print seq_record.organism
                print dir(seq_record)
                print seq_record.seq #sequence
                print dir(seq_record.seq)
                
                #keywords
                #gi
                #organism
                
                #print repr(seq_record.seq)
                #print len(seq_record)
                #print '-------------------------------------------'
                #print seq_record
                #print '==========================================='
                #$locus, $definition, $gi, $keywords, $organism, $sequence, $arquivo, $alphabet
                #['__add__', '__class__', '__contains__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__getitem__', '__hash__', '__init__', '__iter__', '__len__', '__module__', '__new__', '__nonzero__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_per_letter_annotations', '_seq', '_set_per_letter_annotations', '_set_seq', 'annotations', 'dbxrefs', 'description', 'features', 'format', 'id', 'letter_annotations', 'lower', 'name', 'seq', 'upper']
                #my $arquivo = $fileName;
				
				#my $locus = $seq->display_id;
				#my $definition = $seq->desc;
				#my $gi = $seq->primary_id;
				#my $keywords = $seq->keywords;
				#my $alphabet = $seq->alphabet;
				#my $sequence = $seq->seq;

        
class Organism:
    '''
    description
    name
    Sequence 1..*
    '''
    
    def __init__(self):
        pass
    
    
class Sequence:
    '''
    ec
    gi
    complement
    community
    name
    description
    locus
    file
    alphabet
    code
    Organism 1
    '''
    
    def __init__(self):
        pass
    
    
    
    
    
    
    
    
    
