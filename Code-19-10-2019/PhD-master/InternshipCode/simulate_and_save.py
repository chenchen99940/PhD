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
        return 'output/myResult_{}_{}_{}.npy'.format(self.a,self.b,self.shape)

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
    number_computed = 0
    sum_of_results = 0
    sum_of_squares = 0
    try:
        print('file',fileName,'exists')
        sum_of_results,sum_of_squares,number_computed = np.load(fileName)
    except Exception as e:
        print(e)
    if number_computed < number_of_replicas_to_compute:
        print('We should do more computations')
        for n in range(int(number_computed),number_of_replicas_to_compute):
            result = simulate(parameters)
            sum_of_results += result
            sum_of_squares += result**2
        np.save(fileName,np.array([sum_of_results,sum_of_squares,number_of_replicas_to_compute]))
        number_computed = number_of_replicas_to_compute
    print('all computation done for',parameters.fileName())
    average = sum_of_results / number_computed
    confidence = np.sqrt((sum_of_squares / number_computed-average**2)/number_computed) # This uses var[X] = E[X^2]-E[X]^2
    return average,confidence

print('In order for this script to work, you need a directeory "output/" to exists')
print(computeAndSaveStupidValues(Parameters(10,2.5,28), 1000000))
