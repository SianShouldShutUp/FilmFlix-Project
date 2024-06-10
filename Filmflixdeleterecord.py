from connect import *
 
def delete_record():
 
    try:
        id_field = input("Enter the filmID of the record to be deleted: ")
 
        db_cursor.execute("SELECT * FROM tblfilms WHERE filmID = ?", (id_field,))

        a_record = db_cursor.fetchone()
 
        if a_record == None: # Is a singleton object use to check if a value is present/exists
            print(f"The record with id {id_field} does not exists! ")
        else:
            db_cursor.execute("DELETE FROM tblfilms WHERE filmID=?",(id_field,))
            db_con.commit()
            print(f"Record {id_field} deleted from FilmFlix! ")
    except sql.ProgrammingError as pe: # Use to handle invalid SQL statement
        print(f"Failed operation: {pe}")
    finally:
        print("Operation completed")
if __name__ == "__main__":
    delete_record()