from math import sqrt

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
                        
                        
