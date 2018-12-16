
"""
I designed the search engine to be modular and extendable with new requirements.
You can add validation functions and behavior functions at any time.

The way the search engine works is simple. In the initialization phase it
receives a query and queryset representing all properties in the database.
In the start phase, it validates the query and assigns it the best behavior.
Finally, the search engine runs the behavior and returns a filtered queryset.

If you want to start working on this I would suggest understanding the
SearchEngine.start() function to see the underlying pattern. After that, add
a validation function and an associated behavior. Validation functions should
have the form "is_name()" to let the reader know it returns a boolean. Behavior
functions should have the form "search_name()" to let the reader know it
returns a filtered queryset.

As of now, the search engine focuses only on search_proximity() because it is
so useful. The previous implementation just ran an sql query on the breazehome 
database. I left the previous functions for future developers in case they
want to add query behavior to the database. 
"""


# classes
class SearchEngine:
    def __init__(self, query, queryset):
        """
        goal: setup the SearchEngine object
        type: (Self, String, QuerySet) -> ()
        """

        self.query = query.strip()
        self.queryset = queryset
    def start(self):
        """
        goal: use query to filter the queryset
        type: (Self) -> QuerySet
        """

        if is_query(self.query):
            return search_proximity(self.query, self.queryset)
        else:
            return queryset.none()


# validation functions
def is_query(query):
    """
    goal: make sure a query is valid, i.e not whitespace and all chars printable
    type: (String) -> Bool
    """

    if not query.isspace() and query.isprintable():
        return True
    else:
        return False


# search functions
def search_proximity(query, queryset):
    """
    goal: assign a coordinate to a query and use that to find nearby properties
    type: (String, QuerySet) -> QuerySet
    """

    from admins.models import Configuration
    from real_estate.location import in_proximity, to_coordinates
    from real_estate.google import MapsAPI

    api_key  = Configuration.objects.get(pk=1).google_api_key
    maps_api = MapsAPI(api_key)

    try:
        # returns tuple representing (latitude, longitude) of destination
        destination = maps_api.get_coordinates(query)
    except RuntimeError as e:
        print(e)
        return queryset.none()

    property_points = queryset.values_list('id', 'location_point')
    proximity_ids = (e[0] for e in property_points if in_proximity(destination, to_coordinates(e[1])))
    return queryset.filter(id__in=proximity_ids)
       

# previous implementation
def is_address(query):
    """
    goal: determine if a query is an address
    type: (String) -> Bool
    """

    if not query.isspace() and query.isprintable():
        return True
    else:
        return False
def is_zipcode(query):
    """
    goal: determine if a query is a zipcode
    type: (String) -> Bool
    """

    if query.isnumeric() and len(query) == 5:
        return True
    else:
        return False
def search_address(query, queryset):
    """
    goal: filter out properties that match the query address 
    type: (String, QuerySet) -> QuerySet
    """

    return queryset.filter(address_internet_display__icontains=query)
def search_zipcode(query, queryset):
    """
    goal: filter out properties that match the query zipcode
    type: (String, QuerySet) -> QuerySet
    """

    return queryset.filter(postal_code=query)


# END search engine
