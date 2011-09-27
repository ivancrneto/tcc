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
        
    def do_analysis(self, sim_matrix):
        pass
