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
