#!/usr/bin/env python3.10.2
# CMPT 354 ASSIGNMENT 7
# CREATED BY KAJ GRANT-MATHIASEN
# APRIL 2023

import pyodbc
import string
import random

from helpers import *
from sqlApi import *

BUSINESS_COLUMNS = ('business_id', 'name', 'address', 'city',
                    'postal_code', 'stars', 'review_count')
USER_YELP_COLUMNS = ('user_id', 'name', 'review_count', 'yelping_since',
                     'useful', 'funny', 'cool', 'fans', 'average_stars')


# Function to display the main menu terminal gui
def mainMenu():

    print("\nWelcome to the SQL navigator! Please select an option below:")
    print("---------------------------------------------------\n")
    print("1: Login")
    print("2: Search Business")
    print("3: Search Users")
    print("4: Make Friend")
    print("5: Write Review")
    print("q: Exit")

    while True:
        try:
            selection = input()
            if selection.isdigit():
                selection = int(selection)
            else:
                if selection == 'q' or selection == 'Q':
                    break
            if (1 <= int(selection) <= 5):
                break
            raise ValueError()

        except ValueError:
            print("Error: Incorrect input, please try again!\n")

    return selection


# Main entry function
def main():

    cursor = None
    login = False
    sApi = sqlApi()

    while True:
        selection = mainMenu()

        match selection:
            case 1:
                '''
                Login
                1. This function allows the user to log in the interface to have access to all other
                functionalities. The user must be remembered by the system in further operations.
                2. The user must enter a valid user ID.
                3. If the user ID is invalid, an appropriate message should be shown to the user.
                '''
                sApi.setAuthentication()
                sApi.createConnection()
                cursor = sApi.connection.cursor()
                login = True
                print('Successfully logged in!\n')

            case 2:
                if not login:
                    print('Error: Please login first before running a query!\n')
                    continue
                '''
                Search Business
                1. This function allows the user to search for businesses that satisfy certain criteria.
                2. A user should be able to set the following filters as their search criteria: minimum and
                maximum number of stars, city, and name (or a part of the name). The search is not casesensitive. It means that the search for upper or lower case must return the same results.
                3. After the search is complete, a list of search results must be shown to the user. The list
                must include the following information for each business: id, name, address, city and
                number of stars. The results must be ordered by name. The results can be shown on the
                terminal or in a GUI.
                4. If the search result is empty, an appropriate message should be shown to the user.
                '''
                queryString = "SELECT * FROM business"
                queryArgs = {}

                # Get input arguments
                print(
                    "Please enter the minimum number of stars (Leave blank for no minmum filter): ")
                minStarsArg = str(getIntInp(0, 5))
                if minStarsArg != "":
                    queryArgs["stars_min"] = minStarsArg

                print(
                    "Please enter the maximum number of stars (Leave blank for no maximum filter): ")
                maxStarsArg = str(getIntInp(0, 5))
                if maxStarsArg != "":
                    queryArgs["stars_max"] = maxStarsArg

                cityArg = input(
                    "Please enter the city name (Leave blank for no city name filter): ")
                if cityArg != "":
                    queryArgs["city"] = cityArg

                nameArg = input(
                    "Please enter the business name (Leave blank for no business name filter): ")
                if nameArg != "":
                    queryArgs["name"] = nameArg

                # Formulate query string
                if len(queryArgs) > 0:
                    queryString += " WHERE "
                    for arg in queryArgs.keys():
                        if arg == "stars_min":
                            queryString += "stars > " + queryArgs[arg]
                        elif arg == "stars_max":
                            queryString += "stars < " + queryArgs[arg]
                        else:
                            queryString += arg + " LIKE '%" + \
                                queryArgs[arg] + "%'"
                        queryString += " AND "
                    # Remove the last AND statement from the string
                    queryString = queryString[:-5]
                queryString += " ORDER BY name;"

                print('\nYour query is: ' + queryString)
                print(BUSINESS_COLUMNS)
                cursor.execute(queryString)
                dataset = cursor.fetchall()
                if len(dataset) < 1:
                    print('Your query did not return any results!')
                else:
                    for row in dataset:
                        print(row)
                print('Total number of rows returned: ' + str(len(dataset)))

            case 3:
                if not login:
                    print('Error: Please login first before running a query!\n')
                    continue
                '''
                Search Users
                5. This function allows the user to search for users that satisfy certain criteria.
                6. A user should be able to set the following filters as their search criteria: name (or a part of
                the name), useful (yes/no), funny (yes/no) and cool (yes/no). The search is not casesensitive. The user is considered useful, funny or cool if has value greater than zero for the
                corresponding attribute.
                7. After the search is complete, a list of search results must be shown to the user. The list
                must include the following information for each user: id, name, useful (yes/no), funny
                (yes/no), cool (yes/no) and the date when the user was registered at Yelp. The results must
                be ordered by name. The results can be shown on the terminal or in a GUI.
                8. If the search result is empty, an appropriate message should be shown to the user.
                '''
                queryString = "SELECT * FROM user_yelp"
                queryArgs = {}

                # Get input arguments
                nameArg = input(
                    "Please enter the user name (Leave blank for no name filter): ")
                if nameArg != "":
                    queryArgs["name"] = nameArg

                print(
                    "Filter by useful (yes/no)? (Leave blank for no useful filter): ", end='')
                usefulArg = getYesNoInp()
                if usefulArg != "":
                    queryArgs["useful"] = usefulArg

                print(
                    "Filter by funny (yes/no)? (Leave blank for no funny filter): ", end='')
                funnyArg = getYesNoInp()
                if funnyArg != "":
                    queryArgs["funny"] = funnyArg

                print(
                    "Filter by cool (yes/no)? (Leave blank for no cool filter): ", end='')
                coolArg = getYesNoInp()
                if coolArg != "":
                    queryArgs["cool"] = coolArg

                # Formulate query string
                if len(queryArgs) > 0:
                    queryString += " WHERE "
                    for arg in queryArgs.keys():
                        if arg == "name":
                            queryString += arg + " LIKE '%" + \
                                queryArgs[arg] + "%'"
                        else:
                            if queryArgs[arg] == True:
                                queryString += arg + " > 1"
                            elif queryArgs[arg] == False:
                                queryString += arg + " < 1"
                        queryString += " AND "
                    # Remove the last AND statement from the string
                    queryString = queryString[:-5]
                queryString += " ORDER BY name;"

                print('\nYour query is: ' + queryString)
                print(USER_YELP_COLUMNS)
                cursor.execute(queryString)
                dataset = cursor.fetchall()
                if len(dataset) < 1:
                    print('Your query did not return any results!')
                else:
                    for row in dataset:
                        print(row)
                print('Total number of rows returned: ' + str(len(dataset)))

            case 4:
                if not login:
                    print('Error: Please login first before running a query!\n')
                    continue
                '''Make Friend
                1. A user must be able to select another user from the results of the function Search Users and
                create a friendship. This can be done by entering the user's ID in a terminal or by clicking
                on a user in a GUI. The selected user will be a friend of the user that is logged in the
                interface.
                2. The friendship should be recorded in the Friendship table.
                '''
                queryString = "INSERT INTO friendship (user_id, friend) VALUES "

                # Get input arguments
                while True:
                    try:
                        nameArg = input(
                            "Please enter the user id of the user you would like to add as a friend: ")
                        if nameArg != "":
                            break
                        raise ValueError()

                    except ValueError:
                        print("Error: Incorrect input, please try again!\n")

                queryString += "('" + sApi.userId + "', '" + nameArg + "');"
                try:
                    cursor.execute(queryString)
                    cursor.commit()
                    cursor.execute(
                        "SELECT * FROM friendship WHERE user_id ='" + sApi.userId + "';")
                    rows = cursor.fetchall()
                    print('Your friends are now: ')
                    for row in rows:
                        print(row)

                except pyodbc.IntegrityError:
                    print(
                        "Error: User not found in database or is already your friend!")

            case 5:
                if not login:
                    print('Error: Please login first before running a query!\n')
                    continue
                '''
                Write Review
                1. A user should be able to write a review of a business.
                2. To write a review, a user must enter the business's ID in a terminal or by clicking on a
                business in a GUI in Search Business.
                3. The user must provide the number of stars (integer between 1 and 5).
                4. The review should be recorded in the Review table. Consider the ID of the logged user and
                the current date.
                5. The program should update the number of stars and the count of reviews for the business.
                You need to make sure that the triggers you implemented in assignment 4 are working
                properly with your application program.
                '''
                queryString = "INSERT INTO review (review_id, user_id, business_id, stars) VALUES "

                # Get input arguments
                while True:
                    try:
                        busId = input(
                            "Please enter the business id of the buisness you would like to review: ")
                        if busId != "":
                            break
                        raise ValueError()

                    except ValueError:
                        print("Error: Incorrect input, please try again!\n")

                while True:
                    try:
                        print("Please enter the number of stars: ", end='')
                        starsArg = str(getIntInp(0, 5))
                        if starsArg != "":
                            break
                        raise ValueError()

                    except ValueError:
                        print(
                            "Error: Stars must be non-null, please try again!\n")

                cursor.execute("SELECT review_id FROM review;")
                rows = cursor.fetchall()

                while True:
                    try:
                        newId = rndString(22)
                        for i in range(len(rows)):
                            if newId == rows[i][0]:
                                raise ValueError
                        break
                    except ValueError:
                        pass

                queryString += "('" + newId + "', '" + sApi.userId + \
                    "', '" + busId + "', '" + starsArg + "');"
                try:
                    cursor.execute(queryString)
                    cursor.commit()
                    print('Success! Review has been submitted.')
                except pyodbc.IntegrityError:
                    print("Error: Business not found!")

            case 'q':
                print('Exiting...')
                sApi.closeConnection()
                raise SystemExit


if __name__ == "__main__":
    main()
