import requests


def checkHIBP(domain):
    """
    This function is called on the first time to bring the hibp breach data and store in DB
    
    """
    result = []
    try:
        url = "https://haveibeenpwned.com/api/v3/breaches"
        res = requests.get(url)

        if res.status_code == 200:
            content = res.json()
            for element in content:
                if element["Domain"] == domain:
                    result.append(element)
                    
         
    except Exception as e:
        print(e)
    finally:
        return result
            
def updateHIBP():
    url = "https://haveibeenpwned.com/api/v3/latestbreach"
    res = requests.get(url)

    return res.json()
    
    
# print(checkHIBP("google.com"))