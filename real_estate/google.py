# START proximity search:acris005@fiu.edu


"""
I designed this module to hold all objects and functions associated with
accessing any google api. The way the module is organized is as follows:

The first section holds the imports neccessary to run the module.
Next are the api managers, which are basically objects that encapsulate
an api key along with associated api behaviors. After that are functions
with specific purposes: url functions build api urls, api functions send requests
to the api, and response functions handle api reponses.

As of now, I've only implemented a manager to the google maps api. Behaviors
include getting the coordinates from an address query. More google api managers 
can be added to the module and is suggested.
"""


# imports
from django.conf import settings
import urllib
import json


# api managers
class MapsAPI:
    def __init__(self, api_key):
        """
        goal: setup google maps api manager
        type: (Self, ApiKey) -> ()
        """

        self.api_key = api_key
    def get_coordinates(self, query):
        """
        goal: return the coordinates associated with a query
        type: (Self, String) -> (Latitude, Longitude)
        note: Latitude/Longitude are of type Float
        """

        api_url = url_address_search(query, self.api_key)
        response = api_call(api_url)

        if response["status"] == "OK":
            return parse_coordinates(response)
        else:
            raise RuntimeError("Error: Could not return coordinates from query")


# url functions
def url_address_search(query, api_key):
    """
    goal: create api url requesting google maps to search for an address
    type: (String, ApiKey) -> URL
    """

    api_url = settings.POLR_GOOGLE_GEOCODE_API_URL.format(
        urllib.parse.urlencode({"": api_key}),
        urllib.parse.urlencode({"": query})
    )
    return api_url


# api functions
def api_call(api_url):
    """
    goal: use api url to perform a request for an api resource
    type: (URL) -> JSON
    """

    response = urllib.request.urlopen(api_url)
    return json.loads(response.read().decode("utf-8"))


# response functions
def parse_coordinates(response):
    """
    goal: parse the coordinates from a response
    type: (JSON) -> (Latitude, Longitude)
    help: Latitude/Longitude are of type Float
    """

    lat = response["results"][0]["geometry"]["location"]["lat"]
    lng = response["results"][0]["geometry"]["location"]["lng"]

    return (lat, lng)


# END proximity search
