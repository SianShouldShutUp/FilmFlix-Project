from connect import *

def insert_record():
    try:
        tblfilms_filmID = input("Enter filmID: ")
        tblfilms_title = input("Enter film title: ")
        tblfilms_yearReleased = input("Enter release year: ")
        tblfilms_rating = input("Enter the film rating: ")
        tblfilms_duration = input("Enter the film duration: ")
        tblfilms_genre = input("Enter the genre : ")
    

        # Execute SQL insert statement
        db_cursor.execute("INSERT INTO tblfilms VALUES(?, ?, ?, ?, ?, ?)", (tblfilms_filmID, tblfilms_title, tblfilms_yearReleased, tblfilms_rating, tblfilms_duration, tblfilms_genre))
        db_con.commit() # permanently inserting a record in the database in the table
        print(f"{tblfilms_title} inserted into the films table")
    except sql.ProgrammingError as pe: # use to handle invalid sql statement
        print(f"Failed operation: {pe}")
    except sql.OperationalError as oe:
        print(f"Connection failed because: {oe}")
    except sql.Error as e:
        print(f"Error resulted in: {e}")
    finally:
        print("Operation completed")

if __name__ == "__main__":
    insert_record()