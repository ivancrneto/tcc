from xml.dom import minidom
from persistence import Persistence

class Project:
    
    def __init__(self, name, path):
        if name[:-4] != '.nav':
            name += '.nav'
        self.name = name
        self.path = path
        self.persistence = Persistence()
        self.state = ProjectState()
        
    def save_file(self, mode):
        return self.persistence.save_project_file(self, mode)
        
        
class ProjectState:

    def __init__(self):
        pass
        

class SimilaryMatrixGenerated(ProjectState):
    def __init__(self):
        pass
