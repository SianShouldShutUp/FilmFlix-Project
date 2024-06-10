import logging
import time
from connect import *

logging.basicConfig(filename=r"Python/FilmFlixProject/films.log",format='[%(filename)s:%(lineno)d in function %(funcName)s located at %(pathName)s] %(message)s', datefmt='%Y-%M-%d', level=logging.DEBUG)

def read_records():
    try:
        # Select all records
        db_cursor.execute("SELECT * from tblfilms")

        # Fetchall() to fetch/get the selected records from the table
        all_records = db_cursor.fetchall()
        
        if all_records: #if record(s) exists
        #iterate and print all records
            for aRecord in all_records:
                print(aRecord)
        else:
            print("No record found in the film table")
            logging.warning(f"On{time.asctime()}")
                
    except sql.ProgrammingError as pe:
        print(f"Failed operation: {pe}")
    finally:
        print("Displayed all records")

if __name__ == "__main__":
    read_records()