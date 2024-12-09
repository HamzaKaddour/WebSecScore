
# This function is to prevent from SQL injection by monitoring the inputs from the domain and company name
# This comes as a second layer as controls are already implemented on FE side

import re

def is_valid_domain(domain):
    domain_regex = r"^(?!:\/\/)([a-zA-Z0-9-_]+\.)*[a-zA-Z0-9][a-zA-Z0-9-_]+\.[a-zA-Z]{2,11}?$"
    return re.match(domain_regex, domain)

def is_valid_company_name(company_name):
    company_name_regex = r"^[a-zA-Z0-9\s-]+$"
    return re.match(company_name_regex, company_name)