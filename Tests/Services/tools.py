import os
import socket

def getEnvironmentVariable(sVariableName):
    if not os.environ.get(sVariableName) is None:
        return os.environ.get(sVariableName)
    else:
        return None
    

def hostname_to_ip(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return "Invalid hostname or unable to resolve."