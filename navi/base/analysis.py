from math import sqrt
import time
import os
#import glob
import tempfile
import subprocess
#import time
import shutil

class Analysis:
    
    def __init__(self):
        pass
        
        
class ThresholdAnalysis(Analysis):
    
    def __init__(self):
        Analysis.__init__(self)
    
    #TODO: decorator for abstract method
    def do_analysis(self, sim_matrix):
        pass
        
        
class LargestCluster(ThresholdAnalysis):

    def __init__(self):
        ThresholdAnalysis.__init__(self)
        

class Distance(ThresholdAnalysis):

    def __init__(self):
        ThresholdAnalysis.__init__(self)
        
    def do_analysis(self, sim_matrix, neighbourhood_matrices=None):
        data = []
        if neighbourhood_matrices != None:
            for i in range(0, len(neighbourhood_matrices[:-1])):
                distance = 0.0
                for row in range(0, len(neighbourhood_matrices[i].data)):
                    for column in range(0, len(neighbourhood_matrices[i].data[row])):
                        distance += pow(neighbourhood_matrices[i].data[row][column] - \
                            neighbourhood_matrices[i + 1].data[row][column], 2)
                data.append(sqrt(distance))
                
            return data
            
        return None
                        
 
class Clustering(Analysis):
    def __init__(self):
        Analysis.__init__(self)
    
    #TODO: decorator for abstract method
    def clusterize(self, nbh_matrix):
        pass
 
class NewmanGirvan(Clustering):
    def __init__(self):
        Clustering.__init__(self)
        self.dendrogram = []
        
    def clusterize(self, nbh_matrix):
        self.threshold = nbh_matrix.threshold
        similarity_array = nbh_matrix.data
        matrix_str = '   '
        for i in range(0, len(similarity_array)):
            for j in range(0, len(similarity_array[i])):
                matrix_str += str(similarity_array[i][j])
                if j + 1 < len(similarity_array[i]):
                    matrix_str += '   '
            matrix_str += '\n'
        
        dendo_directory = tempfile.mkdtemp(prefix='navi-dendo-', dir=tempfile.gettempdir())
        dendo_file = os.path.join(os.path.dirname(__file__), '../vendors/dendo/dendo')
        shutil.copy(dendo_file, dendo_directory)
        
        f = open(os.path.join(dendo_directory, 'edendo.dat'), 'w')
        f.write('%s 0\nmatrixdendo.txt\nmatrixdendo.txt_out\n-1 3' % len(similarity_array))
        f.flush()
        
        olddir = os.getcwd()
        os.chdir(dendo_directory)
        matrix_file = open(os.path.join(dendo_directory, 'matrixdendo.txt'), 'w')
        matrix_file.write(matrix_str)
        matrix_file.flush()
        
        subprocess.check_call([os.path.join(dendo_directory, 'dendo')])
        #matrix_rearranged = treat open(os.path.join(dendo_directory, 'd2matrixde3.dat'), 'r')
        #dendrogram = treat open(os.path.join(dendo_directory, 'd2matrixde4.dat'), 'r')
        #new_vertex_order = treat open(os.path.join(dendo_directory, 'd2matrixde5.dat'), 'r')
        
        dendrogram_file = open('d2matrixde4.dat', 'r')
        for i in dendrogram_file.readlines():
            data = [float(elem.strip('\n')) for elem in i.split()]
            data = data[1:]
            self.dendrogram.append(data)
        
        os.chdir(olddir)
        
        matrix_file.close()
        f.close()
        shutil.rmtree(dendo_directory)
        
        return True
