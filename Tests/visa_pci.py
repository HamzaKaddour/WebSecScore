import requests

def search_company_in_visa_registry(company_name):
    # URL of the Visa registry search page
    url = "https://www.visa.com/splisting/searchGrsp.do"
    
    # Payload with the company name and other required parameters
    payload = {
        "coName": company_name,
        "participatingFilterOptionsList": "",
        "technologiesList": "",
        "programList": "",
        "assessorList": "",
        "serviceList": "",
        "regionList": "",
        "serviceProviderTypeList": "",
        "HeadCountryList": "",
        "stateList": "",
        "validStart": "",
        "validEnd": "",
        "pageInfo": "1;30;ASC;coName"
    }

    # Headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"  # Ensures server interprets payload correctly
    }

    # Send the POST request
    try:
        response = requests.post(url, data=payload, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Verify if the response is JSON
            if response.headers.get("Content-Type") == "application/json":
                data = response.json()
                
                # Check if the response contains results
                if data.get("retcode") == "OK" and data.get("totalRecords", 0) > 0:
                    # Iterate over the results and check for the company name
                    for result in data.get("resultSet", []):
                        if company_name.lower() in result.get("companyName", "").lower():
                            print(f"Company '{company_name}' is listed in the Visa registry.")
                            print("Details:", result)
                            return True
                    print(f"Company '{company_name}' is NOT listed in the Visa registry.")
                    return False
                else:
                    print(f"No results found for company '{company_name}'.")
                    return False
            else:
                print("Response is not in JSON format.")
                print(response.text)  # Print the raw response for debugging
                return None
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
company_name = "Google"
search_company_in_visa_registry(company_name)
