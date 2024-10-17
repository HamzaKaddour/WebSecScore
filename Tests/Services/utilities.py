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
    
    
def ip_to_hostname(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
        return hostname
    except socket.herror:
        return "Invalid IP address or unable to resolve."
    
# print(ip_to_hostname("139.180.203.104"))