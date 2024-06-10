from connect import *
 
def update_record():
    try:
        id_field = input("Enter the filmID of the record to be updated: ")

        db_cursor.execute("SELECT * FROM tblfilms WHERE filmID = ?", (id_field,)) # select a single record based on the ID

        a_record = db_cursor.fetchone() # fetches a single record
 
        if a_record == None: # Is a singleton object use to check if a value is present/exists
            print(f"The record with id {id_field} does not exists! ")
        else:
            tblfilms_title = input("Enter film title: ")
            tblfilms_yearReleased = input("Enter release year: ")
            tblfilms_rating = input("Enter the film rating: ")
            tblfilms_duration = input("Enter the film duration: ")
            tblfilms_genre = input("Enter the genre: ")
           
            # wrap single quotes to match the value as it is in the table
            tblfilms_title = "'"+tblfilms_title+"'"
            tblfilms_yearReleased = "'"+tblfilms_yearReleased+"'"
            tblfilms_rating = "'"+tblfilms_rating+"'"
            tblfilms_duration = "'"+tblfilms_duration+"'"
            tblfilms_genre = "'"+tblfilms_genre+"'"
 
            db_cursor.execute(f"UPDATE tblfilms SET Title=?, yearReleased=?, Rating=?, Duration=?, Genre=? WHERE filmID=?", (tblfilms_title, tblfilms_yearReleased, tblfilms_rating, tblfilms_duration, tblfilms_genre,id_field))
            db_con.commit()
    except sql.ProgrammingError as pe: # Use to handle invalid SQL statement
        print(f"Failed operation: {pe}")
    finally:
        print("Operation completed")
 
if __name__ == "__main__":
    update_record()