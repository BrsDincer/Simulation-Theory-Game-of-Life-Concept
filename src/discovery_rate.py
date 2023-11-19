from util_main import CLASSINIT,NULL,DOCUMENTATION,ENVIRONMENT,ERROR,ERRORMODULE
import numpy as np

class DiscoveryRate(object):
    """
    DiscoveryRate is responsible for calculating the discovery rate of anomalies within the simulation environment.

    This class takes the environment and the discoveries made within it to compute the rate at which anomalies are being discovered relative to the total number of cells.

    Attributes:
        totalCells (int): The total number of cells in the environment.
        totalDiscovery (int): The total number of discoveries made.
        discoveryRate (float): The calculated rate of discovery.

    Methods:
        __str__(): Returns a string representation of the class.
        __call__(): Defines the callable behavior of the class instance.
        __getstate__(): Method for customizing pickling behavior.
        __repr__(): Returns the class documentation.
        Calculate(environment, discovery): Calculates the discovery rate based on the total cells and discoveries.

    The Calculate method computes the discovery rate by dividing the number of discoveries by the total number of cells in the environment. 
    It ensures a meaningful calculation by handling cases where the number of cells is zero to avoid division by zero errors.
    """
    def __init__(self)->CLASSINIT:
        self.totalCells = None
        self.totalDiscovery = None
        self.discoveryRate = None
    def __str__(self)->str:
        return "Calculation of Discovery Rate - Pre(Script)"
    def __call__(self)->NULL|None:
        return None
    def __getstate__(self)->ERROR:
        ERRORMODULE().Default
    def __repr__(self)->DOCUMENTATION|str:
        return DiscoveryRate.__doc__
    def Calculate(self,environment:ENVIRONMENT,discovery:ENVIRONMENT)->int or float:
        self.totalCells = np.sum(environment)
        self.totalDiscovery = np.sum(discovery)
        self.discoveryRate = (round(self.totalDiscovery / self.totalCells,4)) if self.totalCells > 0 else 0
        return self.totalDiscovery,self.discoveryRate