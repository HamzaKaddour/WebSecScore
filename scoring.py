from Tests import hibp as HIBP
from Tests import malware_detect as MW
from Tests import open_ports as OP
from Tests import threatfox as COMPROMIZE
from Tests import virusTotal as VT
from Tests import vul_wapiti as VUL
from Tests import whatcms as CMS
# from WebSecScore.Tests import 
import requests

# TODO #
'''
ADD THE REGEX OF THE DOMAIN SO THAT IT TAKES DIFFERENT COMBINIZATIONS OF THE DOMAIN FORMAT
'''



def testingResults(domain):
    result = {
        "HIBP" : None, 
        "MALWARE" : None, 
        "OPEN_PORTS" : None, 
        "THREATFOX" : None, 
        "VIRUSTOTAL" : None, 
        "WAPITI" : None, 
        "CMS" : None, 
    }
    
    try:
        result["HIBP"] = HIBP.checkHIBP(domain) 
        result["MALWARE"] = MW.checkMalwareURL(domain)
        result["OPEN_PORTS"] = OP.scan_open_ports(domain)
        result["THREATFOX"] = COMPROMIZE.checkCompromisedURL(domain)
        result["VIRUSTOTAL"] = VT.findVirusTotalResult(domain)
        result["WAPITI"] = VUL.vulnerabilityFinder(domain)
        result["CMS"] = CMS.startCMSChecks(domain)
        
        
    except Exception as e:
        print(e)
        
    finally:
        return result


def scoreResults(testingRes):
    
    weights = {
        "HIBP" : 0.15, 
        "MALWARE" : 0.15, 
        "OPEN_PORTS" : 0.1, 
        "THREATFOX" : 0.15, 
        "VIRUSTOTAL" : 0.2, 
        "WAPITI" : 0.2, 
        "CMS" : 0.05, 
    }
    result = {
        "HIBP" : None, 
        "MALWARE" : None, 
        "OPEN_PORTS" : None, 
        "THREATFOX" : None, 
        "VIRUSTOTAL" : None, 
        "WAPITI" : None, 
        "CMS" : None, 
    }
    
    try:
        score = 0
        if testingRes["HIBP"]:
            score += weights["HIBP"]
        print()
        
    except Exception as e:
        print(e)
        
    finally:
        return score
    
testres = testingResults("google.com")
print(scoreResults(testres))
