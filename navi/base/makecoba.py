
class Project:
    
    def __init__(self, project_name, project_path):
        self.name = project_name
        self.path = project_path

class Makecoba:

    def __init__(self):
        pass
        
    def new_project(self, string):
        self.project = Project()
        print 'Project ' +  string + ' Created!'
