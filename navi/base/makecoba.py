from xml.dom import minidom

class Project:
    
    def __init__(self, name, path):
        self.name = name
        self.path = path

class Makecoba:

    def __init__(self):
        pass
        
    def new_project(self, project_path):
        if project_path[:-4] != '.nav':
            project_path += '.nav'
        #self.project = Project(string)
        #print 'Project ' +  string + ' Created!'
