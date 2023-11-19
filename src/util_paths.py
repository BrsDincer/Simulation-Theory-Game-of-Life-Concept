from util_classes import PATH
import os

BASEPATH:PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENTPATH:PATH = os.path.join(BASEPATH,"contents")
OUTPUTSPATH:PATH = os.path.join(BASEPATH,"outputs")
CONFIGURATIONPATH:PATH = os.path.join(BASEPATH,"configuration")
PROJECTFILEPATH:PATH = os.path.join(CONFIGURATIONPATH,"project.yaml")
