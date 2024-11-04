import requests
from bs4 import BeautifulSoup


# GETTERS

# Function that retrieves status code from a site
def getstatus(url):
    try:
        result = requests.get(url)
        return result.status_code
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
        # In case of exception, return nothing


# Function that retrieves HTML contents from a site
def getcontent(url):
    try:
        result = requests.get(url)
        return result.content
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
        # In case of exception, return nothing

# Function that returns the price information from a product page
def testgetprice(url):
    markup = getcontent(url)
    soup = BeautifulSoup(markup, "html.parser")
    return soup.find("h4").text

# Function that returns the name of a product from a product page
def testgetname(url):
    markup = getcontent(url)
    soup = BeautifulSoup(markup, "html.parser")
    return soup.find("h4", class_="title card-title").text

# Function that returns the description of a product from a product page
def testgetdescription(url):
    markup = getcontent(url)
    soup = BeautifulSoup(markup, "html.parser")
    return soup.find("p", class_="description card-text").text
