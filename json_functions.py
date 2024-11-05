# This is the file within which the JSON-related functions will be stored.
from urllib.request import urlopen
import json
import requests

# GETTERS

# Fetches JSON from a given site
def getjson(site):
    r = requests.get(site)
    return r.json()

# SETTERS