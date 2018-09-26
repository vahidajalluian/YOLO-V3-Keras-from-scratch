import numpy as np
class Yolo_weight:
    def load_weights(self, weightfile):    
        fp      = open(weightfile, "rb")
        header  = np.fromfile(fp, dtype = np.int32, count = 5)
        weights = np.fromfile(fp, dtype = np.float32)
        
