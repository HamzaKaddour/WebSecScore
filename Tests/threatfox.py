# Compromised IP or not

import requests
# import Services.utilities
from Tests.Services import utilities

def checkCompromisedURL(domain):
    result = {
        "isCompromised" : 0,
        "info" : None
    }
    
    try:
        ip_addr = utilities.hostname_to_ip(domain)
    except Exception as e:
        print(e)
        return result
        
    
    url = "https://threatfox-api.abuse.ch/api/v1/"
    data = {
    "query": "search_ioc",
    "search_term": ip_addr
    # "search_term": "139.180.203.104"
    }

    
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            response_json = response.json()
            # print(response_json)
            if response_json["query_status"] == "no_result":
                return result
            elif response_json["query_status"] == "ok":
                result["isCompromised"] = 1
                result["info"] = response_json["data"]
            else:
                result["info"] = "This is not a valid URL"
        else:
            result["info"] = "invalid response code"
    except Exception as e:
        print("ThreatFox IP Warning: ",e)
    finally:
        return result
            
                	
# print(checkCompromisedURL("http://sskymedia.com/VMYB-ht_JAQo-gi/INV/99401FORPO/20673114777/US/Outstanding-Invoices/"))

# print(utilities.hostname_to_ip("http://sskymedia.com/VMYB-ht_JAQo-gi/INV/99401FORPO/20673114777/US/Outstanding-Invoices/"))
# print(checkCompromisedURL("google.com"))