from xml.dom import minidom
from persistence import Persistence

class Project:
    '''
    name
    description
    path
    database_path
    database_date
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
    '''

    def __init__(self, database_path):
        self.database_path = database_path
        self.filter_files()
        
    def filter_files(self):
        pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
