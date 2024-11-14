import requests
import json  # Import json for JSONDecodeError handling



def checkCompanyVisaExist(company_name, get_url, headers):

# First request: GET request to search for the company name
# company_name = "google"
    get_params = {"term": company_name}

    # Sending the GET request
    response_get = requests.get(get_url, headers=headers, params=get_params)

    # Check if GET request was successful
    if response_get.status_code == 200:
        try:
            # Try decoding JSON response
            json_data = response_get.json()
            # print("GET Response JSON:", json_data)
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
        except Exception as e:
            print(e)
    else:
        print("GET Request failed with status:", response_get.status_code)

    return json_data


    
def mainCheckVISA(companyName):
    result = []
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
    
    isExist = checkCompanyVisaExist(companyName, get_url, headers)
    if isExist:
        for element in isExist:
            cpny = element.get("value", None)
            if cpny:
                result.append(cpny)
            
            cpny = None
    return result

# print(mainCheckVISA("google"))






# # def formatVISAResponse(jsonData):
    
#     companyName = jsonData.get("companyName", None)
#     assessorCompanyName = jsonData.get("assessorCompanyName", None)
#     dateOfRegistration = jsonData.get("registeredSince", None)
#     try:
#         certifications =  jsonData["resultSet"]
        
#         if certifications:
#             for certDict in certifications:
#                 for cert in certDict["validationTypeMap"].values():
#                     assessorCompanyNameCert = cert.get("assessorCompanyName", None)
#                     certificationName = cert.get("validationType", None) 
#                     serviceProviderTypeList = cert.get("serviceProviderTypeList", None)
#                     validationDate = cert.get("validationDate", None) 
#     except Exception as e:
#         print(e)
        
#     result = {
#         "companyName" : companyName if companyName else None,
#         "assessorCompanyName" : assessorCompanyName if assessorCompanyName else None,
#         "registeredSince" : dateOfRegistration if dateOfRegistration else None,
#         "certificationDetails" : {
#             "assessorCompanyNameCert" : assessorCompanyNameCert if assessorCompanyNameCert else None,
#             "certification" : certificationName if certificationName else None,
#             "serviceProviderTypeList" : serviceProviderTypeList if serviceProviderTypeList else None,
#             "validationDate" : validationDate if validationDate else None,
#             },        
#     }
    
#     return result
    
    

# # def getCompanyVisaDetails(company_name, post_url, headers):
#     res = []
#     # Second request: POST request with additional payload for details
#     post_payload = {
#         "term": company_name,
#         # Add any other necessary POST parameters here
#     }

#     # Sending the POST request
#     response_post = requests.post(post_url, headers=headers, data=post_payload)

#     # Check if POST request was successful
#     if response_post.status_code == 200:
#         try:
#             # Attempt to parse JSON
#             json_data_post = response_post.json()
#             # print("POST Response JSON:", json_data_post)
#             res = get_certification_details(json_data_post)
#             # print("POST Response JSON:", res)
#         except json.JSONDecodeError:
#             # Print raw text if not JSON
#             print("POST response is not JSON format. Raw text:")
#             print(response_post.text)
#         except Exception as e:
#             print(e)
#     else:
#         print("POST Request failed with status:", response_post.status_code)
#     return res


# # POST REQUEST PARSING
# '''
# resultSet > [companyName, assessorCompanyName, registeredSince, validationTypeMap]
# validationTypeMap > each element in it > assessorCompanyName, validationType, serviceProviderTypeList, validationDate(if any)
# '''

# def get_certification_details(data):
#     companies = []
#     result_set = data.get('resultSet', [])

#     for company in result_set:
#         # Basic company information
#         company_data = {
#             "companyName": company.get("companyName"),
#             "assessorCompanyName": company.get("assessorCompanyName"),
#             "registeredSince": company.get("registeredSince"),
#             "certifications": []
#         }

#         # Extract certifications from validationTypeMap
#         validation_type_map = company.get("validationTypeMap", {})
#         for cert_name, cert_info in validation_type_map.items():
#             certification_data = {
#                 "certificationName": cert_name,
#                 "assessorCompanyName": cert_info.get("assessorCompanyName"),
#                 "validationType": cert_info.get("validationType"),
#                 "serviceProviderTypeList": cert_info.get("serviceProviderTypeList", []),
#                 "validationDate": cert_info.get("validationDate", None)
#             }
#             company_data["certifications"].append(certification_data)

#         companies.append(company_data)

#     return companies

# Using the function to get the structured output
# structured_output = get_certification_details(response_data)

# # Displaying the structured output
# for company in structured_output:
#     print(company)