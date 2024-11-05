import requests
# from Services import utilities
from Tests.Services import utilities

# DNS and VirusTotal Score


def findVirusTotalResult(domain):
    result = {
        "virusTotalScore": 0,
        "virusTotalInfo": None,
        "dns": None,
        "communityScore" : None
    }
    try:
        headers = {"x-apikey": utilities.getEnvironmentVariable('VIRUSTOTAL')}
        response = requests.get("https://www.virustotal.com/api/v3/domains/" + domain, headers=headers)
        core = response.json()
        result = {
        "virusTotalScore": 0,
        "virusTotalInfo": core["data"]["attributes"]["last_analysis_stats"],
        "dns": core["data"]["attributes"]["last_dns_records"],
        "communityScore" : core["data"]["attributes"]["reputation"]
    }
        totalFlags = 0
        badFlag = result["virusTotalInfo"]['malicious'] + result["virusTotalInfo"]['suspicious']
        harmlessFlag = result["virusTotalInfo"]['harmless']
        if badFlag >= harmlessFlag or result["communityScore"] < 0:
            result["virusTotalScore"] = 1
            
    except Exception as e:
        print(e)
    finally:
        return result
    
# print(findVirusTotalResult("google.com.cust_login.ie"))