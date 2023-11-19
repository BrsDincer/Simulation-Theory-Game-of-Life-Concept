from util_main import CLASSINIT,ERROR,DOCUMENTATION,NULL,PROCESS,ENVIRONMENT,ERRORMODULE
import numpy as np

class DiscoveryAnomalies(object):
    """
    DiscoveryAnomalies handles the detection of anomalies within a specified radius in the simulation environment.
    
    The class is designed to work with a grid-like environment where certain cells are marked as anomalies.
    It scans the environment to identify which cells are in close proximity to anomalies.

    Attributes:
        defaultRadius (int): The radius within which the class checks for anomalies around each cell.

    Methods:
        __str__(): Returns a string representation of the class.
        __call__(): Defines the callable behavior of the class instance.
        __getstate__(): Method for customizing pickling behavior.
        __repr__(): Returns the class documentation.
        Run(environment, anomalies): Scans the environment and marks cells that have detected anomalies within the default radius.

    The Run method iterates over each cell in the environment and checks its surrounding cells within the defaultRadius to determine if any anomalies are present. 
    Cells that detect anomalies within this radius are marked accordingly.
    """
    def __init__(self)->CLASSINIT:
        self.defaultRadius = 1
    def __str__(self)->str:
        return "Discovery Anomalies - Pre(Script)"
    def __call__(self)->NULL|None:
        return None
    def __getstate__(self)->ERROR:
        ERRORMODULE().Default
    def __repr__(self)->DOCUMENTATION|str:
        return DiscoveryAnomalies.__doc__
    def Run(self,environment:ENVIRONMENT,anomalies:ENVIRONMENT)->PROCESS:
        discoveries = np.zeros_like(environment)
        for r,c in np.ndindex(environment.shape):
            for dx in range(-self.defaultRadius,self.defaultRadius+1):
                for dy in range(-self.defaultRadius,self.defaultRadius+1):
                    nx,ny = r+dx,c+dy
                    if (0 <= nx < environment.shape[0]) and (0 <= ny < environment.shape[1]):
                        if anomalies[nx,ny]:
                            discoveries[nx,ny] = 1
                        else:
                            pass
                    else:
                        pass
        return discoveries
                   
        