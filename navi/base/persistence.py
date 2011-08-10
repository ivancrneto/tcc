import os

class Persistence:

    def __init__(self):
        pass
        
    def save_project_file(self, project, mode):
        f = open(os.path.join("%s" % project.path, "%s" % project.name), mode)
        f.write('project saved successfully!')
        f.close()
        return True
