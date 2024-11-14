from Tests import hibp as HIBP
from Tests import malware_detect as MW
from Tests import open_ports as OP
from Tests import threatfox as COMPROMIZE
from Tests import virusTotal as VT
from Tests import vul_wapiti as VUL
from Tests import whatcms as CMS
from Tests import csa as CSA
from Tests import visa_pci as VISA
# from WebSecScore.Tests import 
import requests

# TODO #
'''
ADD THE REGEX OF THE DOMAIN SO THAT IT TAKES DIFFERENT COMBINIZATIONS OF THE DOMAIN FORMAT
'''



def testingDomainResults(domain, name = None):
    result = {
        "HIBP" : None, 
        "MALWARE" : None, 
        "OPEN_PORTS" : None, 
        "THREATFOX" : None, 
        "VIRUSTOTAL" : None, 
        "WAPITI" : None, 
        "CMS" : None, 
    #     "CSA" : None,
    #     "VISA": None
    }
    
    try:
        result["HIBP"] = HIBP.checkHIBP(domain) 
        result["MALWARE"] = MW.checkMalwareURL(domain)
        result["OPEN_PORTS"] = OP.scan_open_ports(domain)
        result["THREATFOX"] = COMPROMIZE.checkCompromisedURL(domain)
        result["VIRUSTOTAL"] = VT.findVirusTotalResult(domain)
        result["WAPITI"] = VUL.vulnerabilityFinder(domain)
        result["CMS"] = CMS.startCMSChecks(domain)
        
        if name:
            result["CSA"] = CSA.checkCSAexists(name)
            result["VISA"] = VISA.mainCheckVISA(name)
        
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
        penalty = 0
        for testType in ["HIBP", "CMS", "WAPITI", "OPEN_PORTS"]:
            if testingRes[testType]:
                penalty += weights[testType]
        if testingRes["THREATFOX"]["isCompromised"] == 1:
            penalty += weights["THREATFOX"]
            
        if testingRes["MALWARE"]["isMalware"] == 1:
            penalty += weights["MALWARE"]
        
        if testingRes["VIRUSTOTAL"]["virusTotalScore"]:
            penalty += weights["VIRUSTOTAL"]
        
        score = (1 - penalty) * 100
        score = round(score, 2)
        
    except Exception as e:
        print(e)
        
    finally:
        return score

def mainScanner(domain, companyName = None):
    result = {
        "scanDetails" : None,
        "scanScore" : None,
            
    }
    
    testRes = testingDomainResults(domain, companyName)
    testScore = scoreResults(testRes)
    
    result["scanDetails"] = testRes
    result["scanScore"] = testScore
    
    return result


print(mainScanner("google.com", "google"))
# testres = testingDomainResults("myetherevvalliet.com", "google")
# print(scoreResults(testres))
