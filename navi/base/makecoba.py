from xml.dom import minidom
import os

class Project:
    
    def __init__(self, name, path):
        if name[:-4] != '.nav':
            name += '.nav'
        self.name = name
        self.path = path
        
    def save_file(self, mode):
        f = open(os.path.join("%s" % self.path, "%s" % self.name), mode)
        f.write('project saved successfully!')
        f.close()

class Makecoba:

    def __init__(self):
        pass
        
    def new_project(self, project_path):
        if project_path[:-4] != '.nav':
            project_path += '.nav'
        #self.project = Project(string)
        #print 'Project ' +  string + ' Created!'
