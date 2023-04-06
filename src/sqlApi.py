# sqlApi.py
# Contains the custom sql api class

import pyodbc

SERVER_ADDRESS = "cypress.csil.sfu.ca"


# Main api class
class sqlApi:
    username = None
    userId = None
    password = None
    connection = None
    database = None
    server = SERVER_ADDRESS

    # Set Authentication parameters
    def setAuthentication(self):
        self.username = input(
            "Please enter your username (for database access): ")
        self.password = input(
            "Please enter your password (for database access): ")
        self.database = input(
            "Please enter your database name (for database access): ")

    # Verify that the user_id provided is within the database
    def verifyUserId(self):
        cursor = self.connection.cursor()
        while True:
            self.userId = input("Please enter your user ID (for yelp login): ")
            cursor.execute(
                "SELECT * FROM user_yelp WHERE user_id='" + self.userId + "';")
            rows = cursor.fetchall()
            if len(rows) < 1:
                print("Error: User not found in database")
            else:
                break

    # Create the main connection to the database
    def createConnection(self):
        while True:
            try:
                self.connection = pyodbc.connect(
                    'Driver={SQL Server};'
                    'Server=' + SERVER_ADDRESS + ';'
                    'Database=' + self.database + ';'
                    'Uid=' + self.username + ';'
                    'Pwd=' + self.password)
                break
            except pyodbc.Error as E:
                print(
                    "Error: Incorrect connection parameters, please try again")
                print(E)
                self.setAuthentication()

        self.verifyUserId()

    # Close the connection
    def closeConnection(self):
        try:
            self.connection.close()
        except:
            print('No connection was made!')
