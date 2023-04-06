# sql-app

This is a simple sql app that can connect to a database and make basic queries

## Running the app

To run the app, generate an executable with the following command:

```
pyinstaller -F src/main.py
```

Alternatively, naviagte the the /src/ directory and execute the following command:

```
$ python main.py
```

The app takes several parameters:

- username
  > This is used for SQL Server Authentication
- password
  > This is used for SQL Server Authentication
- database name
  > The database you want to connect to (i.e. Master)
- user id
  > The user id of your yelp user (can use any example one from the user_yelp table)

Once you have input these parameters you will be greeted with the following options:

- 1: Login
- 2: Search Business
- 3: Search Users
- 4: Make Friend
- 5: Write Review
- q: Exit
