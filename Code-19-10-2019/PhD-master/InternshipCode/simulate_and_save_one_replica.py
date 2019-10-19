"""
This document describes a simple way to pre-compute and save results
"""
import numpy as np

class Parameters:
    """
    This class contains all the parameters needed to run a simulation of the model
    """
    def __init__(self, a, b, shape):
        self.a = a
        self.b = b 
        self.shape = shape
    def fileName(self):
        """
        This function returns the name of the file to which data is stored
        (to be replaced by something useful)
        """
        return 'output/myResult_oneReplica_{}_{}_{}.npy'.format(self.a,self.b,self.shape)

def simulate(parameters):
    """
    This function simulates the system once
    (this should be replace by something useful)
    """
    return (np.random.pareto(parameters.shape) + parameters.a) * parameters.b

def computeAndSaveStupidValues(parameters, number_of_replicas_to_compute):
    """
    This function tries to load the result. 
    If 'fileName' does not exists, it will comppute the value and then save it. 
    """
    fileName = parameters.fileName()
    try:
        print('file',fileName,'exists')
        return np.load(fileName)
    except Exception as e:
        print(e)
    result = simulate(parameters)
    np.save(fileName,result)
    return result

print('In order for this script to work, you need a directeory "output/" to exists')
print(computeAndSaveStupidValues(Parameters(10,2.5,28), 1000000))
