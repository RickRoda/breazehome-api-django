"""
The purpose of this module is to hold functions that operate on coordinates.
Coordinates are of the form (Latitude, Longitude), which are of type
(Float, Float).

If you want to extend this module, ask yourself if the functions you include
are for the purpose of operating on coordinates.
"""


# imports
from math import sqrt


# coordinate functions
def degrees_to_miles(degrees):
    """
    goal: convert Latitude/Longitude degrees to miles
    type: (Float) -> Float
    """

    miles_per_degree = 69.172
    return degrees * miles_per_degree
def in_proximity(pt1, pt2):
    """
    goal: determine if point1 is in proximity to point2
    type: (Point, Point) -> Bool
    help: a Point is of type (Latitude, Longitude) which is (Float, Float)
    """

    # the radius of proximity, the default is a 3 mile radius
    radius_miles = 3.0
    distance = calculate_distance(pt1, pt2)
    distance_miles = degrees_to_miles(distance)

    return distance_miles < radius_miles
def calculate_distance(pt1, pt2):
    """
    goal: calculate the distance between two points
    type: (Point, Point) -> Float
    help: a point is of type (Float, Float)
    """

    (x1, y1) = pt1
    (x2, y2) = pt2

    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
def to_coordinates(point_field):
    """
    goal: convert a PointField into (Latitude, Longitude)
    type: (PointField) -> (Latitude, Longitude)
    help: the database stores coordinates as (Longitude, Latitude), which is
    not standard. This function is used to make sure everything is (Lat, Long)
    """

    (lng, lat) = point_field
    return (lat, lng)


# END proximity search
