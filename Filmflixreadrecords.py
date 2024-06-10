

from connect import *
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
            print("No record found in the songs table")
                
    except sql.ProgrammingError as pe: # use to handle invalid sql statement
        print(f"Failed operation: {pe}")
    finally:
        print("Displayed all records")

if __name__ == "__main__":
    read_records()