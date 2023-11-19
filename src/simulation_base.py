from util_main import CLASSINIT,NULL,DOCUMENTATION,ENVIRONMENT,ERROR,ERRORMODULE,PROCESS,ReturnFontConfiguration
from environment_base import ReturnEnvironment
from update_cells import UpdateCellExistence
from discovery_rate import DiscoveryRate
import pygame,numpy as np

class SimulationBase(object):
    """
    Environment Size (ex: 7200):
        This represents the scale or complexity of the simulation environment.
        In the context of simulation theory, a larger environment could imply a more complex and detailed simulation, akin to our vast universe.
    
    Time Pass (ex: 13 seconds):
        This is the duration for which the simulation ran.
        In relation to humanity, this could be analogous to the span of human existence or the period during which we have been capable of contemplating and investigating our reality.
    
    Total Discovery (ex: 202):
        This number indicates how many anomalies were discovered during the simulation. In terms of simulation theory, discoveries might be equated to scientific or philosophical insights that challenge or expand our understanding of reality.
    
    Discovery Rate (ex: 1%):
        A low discovery rate suggests that uncovering anomalies or evidence of the simulation is rare and challenging.
        Applied to humanity, this might imply that despite our advancements, the chances of definitively proving we are in a simulation are slim, as the 'anomalies' or 'clues' are sparse and difficult to detect.
    
    Alive Single (ex: 122):
        This could represent the active individuals on the earth or universe.
    
    Alive Colony (ex: 20):
        This could represent the active or aware portion of a population.
        In our case, it might refer to the number of individuals or groups actively engaged in exploring or questioning the nature of reality.
    
    Deceased (ex: 120):
        This number may symbolize the ideas, theories, or individuals that have not survived the test of time or scrutiny in the quest to understand our existence.
        It could represent failed hypotheses or obsolete scientific theories.
    """
    def __init__(self)->CLASSINIT:
        self.gridColor = (53,54,53)
        self.txtColor = (255,255,255)
        self.xdim = 120
        self.ydim = 60
        self.size = 7
        self.randomness = 100
    def __str__(self)->str:
        return "Simulation - Main(Script)"
    def __call__(self)->NULL|None:
        return None
    def __getstate__(self)->ERROR:
        ERRORMODULE().Default
    def __repr__(self)->DOCUMENTATION|str:
        return SimulationBase.__doc__
    def LoadEnvironment(self)->ENVIRONMENT:
        try:
            env = ReturnEnvironment().Create(
                    xdim=self.xdim,
                    ydim=self.ydim,
                    roundCount=self.randomness
                )
            return env
        except:
            ERRORMODULE().Manuel(OSError,"[ERROR] Loading Environment Failed, Check Process [ERROR]")
    def Initialize(self)->PROCESS:
        try:
            pygame.init()
            surface = pygame.display.set_mode(
                    (
                        self.xdim*self.size,
                        self.ydim*self.size
                        )
                )
            #discoveryEngine = DiscoveryRate()
            font = pygame.font.Font(None,15)
            timeClock = pygame.time.Clock()
            ticks = pygame.time.get_ticks()
            pygame.display.set_caption("SIMULATION THEORY - BASED ON GAME OF LIFE")
            environment = self.LoadEnvironment()
            anomalyGrid = np.zeros((self.xdim*self.size,self.ydim*self.size),dtype=int)
            discoveryGrid = np.zeros((self.xdim*self.size,self.ydim*self.size),dtype=int)
            while True:
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT):
                        pygame.quit()
                        return
                surface.fill(self.gridColor)
                environment,alive,deceased,anomalyGrid,discoveryGrid = UpdateCellExistence().Run(surface=surface,
                                                                                                 anomalyGrid=anomalyGrid,
                                                                                                 discoveryGrid=discoveryGrid,
                                                                                                 env=environment,
                                                                                                 sze=self.size)
                if int(alive) > 0:
                    totalDiscovery,discoveryRate = DiscoveryRate().Calculate(environment=environment,discovery=discoveryGrid)
                else:
                    pass
                endTime = pygame.time.get_ticks() - ticks
                sizeInfo = f"ENVIRONMENT - SIZE: {str(self.xdim*self.ydim)}"
                timeInfo = f"TIME - SECOND: {str(endTime/1000)}"
                randomnessInfo = f"RANDOMNESS: {str(self.randomness)}"
                colonyAliveInfo = f"COLONY:ALIVE - COUNT: {str(int(alive/4))}"
                singleAliveInfo = f"SINGLE:ALIVE - COUNT: {str(alive)}"
                deceasedInfo = f"DECEASED - COUNT: {str(deceased)}"
                totalDiscoveryInfo = f"TOTAL DISCOVERY:CELL CROSS - COUNT: {str(totalDiscovery)}"
                discoveryRateInfo = f"DISCOVERY RATE: {str(discoveryRate)} %"
                sizeOut = ReturnFontConfiguration(font,sizeInfo,self.txtColor)
                timeOut = ReturnFontConfiguration(font,timeInfo,self.txtColor)
                randomnessOut = ReturnFontConfiguration(font,randomnessInfo,self.txtColor)
                colonyAliveOut = ReturnFontConfiguration(font,colonyAliveInfo,self.txtColor)
                singleAliveOut = ReturnFontConfiguration(font,singleAliveInfo,self.txtColor)
                deceasedOut = ReturnFontConfiguration(font,deceasedInfo,self.txtColor)
                totalDiscoveryOut = ReturnFontConfiguration(font,totalDiscoveryInfo,self.txtColor)
                discoveryRateOut = ReturnFontConfiguration(font,discoveryRateInfo,self.txtColor)
                surface.blit(sizeOut,(12,self.xdim+215))
                surface.blit(timeOut,(12,self.xdim+230))
                surface.blit(totalDiscoveryOut,(12,self.xdim+245))
                surface.blit(discoveryRateOut,(12,self.xdim+260))
                surface.blit(randomnessOut,(self.ydim+558,self.xdim+215))
                surface.blit(colonyAliveOut,(self.ydim+558,self.xdim+230))
                surface.blit(singleAliveOut,(self.ydim+558,self.xdim+245))
                surface.blit(deceasedOut,(self.ydim+558,self.xdim+260))
                timeClock.tick(60)
                pygame.display.update()
        except:
            ERRORMODULE().Manuel(OSError,"[ERROR] An Error Occurred While Loading the System, Try Again [ERROR]")
                
if __name__ == "__main__":
    SimulationBase().Initialize()         
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            