# # import requests

# # def search_company_in_visa_registry(company_name):
# #     # URL of the Visa registry search page
# #     url = "https://www.visa.com/splisting/searchGrsp.do"
    
# #     # Payload with the company name and other required parameters
# #     payload = {
# #         "coName": company_name,
# #         "participatingFilterOptionsList": "",
# #         "technologiesList": "",
# #         "programList": "",
# #         "assessorList": "",
# #         "serviceList": "",
# #         "regionList": "",
# #         "serviceProviderTypeList": "",
# #         "HeadCountryList": "",
# #         "stateList": "",
# #         "validStart": "",
# #         "validEnd": "",
# #         "pageInfo": "1;30;ASC;coName"
# #     }

# #     # Headers to mimic a browser request
# #     headers = {
# #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
# #         "Content-Type": "application/x-www-form-urlencoded"  # Ensures server interprets payload correctly
# #     }

# #     # Send the POST request
# #     try:
# #         response = requests.post(url, data=payload, headers=headers)

# #         # Check if the request was successful
# #         if response.status_code == 200:
# #             # Verify if the response is JSON
# #             if response.headers.get("Content-Type") == "application/json":
# #                 data = response.json()
                
# #                 # Check if the response contains results
# #                 if data.get("retcode") == "OK" and data.get("totalRecords", 0) > 0:
# #                     # Iterate over the results and check for the company name
# #                     for result in data.get("resultSet", []):
# #                         if company_name.lower() in result.get("companyName", "").lower():
# #                             print(f"Company '{company_name}' is listed in the Visa registry.")
# #                             print("Details:", result)
# #                             return True
# #                     print(f"Company '{company_name}' is NOT listed in the Visa registry.")
# #                     return False
# #                 else:
# #                     print(f"No results found for company '{company_name}'.")
# #                     return False
# #             else:
# #                 print("Response is not in JSON format.")
# #                 print(response.text)  # Print the raw response for debugging
# #                 return None
# #         else:
# #             print(f"Failed to retrieve data. Status code: {response.status_code}")
# #             return None

# #     except requests.exceptions.RequestException as e:
# #         print(f"An error occurred: {e}")
# #         return None

# # # Example usage
# # company_name = "Google"
# # search_company_in_visa_registry(company_name)

# import requests
# import json  # Import the json module to handle JSONDecodeError

# # URL for the GET request
# get_url = "https://www.visa.com/splisting/searchCompanyName.do"
# # URL for the POST request
# post_url = "https://www.visa.com/splisting/searchGrspAjax.do"

# # Headers common for both requests
# headers = {
#     "Accept": "application/json, text/javascript, */*; q=0.01",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "en-US,en;q=0.9",
#     "Connection": "keep-alive",
#     "Referer": "https://www.visa.com/splisting/searchGrsp.do",
#     "Sec-Fetch-Dest": "empty",
#     "Sec-Fetch-Mode": "cors",
#     "Sec-Fetch-Site": "same-origin",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
#     "X-Requested-With": "XMLHttpRequest",
# }

# # First request: GET request to search for the company name
# company_name = "google"
# get_params = {"term": company_name}

# # Sending the GET request
# response_get = requests.get(get_url, headers=headers, params=get_params)

# # Check if GET request was successful
# if response_get.status_code == 200:
#     try:
#         # Attempt to parse JSON
#         json_data = response_get.json()
#         print("GET Response JSON:", json_data)
#     except json.JSONDecodeError:
#         # Print raw text if not JSON
#         print("GET response is not JSON format. Raw text:")
#         print(response_get.text)
# else:
#     print("GET Request failed with status:", response_get.status_code)

# # Second request: POST request with additional payload for details
# post_payload = {
#     "term": company_name,
#     # Add any other necessary POST parameters here
# }

# # Sending the POST request
# response_post = requests.post(post_url, headers=headers, data=post_payload)

# # Check if POST request was successful
# if response_post.status_code == 200:
#     try:
#         # Attempt to parse JSON
#         json_data_post = response_post.json()
#         print("POST Response JSON:", json_data_post)
#     except json.JSONDecodeError:
#         # Print raw text if not JSON
#         print("POST response is not JSON format. Raw text:")
#         print(response_post.text)
# else:
#     print("POST Request failed with status:", response_post.status_code)

import requests
import json  # Import json for JSONDecodeError handling

# URL for the GET request
get_url = "https://www.visa.com/splisting/searchCompanyName.do"
# URL for the POST request
post_url = "https://www.visa.com/splisting/searchGrspAjax.do"

# Headers for both requests, without Accept-Encoding
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Referer": "https://www.visa.com/splisting/searchGrsp.do",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

# First request: GET request to search for the company name
company_name = "google"
get_params = {"term": company_name}

# Sending the GET request
response_get = requests.get(get_url, headers=headers, params=get_params)

# Check if GET request was successful
if response_get.status_code == 200:
    try:
        # Try decoding JSON response
        json_data = response_get.json()
        print("GET Response JSON:", json_data)
    except json.JSONDecodeError:
        # If JSON decoding fails, try manual decompression if the content is encoded
        print("GET response is not JSON format. Attempting to decode raw content.")
        content = response_get.content
        if response_get.headers.get('Content-Encoding') == 'gzip':
            import gzip
            content = gzip.decompress(content).decode('utf-8')
        elif response_get.headers.get('Content-Encoding') == 'br':
            import brotli
            content = brotli.decompress(content).decode('utf-8')
        print("Decompressed content:", content)
else:
    print("GET Request failed with status:", response_get.status_code)

# Second request: POST request with additional payload for details
post_payload = {
    "term": company_name,
    # Add any other necessary POST parameters here
}

# Sending the POST request
response_post = requests.post(post_url, headers=headers, data=post_payload)

# Check if POST request was successful
if response_post.status_code == 200:
    try:
        # Attempt to parse JSON
        json_data_post = response_post.json()
        print("POST Response JSON:", json_data_post)
    except json.JSONDecodeError:
        # Print raw text if not JSON
        print("POST response is not JSON format. Raw text:")
        print(response_post.text)
else:
    print("POST Request failed with status:", response_post.status_code)


# POST REQUEST PARSING
'''
resultSet > [companyName, assessorCompanyName, registeredSince, validationTypeMap]
validationTypeMap > each element in it > assessorCompanyName, validationType, serviceProviderTypeList, validationDate(if any)
'''
