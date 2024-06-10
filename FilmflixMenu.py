import Filmflixreadrecords, Filmflixaddrecord, Filmflixupdaterecord, Filmflixdeleterecord
import FilmflixReportAll, FilmFlixReportGenre, FilmflixReportYear, FilmflixReportRating

# Create a function to read content from the FilmflixMenu.txt file
def read_file():
    try:
        with open('Python/FilmFlixProject/FilmflixMenu.txt') as file_read:
            fr = file_read.read()
            return fr
    except FileNotFoundError as fnf:
        print(f"Error handling file because: {fnf}")

# Create a function to read content from the FilmflixReportMenu.txt file
def read_file2():
    try:
        with open('Python/FilmFlixProject/FilmflixReportMenu.txt') as file_read:
            fr = file_read.read()
            return fr
    except FileNotFoundError as fnf:
        print(f"Error handling file because: {fnf}")

# Function to display the main menu and get user's choice
def films_menu():
    option = 0  # Declare option variable and initialize with an integer data type
    options_list = ["1", "2", "3", "4", "5", "6"]  # List of valid options

    menu_choices = read_file()  # Read the main menu content from the file

    # Loop until the user selects a valid option
    while option not in options_list:
        print(menu_choices)  # Display the main menu
        option = input("Enter an option from the menu choices above ")  # Get user's choice
        if option not in options_list:
            print(f"{option} is not a valid choice! ")  # Display error message for invalid choice
    return option

# Function to display the report menu and get user's choice
def search_menu():
    option = 0  # Declare option variable and initialize with an integer data type
    options_list = ["1", "2", "3", "4", "5"]  # List of valid options

    menu_choices = read_file2()  # Read the report menu content from the file

    # Loop until the user selects a valid option
    while option not in options_list:
        print(menu_choices)  # Display the report menu
        option = input("Enter an option from the menu choices above ")  # Get user's choice
        if option not in options_list:
            print(f"{option} is not a valid choice! ")  # Display error message for invalid choice
    return option

# Function to handle the report menu
def report_menu():
    report_program = True  # Flag to control the report menu loop
    while report_program:
        report_menu = search_menu()  # Display the report menu and get user's choice
        match report_menu:
            case "1":
                FilmflixReportAll.read_records()
            case "2":
                FilmFlixReportGenre.search_report()
            case "3":
                FilmflixReportYear.search_report()
            case "4":
                FilmflixReportRating.search_report()
            case _:
                report_program = False  # Exit the report menu loop

# Main program loop
main_program = True  # Flag to control the main program loop

while main_program:
    main_menu = films_menu()  # Display the main menu and get user's choice
    match main_menu:
        case "1":
            Filmflixaddrecord.insert_record()
        case "2":
            Filmflixdeleterecord.delete_record()
        case "3":
            Filmflixupdaterecord.update_record()
        case "4":
            Filmflixreadrecords.read_records()
        case "5":
            report_menu()  # Call the report menu function
        case _:
            main_program = False  # Exit the main program loop

input("Press 'Enter' to exit the Menu/App")  # Prompt to exit the application
