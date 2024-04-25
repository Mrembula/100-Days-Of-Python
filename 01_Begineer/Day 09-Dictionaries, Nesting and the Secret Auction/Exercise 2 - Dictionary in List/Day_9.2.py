travel_log = [
    {
        "country": "France",
        "cities_visited": ['Paris', 'Lille', 'Dijon'],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ['Berlin', 'Hamburg',  'Stuttgart'],
        "total_visits": 6
    },
]


def add_new_country(country_visit, times_visit, cities):
    travel_log.append({"country": country_visit,
                       "cities_visited": cities,
                       "total_visits": times_visit})


def add_new_county2(country_visit, times_visit, cities_visited):
    new_country = {}
    new_country["county"] = country_visit
    new_country["visits"] = times_visit
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia",2,['Moscow', 'Saint Petersburg'], )
print(travel_log)