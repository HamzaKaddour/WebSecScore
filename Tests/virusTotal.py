import requests
# from Services import utilities
from Tests.Services import utilities

# DNS and VirusTotal Score


def findVirusTotalResult(domain):
    result = {
        "virusTotalScore": None,
        "dns": None,
        "communityScore" : None
    }
    try:
        headers = {"x-apikey": utilities.getEnvironmentVariable('VIRUSTOTAL')}
        response = requests.get("https://www.virustotal.com/api/v3/domains/" + domain, headers=headers)
        core = response.json()
        result = {
        "virusTotalScore": core["data"]["attributes"]["last_analysis_stats"],
        "dns": core["data"]["attributes"]["last_dns_records"],
        "communityScore" : core["data"]["attributes"]["reputation"]
    }
    except Exception as e:
        print(e)
    finally:
        return result
    
# print(findVirusTotalResult("google.com"))