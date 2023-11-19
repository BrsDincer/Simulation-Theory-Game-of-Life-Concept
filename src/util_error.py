from util_classes import CLASSINIT,ERROR,DOCUMENTATION

class ERRORMODULE(object):
    """
    ERRORMODULE is a custom error handling class for the simulation.

    It encapsulates error handling logic, providing a structured approach to raising and managing exceptions within the simulation. 
    The class is designed to facilitate the handling of various error scenarios that might arise during the execution of the simulation.

    Attributes:
        error (Exception): The default exception to be raised by the module.

    Methods:
        __str__(): Returns a string representation of the class.
        __call__(): Returns the default error when the class instance is called.
        __getstate__(): Custom method for pickling, which raises the default error.
        __repr__(): Returns the class documentation.
        Default: A property that raises the default error when accessed.
        Manual(errorType, errorMessage): Allows for raising manual errors with a specified error type and message.

    The 'Manual' method provides flexibility in raising customized exceptions, enhancing the error handling capabilities of the simulation.
    """
    def __init__(self)->CLASSINIT:
        self.error = NotImplementedError(NotImplemented)
    def __str__(self)->str:
        return "Error Module - Sub(Script)"
    def __call__(self)->ERROR:
        return self.error
    def __getstate__(self)->ERROR:
        raise self.error
    def __repr__(self)->DOCUMENTATION|str:
        return ERRORMODULE.__doc__
    @property
    def Default(self)->ERROR:
        raise self.error
    def Manuel(self,errorType:ERROR,errorMessage:str)->ERROR:
        raise errorType(errorMessage)