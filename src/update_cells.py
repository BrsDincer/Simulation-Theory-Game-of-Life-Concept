from util_main import CLASSINIT,NULL,ERROR,DOCUMENTATION,ENVIRONMENT,PROCESS,CELL,ERRORMODULE
from discovery_anomaly import DiscoveryAnomalies
import pygame,numpy as np

class UpdateCellExistence(object):
    """
    UpdateCellExistence is responsible for updating the state of each cell in the simulation grid. 
    It handles the logic for cell survival, death, and the discovery of anomalies.

    Attributes:
        dieColor (tuple): Color for dead cells.
        aliveColor (tuple): Color for alive cells.
        anomalyColor (tuple): Color for cells marked as anomalies.
        discoveryColor (tuple): Color for cells that have discovered anomalies.
        backgroundColor (tuple): Background color of the grid.
        deceasedCount (int): Counter for the number of deceased cells.
        alive (int): Number of alive cells after the latest update.
        deceased (int): Number of deceased cells after the latest update.

    Methods:
        __str__(): Returns a string representation of the class.
        __call__(): Defines the callable behavior of the class instance.
        __getstate__(): Method for customizing pickling behavior.
        __repr__(): Returns the class documentation.
        Run(surface, anomalyGrid, discoveryGrid, env, sze): Handles the logic for updating the state of each cell in the grid.

    The Run method is the core of this class, where it processes each cell in the environment, 
    applies the rules of cell survival and death, checks for anomalies, and updates the grid accordingly.
    """
    def __init__(self)->CLASSINIT:
        self.dieColor = (178,178,184)
        self.aliveColor = (29,245,5)
        self.anomalyColor = (255,100,10)
        self.discoveryColor = (0,10,255)
        self.backgroundColor = (0,0,0)
        self.deceasedCount = 0
        self.alive = None
        self.deceased = None
    def __str__(self)->str:
        return "Update For Cell Existence - Pre(Script)"
    def __call__(self)->NULL|None:
        return None
    def __getstate__(self)->ERROR:
        ERRORMODULE().Default
    def __repr__(self)->DOCUMENTATION|str:
        return UpdateCellExistence.__doc__
    def Run(self,
            surface:list|int|float|CELL,
            anomalyGrid:list|int|float|CELL,
            discoveryGrid:list|int|float|CELL,
            env:list|int|float|ENVIRONMENT,
            sze:list|int|float)->PROCESS:
        nextGeneration = np.zeros(
                (
                    env.shape[0],
                    env.shape[1]
                    )
            )
        for r,c in np.ndindex(env.shape):
            nAlive = np.sum(
                    env[r-1:r+2,c-1:c+2]
                ) - env[r,c]
            if (env[r,c] == 1) and (nAlive < 2 or nAlive > 3):
                nextGeneration[r,c] = 0
                color = self.dieColor
                self.deceasedCount += 1
                self.deceased = self.deceasedCount
            elif (env[r,c] == 1 and 2 <= nAlive <= 3) or (env[r,c] == 0 and nAlive == 3):
                nextGeneration[r,c] = 1
                self.alive = (nextGeneration == 1).sum()
                color = self.aliveColor
                if np.random.random() > 0.99:
                    # which happens about 1% of the time - anomaly
                    # this condition effectively means that for each cell in each iteration, there is a 1% chance that an "anomaly" will occur
                    anomalyGrid[r,c] = 1
                    discoveryGrid = DiscoveryAnomalies().Run(environment=env,anomalies=anomalyGrid)
                    if discoveryGrid[r,c] == 1:
                        color = self.discoveryColor
                    else:
                        color = self.anomalyColor
                else:
                    pass
            else:
                pass
            if env[r,c] == 1:
                color = color
            else:
                color = self.backgroundColor
            pygame.draw.rect(
                    surface,
                    color,
                    (c*sze,r*sze,sze-1,sze+1)
                )
        return nextGeneration,self.alive,self.deceased,anomalyGrid,discoveryGrid
            
            
                
                
                
    