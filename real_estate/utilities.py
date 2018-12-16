from django.conf import settings
import urllib
import json
import sys
from admins.models import Configuration
 
class Utilities():
    """ 
    Internal class to contain supplemental f(x)'s that are utilitarian to BH business logic but directly in service of forward facing BH logic.
    """
    #BEGIN PoLR utility function code

    def get_distance_matrix(origin_geocodes, destination_geocode, arrival_datetime, travel_mode, polr_settings):

        distance_matrix_API_URL = settings.POLR_GOOGLE_DISTANCEMATRIX_API_URL.format(
            urllib.parse.urlencode({ "" : polr_settings.google_api_key }), 
            urllib.parse.urlencode( { "" : "|".join(",".join(str(component) for component in geocode) for geocode in origin_geocodes) }), 
            urllib.parse.urlencode( { "" : ",".join(str(component) for component in destination_geocode) }), 
            urllib.parse.urlencode({ "" : travel_mode }), 
            urllib.parse.urlencode( { "" : arrival_datetime })  
            #add more arguments as necessary here for supporting additional isochrone generation parameters., additional API call parameters would go here such that they line up with the token ordinals defined in settings.POLR_GOOGLE_DISTANCEMATRIX_API_URL            
        )

        if settings.POLR_DEBUG_LEVEL >= 3: sys.stderr.write(distance_matrix_API_URL + "\n")
        response = Utilities.execute_remote_API_call(distance_matrix_API_URL)

        if response["status"] != "OK":
            raise RuntimeError("get_distance_matrix() could not successfully process the requested API call.  origin_geocodes == {0}, destination_geocode == {1}, arrival_datetime == {2}, travel_mode == {3}, response == {4}".format(
                origin_geocodes, destination_geocode, arrival_datetime, travel_mode, response)
            )

        return response 

    def get_geocode(origin_address, polr_settings):

        geocode_API_URL = settings.POLR_GOOGLE_GEOCODE_API_URL.format(urllib.parse.urlencode({ "" : polr_settings.google_api_key }), urllib.parse.urlencode( { "" : origin_address }))
        
        if settings.POLR_DEBUG_LEVEL >= 3: sys.stderr.write(geocode_API_URL + "\n")
        response = Utilities.execute_remote_API_call(geocode_API_URL)

        if response["status"] != "OK":
            raise RuntimeError("get_geocode() could not successfully process the requested origin_address.  origin_address == {0}, response == {1}".format(origin_address, response))

        return [response["results"][0]["geometry"]["location"]["lat"], response["results"][0]["geometry"]["location"]["lng"]]

    def execute_remote_API_call(service_URL):

        response = urllib.request.urlopen(service_URL)
        return json.loads(response.read().decode("utf-8"))

    #END PoLR utility function code