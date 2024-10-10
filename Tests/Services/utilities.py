import os

def getEnvironmentVariable(sVariableName):
    if not os.environ.get(sVariableName) is None:
        return os.environ.get(sVariableName)
    else:
        return None