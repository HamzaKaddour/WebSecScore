import requests


def firstInit():
    """
    This function is called on the first time to bring the hibp breach data and store in DB
    
    """
    url = "https://haveibeenpwned.com/api/v3/breaches"
    res = requests.get(url)

    print(res.content)

def updateHIBP():
    url = "https://haveibeenpwned.com/api/v3/latestbreach"
    res = requests.get(url)

    print(res.content)
    
    
updateHIBP()