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
                    
        Matrix.__init__(self, data, sequence_position_map)
