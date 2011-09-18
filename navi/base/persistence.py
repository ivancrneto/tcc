import os, sys, zipfile, time, tempfile, shutil, pickle

class Persistence:

    def __init__(self):
        self.project_file = None
        self.tmp_project_dir = None
        self.project_tree_decompressed = False
        
    def save_project_file(self, project, mode):
        self.project_file = os.path.join("%s" % project.path, "%s" % project.name)
        if self.tmp_project_dir == None:
            self.tmp_project_dir = os.path.join(tempfile.gettempdir(), 'navi-%s' % int(time.time()))
        os.mkdir(self.tmp_project_dir)
        f = open(os.path.join(self.tmp_project_dir, 'project.nv'), 'w')
        pickle.dump(project, f)
        f.close()
        self.compress_dir_structure()
        return True
        
    def load_project_data(self, project):
        self.project_file = '%s' % project.path
        if self.tmp_project_dir == None:
            self.tmp_project_dir = os.path.join(tempfile.gettempdir(), 'navi-%s' % int(time.time()))
        self.decompress_dir_structure()
        f = open(os.path.join(self.tmp_project_dir, 'project.nv'), 'r')
        up = pickle.Unpickler(f)
        new_project = up.load()
        self.compress_dir_structure()
        return new_project
        
    def compress_dir_structure(self):
        zip = zipfile.ZipFile(self.project_file, 'w')
        olddir = os.getcwd()
        os.chdir(self.tmp_project_dir)
        for root, dirs, files in os.walk('.'):
            for file_name in files:
                zip.write(os.path.join(root,file_name))
        zip.close()
        os.chdir(olddir)
        shutil.rmtree(self.tmp_project_dir)
        self.project_tree_decompressed = False
    
    def decompress_dir_structure(self):
        if not self.project_tree_decompressed:
            zip = zipfile.ZipFile(self.project_file, 'r')
            olddir = os.getcwd()
            try:
                os.chdir(self.tmp_project_dir)
            except OSError:
                folder_name = 'navi-%s' % int(time.time())
                self.tmp_project_dir = os.path.join(tempfile.gettempdir(), folder_name)
                os.chdir(tempfile.gettempdir())
                os.mkdir(folder_name)
                os.chdir(self.tmp_project_dir)
            
            zip.extractall()
            os.chdir(olddir)
            self.project_tree_decompressed = True
    
    def update_data(self, project):
        self.decompress_dir_structure()
        #This is because it is saving this variable as True and shouldn't
        if self.project_tree_decompressed == True:
            self.project_tree_decompressed = False
        f = open(os.path.join(self.tmp_project_dir, 'project.nv'), 'w')
        pickle.dump(project, f)
        f.close()
        self.compress_dir_structure()

