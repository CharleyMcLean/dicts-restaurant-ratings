# your code goes here

import sys

file_name = sys.argv[1]

def rate_restaurants(file_name):
    """
    Takes restaurants and ratings, and returns them alphabetized.
    """
    with open(file_name) as restaurant_scores:

        restaurants_dict = {}
        for line in restaurant_scores:
            # print line
            restaurant_info = line.strip().split(":")
            # print restaurant_info
            key = restaurant_info[0]
            value = restaurant_info[1]
            restaurants_dict[key] = value

        new_restaurant = raw_input("Please enter a new restaurant: ")
        new_rating = raw_input("Please enter that restaurant's rating: ")

        restaurants_dict[new_restaurant] = new_rating

        tuple_list = restaurants_dict.items()
        sorted_tuple_list = sorted(tuple_list)
        return sorted_tuple_list

print rate_restaurants(file_name)

    

