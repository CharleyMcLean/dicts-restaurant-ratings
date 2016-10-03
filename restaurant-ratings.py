# your code goes here

import sys

file_name = sys.argv[1]

def rate_restaurants(file_name):
    """
    """
    with open(file_name) as restaurant_scores:

        restaurants_dict = {}
        for line in restaurant_scores:
            print line
            restaurant_info = line.strip().split(":")
            print restaurant_info
            key = restaurant_info[0]
            value = restaurant_info[1]
            restaurants_dict[key] = value
            
        tuple_list = restaurants_dict.items()
        sorted_tuple_list = sorted(tuple_list)
        return sorted_tuple_list

print rate_restaurants(file_name)