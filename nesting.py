#dictionary nesting
#dictionarie are accessed by keys
travel_log = {
    "France" : {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

#list nesting
#lists are accessed by index

#nesting a dictionary in a list
travel_log = [
   { "country": "France", 
    "cities_visited" : ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
    },
    {"country": "Germany", 
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
     "total_visits": 5
     }
]
