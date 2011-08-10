from xml.dom import minidom
from persistence import Persistence

class Project:
    
    def __init__(self, name, path):
        if name[:-4] != '.nav':
            name += '.nav'
        self.name = name
        self.path = path
        self.persistence = Persistence()
        
    def save_file(self, mode):
        return self.persistence.save_project_file(self, mode)

class Makecoba:

    def __init__(self):
        pass
        
    def new_project(self, project_path):
        if project_path[:-4] != '.nav':
            project_path += '.nav'
        #self.project = Project(string)
        #print 'Project ' +  string + ' Created!'
