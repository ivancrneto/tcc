import os
#import glob
import tempfile
import subprocess
#import time
import shutil

class Matrix:
    '''
    data
    path
    sequence_position_map
    '''
    
    def __init__(self, data, sequence_position_map):
        self.data = data
        self.path = None
        self.sequence_position_map = sequence_position_map
        
        
class SimilarityMatrix(Matrix):
    def __init__(self, data, sequence_position_map):
        Matrix.__init__(self, data, sequence_position_map)


class AdjacencyMatrix(Matrix):
    def __init__(self, similarity_matrix, threshold):
        sequence_position_map = similarity_matrix.sequence_position_map
        self.threshold = threshold
        self.graphic = False
        self.graphic_name = None
        
        data = []
        for t in range(0, len(similarity_matrix.data)):
            columns = []
            for v in range(0, len(similarity_matrix.data)):
                 columns.append(0)
            data.append(columns)
        
        for i in range(0, len(similarity_matrix.data)):
            for j in range(0, len(similarity_matrix.data)):
                if similarity_matrix.data[i][j] >= threshold:
                    data[i][j] = 1
                else:
                    data[i][j] = 0
                    
        Matrix.__init__(self, data, sequence_position_map)


class NeighbourhoodMatrix(Matrix):
    def __init__(self, similarity_matrix, threshold):
        sequence_position_map = similarity_matrix.sequence_position_map
        self.threshold = threshold
        self.graphic = False
        self.graphic_name = None
        self.rearranged = False
        
        data = []
        for t in range(0, len(similarity_matrix.data)):
            columns = []
            for v in range(0, len(similarity_matrix.data)):
                 columns.append(0)
            data.append(columns)
        
        for i in range(0, len(similarity_matrix.data)):
            for j in range(0, len(similarity_matrix.data)):
                if similarity_matrix.data[i][j] >= threshold:
                    data[i][j] = 1
                else:
                    data[i][j] = 0
                    
        data = self.generate_neighbourhood_values(data)
                    
        Matrix.__init__(self, data, sequence_position_map)
        
        
    def generate_neighbourhood_values(self, adj_matrix):
        madchar_directory = tempfile.mkdtemp(prefix='navi-madchar-', dir=tempfile.gettempdir())
        
        madchar_file = os.path.join(os.path.dirname(__file__), '../vendors/madchar/madchar')
        shutil.copy(madchar_file, madchar_directory)
        
        f = open(os.path.join(madchar_directory, 'emadch.dat'), 'w')
        f.write('5 %s 1 300 0 1\nmatrix.txt\nmadcharresult\n0\n-1 0 0 0 0 0\t' % len(adj_matrix))
        f.flush()
        
        olddir = os.getcwd()
        os.chdir(madchar_directory)
        matrix_file = open(os.path.join(madchar_directory, 'matrix.txt'), 'w')
        matrix_str = ''
        for i in adj_matrix:
            for j in i:
                matrix_str += '%s' % j
            matrix_str += '\n'
        matrix_file.write(matrix_str)
        matrix_file.flush()
        subprocess.check_call([os.path.join(madchar_directory,'madchar')])
        raw_nbh_matrix = open(os.path.join(madchar_directory, 'madcharresult_11.dat'), 'r')
        os.chdir(olddir)
        
        data = raw_nbh_matrix.readlines()
        data = data[2:]
        for i in range(0, len(data)):
            data[i] = [int(j) for j in data[i].split()]
        
        raw_nbh_matrix.close()
        matrix_file.close()
        f.close()
        shutil.rmtree(madchar_directory)
        
        return data
        
        
        
        
        
        
        
        
        
