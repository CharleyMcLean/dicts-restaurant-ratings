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

        tuple_list = restaurants_dict.items()
        sorted_tuple_list = sorted(tuple_list)

        # if user_choice == "3":
        #     break


        while True:
            user_choice = raw_input("To see restaurants and their ratings, press 1.  To add a new restaurant, press 2.  To quit, press 3.")
            if user_choice == "1":
                print sorted_tuple_list
            elif user_choice == "2":
                new_restaurant = raw_input("Please enter a new restaurant: ")
                new_rating = raw_input("Please enter that restaurant's rating: ")
                restaurants_dict[new_restaurant] = new_rating
                tuple_list = restaurants_dict.items()
                sorted_tuple_list = sorted(tuple_list)
                print sorted_tuple_list
            elif user_choice == "3":
                break
        

rate_restaurants(file_name)

    

