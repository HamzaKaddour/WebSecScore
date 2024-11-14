# System Libaries
import json
import requests

from Tests.Services import utilities


def startCMSChecks(url):
    # global data

    try:
        
        # whatCMSApiKey = "w2asiod8dvft0qj1lmfdowp1ixvp0tj6gwxca1euivgdz1p0md2mfvhlkk34bsyw5jhxva"
        whatCMSApiKey = utilities.getEnvironmentVariable('WHATCMS')
        
        # api = requests.get('https://whatcms.org/APIEndpoint/Detect?key=' + whatCMSApiKey + '&url=' + url)
        api = requests.get('https://whatcms.org/API/Tech?key=' + whatCMSApiKey + '&url=' + url)

        # Retrieve cms data
        cmsinfo = api.json()
        return cmsinfo['results'] if cmsinfo['results'] else []
        
    except Exception as e:
        print("WHATCMS Warning: ",e)
        jsonResult = {"WhatCMS_Scan": "Failed", "FailReason": "No address associated with hostname"}   
        return []

# print(startCMSChecks('wordpress.com'))

