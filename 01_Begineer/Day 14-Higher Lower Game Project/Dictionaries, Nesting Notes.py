#                                           Dictionaries, Nesting NOTES
capitals = {
    'France': 'Paris',
    'Germany': 'Berlin',
}


# Nesting a list in Dictionary
travel_log = {
    'France': ['Paris', 'Lille', 'Dijon'],
    'Germany': ['Berlin', 'Hamburg',  'Stuttgart'],
}

# Nesting a Dictionary in a Dictionary

travel_log1 = {
    'France': {"cities_visited": ['Paris', 'Lille', 'Dijon'], "total_visits": 12},
    'Germany': {"cities_visited": ['Berlin', 'Hamburg',  'Stuttgart'], "total_visits": 6},
}

# Nesting Dictionary in a List
travel_log3 = [
    {
        "country": 'France',
        "cities_visited": ['Paris', 'Lille', 'Dijon'],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ['Berlin', 'Hamburg',  'Stuttgart'],
        "total_visits": 6
    },
]

# ********************************************************************
#                                                   Function Return Value


def format_name(f_name, l_name):
    """Takes a first and last name and formats it
    to return a title case version of the name"""
    if f_name == '' and l_name == '':
        return  "You provided invalid output"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name}, {formatted_l_name}"


formatted_string = format_name("ANGELA", "YU")
print(formatted_string)

