import logging
import time
from connect import *

logging.basicConfig(filename=r"Python/FilmFlixProject/films.log",format='[%(filename)s:%(lineno)d in function %(funcName)s located at %(pathName)s] %(message)s', datefmt='%Y-%M-%d', level=logging.DEBUG)

def search_report():
    try:
        id_field = input("What genre would you like to search for? ")

        db_cursor.execute("SELECT * FROM tblfilms WHERE genre = ?", (id_field,))
        a_record = db_cursor.fetchall()
        if a_record == None:
            print(f"A record with genre {id_field} does not exists in the film table!")
            logging.warning(f"On{time.asctime()}")
        else:
                print(a_record)
    except sql.ProgrammingError as pe: # Use to handle invalid SQL statement
        print(f"Failed operation: {pe}")
    finally:
        print("Operation completed")
if __name__ == "__main__":
    search_report()