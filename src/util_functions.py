from util_classes import PROCESS,ERROR
from util_error import ERRORMODULE
import os,shutil

CreateDirectory:PROCESS = lambda x: os.mkdir(x) if not os.path.exists(x) else None
DeleteDirectory:PROCESS = lambda x: shutil.rmtree(x) if len(os.listdir(x)) > 1 else None
TerminationMessage:PROCESS = lambda x: x.get("content","") and x.get("content","").rstrip().endswith("TERMINATE")
ReturnFontConfiguration = lambda x,y,z: x.render(y,True,z)

def DefineCredentials(initialKey:str)->PROCESS|ERROR:
    if (initialKey) and (initialKey != " "):
        os.environ["OPENAI_API_KEY"] = initialKey
    else:
        ERRORMODULE().Manuel(ValueError,"[ERROR] The API Key entered is invalid or inappropriate [ERROR]")