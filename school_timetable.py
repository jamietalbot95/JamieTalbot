import csv
import datetime
from tabulate import tabulate


def school_timetable_main():
    close_app = False
    while not close_app:
        print("\nWelcome to the school timetable application. From this application you can view your timetable and "
              "accept\nany changes that your teachers may have made. Type 'help' if you are unsure what to do at any"
              " time or 'quit' to go back to the main menu.")
        # Dealing with user input and catching any help/quit inputs
        while True:
            first_name = input("\nWhat is your first name?").lower().strip(" ")
            if first_name == "help":
                student_help("entering_first_name")
                first_name = ""
                continue
            elif first_name == "quit":
                close_app = True
                break
            surname = input("\nWhat is your surname?").lower().strip(" ")
            if surname == "help":
                student_help("entering_surname")
                surname = ""
                continue
            elif surname == "quit":
                close_app = True
                break
            required_day = input("\nWhich date would you like to view? Use the format DD/MM/YYYY.\n"
                                 "For example the 1st of January 2020 would be: 01/01/2020: ").strip(" ")
            if required_day == "help":
                student_help("entering_required_date")
                required_day = ""
                continue
            elif required_day == "quit":
                close_app = True
                break
            break
        if close_app:
            break
        # Begin to collect the student timetable
        student_timetable = fetch_time_table(first_name,surname,required_day)
        if student_timetable not in ["date not found","student file not found"]:
            format_timetable(student_timetable)
            if check_timetable_changes(student_timetable):
                changes_acknowledged = False
                while not changes_acknowledged:
                    print("\nYour teacher has changed this timetable since you last viewed it.")
                    while True:
                        student_acknowledge_changes = input("\nPlease enter 'yes' to let your teacher know that you "
                                                            "have viewed the latest version of your timetable: ").lower().strip(" ")
                        if student_acknowledge_changes == "yes":
                            print("\nThank you for accepting the changes to your timetable.")
                            changes_acknowledged = True
                            update_last_viewed(first_name,surname,required_day)
                            break
                        elif student_acknowledge_changes == "help":
                            student_help("acknowledge_changes")
                        else:
                            print("Please accept the changes made to the timetable by typing 'yes'. "
                                  "If you are stuck you can type 'help'. ")
        elif student_timetable == "date not found":
            print("\nNo timetable found for the date required. Please check you typed the date you need correctly.\n"
                  "If you are sure the date is correct, you can ask your teacher to upload the timetable you need.")
        elif student_timetable == "student file not found":
            print("\nWe could not find a timetable for the name you entered. Please check you typed the name "
                  "correctly.\nIf you are sure the name is correct, you can ask your teacher to create a student "
                  "file for you.")


def fetch_time_table(first_name, surname, date):
    full_name = 'student_data\\' + first_name + "." + surname + "." + "timetable.txt"
    student_timetable = ""
    try:
        with open(full_name) as student_file:
            csv_reader = csv.reader(student_file, delimiter=',')
            for rows in csv_reader:
                if date in rows:
                    student_timetable = rows
            if student_timetable == "":
                student_timetable = "date not found"
    except FileNotFoundError:
        student_timetable = "student file not found"
    return student_timetable


def format_timetable(timetable):
    data = [["Date:",timetable[2]],["Period One:",timetable[3]],["Period Two:",timetable[4]],["Period Three:",timetable[5]],["Period Four:",timetable[6]]]
    print("\n",tabulate(data, tablefmt = "plain",stralign="right"))


def check_timetable_changes(timetable):
    last_viewed = timetable[7]
    last_updated = timetable[8]
    return last_viewed < last_updated


# Changes the last viewed date in the selected timetable to the current date, which will stop the notification of
# teacher changes being made every time the timetable is viewed.
def update_last_viewed(first_name, surname, date):
    now = datetime.datetime.now()
    new_date = now.strftime("%d/%m/%Y %H:%M")
    contents = []
    full_name = 'student_data\\' + first_name + "." + surname + "." + "timetable.txt"
    with open(full_name, mode="r") as student_file:
        csv_reader = csv.reader(student_file, delimiter=',')
        for lines in csv_reader:
            contents.append(lines)
        for i in range(0,len(contents)):
            if date in contents[i]:
                old_line = contents[i]
                old_line[7] = new_date
                contents[i] = old_line
    with open(full_name, mode="w") as student_file:
        content_writer = csv.writer(student_file, delimiter=',',lineterminator='\n')
        content_writer.writerows(contents)


def student_help(section):
    if section == "entering_first_name":
        print("The program requires you to input your first name by typing after the question mark. Press enter once"
              " you have finished.")
    elif section == "entering_surname":
        print("The program requires you to input your surname by typing after the question mark. Press enter once"
              " you have finished.")
    elif section == "entering_required_date":
        print("The program requires you to input the date of the timetable you would like to view. For example if you"
              " wanted to view\na timetable for the 1st of January 2020 you would type 01/01/2020 and then press enter.")
    elif section == "acknowledge_changes":
        print("To continue you must accept the new version of your timetable by typing 'yes' followed by pressing"
              " enter")