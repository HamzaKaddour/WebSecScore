import requests

# DNS and VirusTotal Score


def findVirusTotalResult(domain):
    result = {
        "virusTotalScore": None,
        "dns": None
    }
    try:
        headers = {"x-apikey": "0962e29cb20fb8983790150e256a76e7ba1b93f3e2ed6c6fe663284c03172711"}
        response = requests.get("https://www.virustotal.com/api/v3/domains/" + domain, headers=headers)
        core = response.json()
        result = {
        "virusTotalScore": core["data"]["attributes"]["last_analysis_stats"],
        "dns": core["data"]["attributes"]["last_dns_records"]
    }
    except Exception as e:
        print(e)
    finally:
        return result
    
print(findVirusTotalResult("google.com"))