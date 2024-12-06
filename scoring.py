from Tests import hibp as HIBP
from Tests import malware_detect as MW
from Tests import open_ports as OP
from Tests import threatfox as COMPROMIZE
from Tests import virusTotal as VT
from Tests import vul_wapiti as VUL
from Tests import whatcms as CMS
from Tests import csa as CSA
from Tests import visa_pci as VISA
import database as db

# from WebSecScore.Tests import 
import requests
import json

# TODO #
'''
ADD THE REGEX OF THE DOMAIN SO THAT IT TAKES DIFFERENT COMBINIZATIONS OF THE DOMAIN FORMAT
'''



def testingDomainResults(domain, name = None):
    resultDetails = {
        "HIBP" : None, 
        "MALWARE" : None, 
        "OPEN_PORTS" : None, 
        "THREATFOX" : None, 
        "VIRUSTOTAL" : None, 
        "WAPITI" : None, 
        "CMS" : None, 
    }

    resultStatus = {
        "HIBP" : False, 
        "MALWARE" : False, 
        "OPEN_PORTS" : False, 
        "THREATFOX" : False, 
        "VIRUSTOTAL" : False, 
        "WAPITI" : False, 
        "CMS" : False, 
    }
    
    try:
        # Scan Details
        resultDetails["HIBP"] = HIBP.checkHIBP(domain) 
        resultDetails["MALWARE"] = MW.checkMalwareURL(domain)
        resultDetails["OPEN_PORTS"] = OP.scan_open_ports(domain)
        resultDetails["THREATFOX"] = COMPROMIZE.checkCompromisedURL(domain)
        resultDetails["VIRUSTOTAL"] = VT.findVirusTotalResult(domain)
        resultDetails["WAPITI"] = VUL.vulnerabilityFinder(domain)
        resultDetails["CMS"] = CMS.startCMSChecks(domain)
        
        # ScanStatus
        resultStatus = {
        "HIBP" : len(resultDetails["HIBP"]) > 0, 
        "MALWARE" : resultDetails["MALWARE"]["isMalware"] > 0, 
        "OPEN_PORTS" : len(resultDetails["OPEN_PORTS"]) > 0, 
        "THREATFOX" : resultDetails["THREATFOX"]["isCompromised"] > 0, 
        "VIRUSTOTAL" : len(resultDetails["VIRUSTOTAL"]["virusTotalInfo"]) > 0, 
        "WAPITI" : resultDetails["WAPITI"] != {}, 
        "CMS" : len(resultDetails["CMS"]) > 0, 
    }
        if name:
            resultDetails["CSA"] = CSA.checkCSAexists(name)
            resultDetails["VISA"] = VISA.mainCheckVISA(name)
            resultStatus["CSA"] = CSA.checkCSAexists(name)
            resultStatus["VISA"] = len(resultDetails["VISA"]) > 0
            
            
            
    except Exception as e:
        print(e)
        
    finally:
        return resultDetails, resultStatus


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
        "scanStatus" : None,
        "scanDetails" : None,
        "scanScore" : None,
            
    }
    
    if db.checkDomainExists(domain):
        scanResults = db.getDomainScanResults(domain)
        result["scanScore"] = scanResults["score"]
        result["scanStatus"] = scanResults["scanStatus"]
        result["scanDetails"] = scanResults
    
    else:
    
        testRes = testingDomainResults(domain, companyName)
        testScore = scoreResults(testRes[0])
        
        result["scanDetails"], result["scanStatus"] = testRes
        result["scanScore"] = testScore
        
        db.InsertUpdate(domain, result, companyName)
    
    return result

# mainScanner("google.com", "amazon")