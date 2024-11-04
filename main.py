# This is the file within which the main processes will be executed

import json_functions
import html_xml_functions
from bs4 import BeautifulSoup

# Variable taking URL from user input
# targetURL = https://webscraper.io/test-sites/e-commerce/allinone/product/71
targetURL = input("Paste website URL to find product information:\n")

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

# TO-DO:
# 1. Fetch JSON from a test website
# 2. Store JSON in a .txt file
# 3. Clean up main
# 4. Set up classes for each website
