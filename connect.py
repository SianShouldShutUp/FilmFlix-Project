import sqlite3 as sql # import the sqlite3 module and alised it as 'sq'

try:
    # to use the sqlite3 module we start by creating a database connection object (variable to hold the folder path with the filename)
    with sql.connect('Python/FilmFlixProject/filmflix.db') as db_con:
        # we create a cursor object (a variable) and bind it to the cursor() method from the sqlite module
        db_cursor = db_con.cursor() # use execute sql statements
except sql.OperationalError as oe: #raise a sql error as
    # handle the exception/error
    print(f"Connection failed because: {oe}")