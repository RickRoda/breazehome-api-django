from math import cos, sin, radians, degrees, asin, atan2
from real_estate.utilities import Utilities
from django.conf import settings
from time import sleep
import sys

class Polygons():
    """
    Internal class to contain f(x)'s that are in service of geometric polygon generation for forward facing BH logic.
    """

    #BEGIN PoLR isochrone polygon generation code

    def get_isochrone(origin_geocode, arrival_datetime, travel_duration, travel_mode, polr_settings):  #add more arguments as necessary here for supporting additional isochrone generation parameters.
        #inspired by Drew Fustin, https://github.com/drewfustin/isocronut/blob/master/isocronut.py, his is a clever algorithm;  I reversed the direction of the radial vectors (i.e. from radial points inward to origin)

        max_radial_distance = [float(travel_duration) * float(polr_settings.polr_max_mpm)] * polr_settings.polr_search_angles #this might have to change for higher speed transit options like rail
        phi = [iterator * (360 / polr_settings.polr_search_angles) for iterator in range(polr_settings.polr_search_angles)]             
        travel_duration_seconds_upperbound = (float(travel_duration) * 60.0) * (1.00 + float(polr_settings.polr_duration_max_tolerance))
        travel_duration_seconds_lowerbound = (float(travel_duration) * 60.0) * (1.00 - float(polr_settings.polr_duration_max_tolerance))
        is_diverged_isoline = [True] * polr_settings.polr_search_angles
        unconverged_isolines = [0] * polr_settings.polr_search_angles
        min_radial_distance = [0] * polr_settings.polr_search_angles
        isochrone = [0] * polr_settings.polr_search_angles
        next_radial_search_distance = list(max_radial_distance)
        distance_matrix_iterator = 0
        distance_matrix = None
        search_iterator = 0
        angle_iterator = 0
        
        if settings.POLR_DEBUG_LEVEL >= 1: sys.stderr.write("get_isochrone() started\n\torigin_geocode == {0}\n\tarrival_datetime == {1}\n\ttravel_duration == {2}\n\ttravel_mode == {3}\n".format(origin_geocode, arrival_datetime, travel_duration, travel_mode))

        while search_iterator < int(polr_settings.polr_search_iterations) and Polygons.is_divergent_radial_set(min_radial_distance, max_radial_distance):  #min_radial_distance == max_radial_distance occurs on convergence of travel_duration to the bounded range +/- travel_duration_seconds
 
            #calculate the locations from the origin that are in radial distance in search range 
            for angle_iterator in range(polr_settings.polr_search_angles):
                if is_diverged_isoline[angle_iterator]:
                    isochrone[angle_iterator] = Polygons.get_radial_destination_geocode(origin_geocode, phi[angle_iterator], next_radial_search_distance[angle_iterator])
                    unconverged_isolines[distance_matrix_iterator] = isochrone[angle_iterator]
                    distance_matrix_iterator += 1

            #set them as the distal starting points heading towards origin for the distance matrix call
            distance_matrix = Utilities.get_distance_matrix(unconverged_isolines, origin_geocode, arrival_datetime, travel_mode, polr_settings) #add more arguments as necessary here for supporting additional isochrone generation parameters.
            distance_matrix_iterator = 0

            if distance_matrix["status"] == "OK":

                if settings.POLR_DEBUG_LEVEL >= 3: sys.stderr.write("\tget_isochrone() finds {0}\n".format(distance_matrix))

                for angle_iterator in range(polr_settings.polr_search_angles):
                    if is_diverged_isoline[angle_iterator]:
                        if distance_matrix["rows"][distance_matrix_iterator]["elements"][0]["status"] == "OK":                            
                            if travel_duration_seconds_lowerbound <= float(distance_matrix["rows"][distance_matrix_iterator]["elements"][0]["duration"]["value"]) <= travel_duration_seconds_upperbound:
                                 #we have converged on a point that is a match for the travel_duration distance from the origin, heading towards the origin from some point on the radius of search_angle that is away from it
                                if settings.POLR_DEBUG_LEVEL >= 1: sys.stderr.write("\tget_isochrone() angle {0} converges on {1} with distance {2} after {3} iterations\n".format(phi[angle_iterator], ",".join(str(component) for component in unconverged_isolines[distance_matrix_iterator]), max_radial_distance[angle_iterator], search_iterator))

                                min_radial_distance[angle_iterator] = max_radial_distance[angle_iterator] = next_radial_search_distance[angle_iterator]
                                is_diverged_isoline[angle_iterator] = False
                            else:
                                if float(distance_matrix["rows"][distance_matrix_iterator]["elements"][0]["duration"]["value"]) < travel_duration_seconds_lowerbound:
                                    #then there exists a point further from the origin_geocode that has a match for the travel_duration, therefore we move the radial search point out further and search again on the next pass
                                    if settings.POLR_DEBUG_LEVEL >= 2: sys.stderr.write("\tget_isochrone() angle {0} extending on iteration {1}; current next, min, and max == {2}, {3}, {4}\n".format(phi[angle_iterator], search_iterator, next_radial_search_distance[angle_iterator], min_radial_distance[angle_iterator], max_radial_distance[angle_iterator]))
                            
                                    min_radial_distance[angle_iterator] = next_radial_search_distance[angle_iterator] #next_radial_search_distance[angle_iterator] refers to the previous iteration, hence, it really represents the "previous" next_radial_search_distance[angle_iterator]
                                    next_radial_search_distance[angle_iterator] = (max_radial_distance[angle_iterator] + min_radial_distance[angle_iterator]) / 2

                                    if settings.POLR_DEBUG_LEVEL >= 2: sys.stderr.write("\tget_isochrone() angle {0} extending on iteration {1}; new next, min, and max == {2}, {3}, {4}\n".format(phi[angle_iterator], search_iterator, next_radial_search_distance[angle_iterator], min_radial_distance[angle_iterator], max_radial_distance[angle_iterator]))
                                else:
                                    #then there exists a point closer to the origin_geocode that has a match for the travel_duration, therefore we move the radial search point in closer and search again on the next pass
                                    if settings.POLR_DEBUG_LEVEL >= 2: sys.stderr.write("\tget_isochrone() angle {0} retracting on iteration {1}; current next, min, and max == {2}, {3}, {4}\n".format(phi[angle_iterator], search_iterator, next_radial_search_distance[angle_iterator], min_radial_distance[angle_iterator], max_radial_distance[angle_iterator]))
                                
                                    max_radial_distance[angle_iterator] = next_radial_search_distance[angle_iterator] #next_radial_search_distance[angle_iterator] refers to the previous iteration, hence, it really represents the "previous" next_radial_search_distance[angle_iterator]
                                    next_radial_search_distance[angle_iterator] = (max_radial_distance[angle_iterator] + min_radial_distance[angle_iterator]) / 2

                                    if settings.POLR_DEBUG_LEVEL >= 2: sys.stderr.write("\tget_isochrone() angle {0} retracting on iteration {1}; new next, min, and max == {2}, {3}, {4}\n".format(phi[angle_iterator], search_iterator, next_radial_search_distance[angle_iterator], min_radial_distance[angle_iterator], max_radial_distance[angle_iterator]))
                        else: #we've received a ZERO_RESULTS, NOT_FOUND, or MAX_LENGTH_EXCEEDED and our estimate went too far; therefore we move the radii in closer and search again on the next                     
                            if settings.POLR_DEBUG_LEVEL >= 2: sys.stderr.write("\tget_isochrone() angle {0} status != OK, retracting on iteration {1}; current next, min, and max == {2}, {3}, {4}\n".format(phi[angle_iterator], search_iterator, next_radial_search_distance[angle_iterator], min_radial_distance[angle_iterator], max_radial_distance[angle_iterator]))
                        
                            max_radial_distance[angle_iterator] = next_radial_search_distance[angle_iterator] #next_radial_search_distance[angle_iterator] refers to the previous iteration, hence, it really represents the "previous" next_radial_search_distance[angle_iterator]
                            next_radial_search_distance[angle_iterator] = (max_radial_distance[angle_iterator] + min_radial_distance[angle_iterator]) / 2

                            if settings.POLR_DEBUG_LEVEL >= 2: sys.stderr.write("\tget_isochrone() angle {0} status != OK, retracting on iteration {1}; new next, min, and max == {2}, {3}, {4}\n".format(phi[angle_iterator], search_iterator, next_radial_search_distance[angle_iterator], min_radial_distance[angle_iterator], max_radial_distance[angle_iterator]))

                        distance_matrix_iterator += 1
            else:
                raise RuntimeError("\tget_isochrone() could not successfully process a call to Utilities.get_distance_matrix()")
            
            #throttle to not blow out the per second API call limit
            if settings.POLR_DEBUG_LEVEL >= 1: sys.stderr.write("\tget_isochrone() sleeping for {0} seconds\n".format(float(len(unconverged_isolines)) / float(polr_settings.polr_google_matrix_elements_ps)))
            sleep(float(len(unconverged_isolines)) / float(polr_settings.polr_google_matrix_elements_ps)) 
            
            #reset the vector and counter states for the new isolines that have not converged, increment the search attempt, do it all again if applicable
            unconverged_isolines = [0] * int(sum(is_diverged_isoline)) 
            distance_matrix_iterator = 0
            search_iterator += 1

        return isochrone

    def is_divergent_radial_set(lowerbound_radial_array, upperbound_radial_array):

        radial_sum = 0
        iterator = 0

        for iterator in range(len(lowerbound_radial_array)):
            radial_sum += lowerbound_radial_array[iterator] - upperbound_radial_array[iterator]

        return radial_sum != 0

    def get_radial_destination_geocode(location_geocode, arc_angle, radius_length): #finds the location on a sphere a distance 'radius' along a bearing 'angle' from origin.  Uses haversines rather than simple Pythagorean distance in Euclidean space
        #taken from Drew Fustin, select_destination, https://github.com/drewfustin/isocronut/blob/master/isocronut.py, give credit where credit is due, I would have learned this the hard way and missed the spherical distance/need for haversines at first

        origin_lat = radians(location_geocode[0])
        origin_lng = radians(location_geocode[1])
        bearing = radians(arc_angle)
        EARTH_RADIUS = 3963.1676

        destination_lat = asin(sin(origin_lat) * cos(radius_length / EARTH_RADIUS) + cos(origin_lat) * sin(radius_length / EARTH_RADIUS) * cos(bearing))
        destination_lng = origin_lng + atan2(sin(bearing) * sin(radius_length / EARTH_RADIUS) * cos(origin_lat), cos(radius_length / EARTH_RADIUS) - sin(origin_lat) * sin(destination_lat))     

        return [degrees(destination_lat), degrees(destination_lng)]

    #END PoLR isochrone polygon generation code