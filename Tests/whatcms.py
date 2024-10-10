# System Libaries
import json
import requests

from Services import logging
logging = logging.LogWrapper(__name__)



# class InvalidHIBPException(Exception):
#     pass

# def triggerScan(dbConnection, sSiteName, scanBlob, filenames):
#     outputFilename = filenames["output"]
#     resultFilename = filenames["result"]
#     dependenciesPath = filenames["dependencies"]

#     startCMSChecks(sSiteName, outputFilename)
#     successfulScan = database.storeScan(dbConnection, scanBlob, outputFilename)

#     verifyWhatCMSResults(outputFilename, resultFilename, dependenciesPath)
#     successfulResult = database.storeCheck(dbConnection, scanBlob, resultFilename)

#     if (successfulScan and successfulResult):
#         return True
#     else:
#         return False


def startCMSChecks(url):
    global data

    try:
        whatCMSApiKey = "w2asiod8dvft0qj1lmfdowp1ixvp0tj6gwxca1euivgdz1p0md2mfvhlkk34bsyw5jhxva"
        
        # api = requests.get('https://whatcms.org/APIEndpoint/Detect?key=' + whatCMSApiKey + '&url=' + url)
        api = requests.get('https://whatcms.org/API/Tech?key=' + whatCMSApiKey + '&url=' + url)

        # Retrieve cms data
        cmsinfo = api.json()
        return cmsinfo['results'] if cmsinfo['results'] else []
        
    except Exception:
        logging.exception()
        jsonResult = {"WhatCMS_Scan": "Failed", "FailReason": "No address associated with hostname"}   

print(startCMSChecks('wordpress.com'))

