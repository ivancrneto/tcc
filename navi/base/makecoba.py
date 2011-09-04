from xml.dom import minidom
from persistence import Persistence

class Project:
    
    def __init__(self, name, path):
        if name[:-4] != '.nav':
            name += '.nav'
        self.name = name
        self.path = path
        self.persistence = Persistence()
        self.save_file('w')
        
    def save_file(self, mode):
        return self.persistence.save_project_file(self, mode)
        
    def end(self):
        self.persistence.update_data(self)
