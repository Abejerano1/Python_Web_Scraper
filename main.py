# This is the file within which the main processes will be executed

import json_functions
import html_xml_functions
from bs4 import BeautifulSoup

# Class file for websites
from websites import *

# Variable taking URL from user input
# targetURL = https://webscraper.io/test-sites/e-commerce/allinone/product/71
# targetURL = input("Paste website URL to find product information:\n")
targetURL = "https://webscraper.io/test-sites/e-commerce/allinone/product/71"

# Variable storing our response to an HTTP request from a web server

# Our status code
statusCode = html_xml_functions.getstatus(targetURL)

# CHECK STATUS CODE:
print("Acquiring status code...")
if statusCode is not None:
    if statusCode == 200:
        # f-string here:
        print(f"Success!\nStatus code: {statusCode}")

    else:
        print("Failed.")
print()

urlContents = html_xml_functions.getcontent(targetURL)
markup = urlContents
soup = BeautifulSoup(markup, "html.parser")
soup.prettify()

# ========================= #
# PRINT PRODUCT INFORMATION #
# ========================= #

print("Product information: ")
print(f"Name: {html_xml_functions.testgetname(targetURL)}")
print(f"Base price: {html_xml_functions.testgetprice(targetURL)}")
print(f"Description: {html_xml_functions.testgetdescription(targetURL)}")
print(f"SKU: NONE (for now) :)")
print()

# ====================== #
# PRINT JSON INFORMATION #
# ====================== #

print("JSON data from https://api.github.com/...")

# Print test JSON from requests library website
print(json_functions.getjson("https://docs.python-requests.org/"
                             "_/addons/?client-version=0.19.0&api-version=1&project-slug=requests&version-slug=latest"))
print()

tester = TestWebsite("Webscraper", "https://webscraper.io/test-sites/e-commerce/allinone/product/71")

# Print website class
print("WEBSITE AS A CLASS:")
print("Company: ", tester.company)
print("URL: ", tester.url)
print()

# PRINT METHOD CALL FROM CLASS
print(tester.fullname())

# TO-DO:
# 1. Search through JSON file for specific information
# 2. Print target information
# 3. Clean up main
# 4. Set up classes for each website
