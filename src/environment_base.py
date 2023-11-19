from util_main import CLASSINIT,NULL,DOCUMENTATION,ENVIRONMENT
import numpy as np,random

class ReturnEnvironment(object):
    """
    ReturnEnvironment is responsible for creating the initial environment or grid for the simulation.

    It initializes the environment with a specific size and populates it based on a degree of randomness. 
    This environment serves as the baseline upon which the simulation operates.

    Attributes:
        randomness (int): The seed for random number generation, which influences the initial state of the environment.
        size (int): Represents the scale or maximum limit for generating random positions in the environment.

    Methods:
        __str__(): Returns a string representation of the class.
        __call__(): Defines the callable behavior of the class instance.
        __repr__(): Returns the class documentation.
        Create(xdim, ydim, roundCount): Generates the initial environment grid based on the specified dimensions and randomness.

    The Create method initializes a grid of given dimensions and randomly activates a certain number of cells based on the 'roundCount'. 
    This process involves setting random cells to an 'alive' state, thereby creating the initial configuration for the simulation.
    """
    def __init__(self)->CLASSINIT:
        self.randomness = 10
        self.size = 9*39
    def __str__(self)->str:
        return "Creating Environment - Pre(Script)"
    def __call__(self)->NULL|None:
        return None
    def __repr__(self)->DOCUMENTATION|str:
        return ReturnEnvironment.__doc__
    def Create(self,xdim:int,ydim:int,roundCount:int)->ENVIRONMENT:
        baseArea = np.zeros((ydim,xdim))
        np.random.seed(self.randomness)
        for _ in range(roundCount):
            randomInteger = random.randint(1,self.size)
            baseArea.ravel()[randomInteger] = 1
        return baseArea