# ------------------------------------------------------------------------------------- #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   PSheehy, 2026-03-06, Updated starter script
# ------------------------------------------------------------------------------------- #
import json
import _io

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

# Data -------------------------------------------------------------------------------- #
# TODO Create a Person Class (DONE)
class Person(object):
    """
    The Data class representing a person's data

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.

    ChangeLog: (Who, When, What)
        PSheehy, 2026-03-06, Created Class
    """
    def __init__(self, first_name: str = "", last_name: str = ""):
        # TODO Add first_name and last_name properties to the constructor (DONE)
        if first_name == "" or type(first_name) is str and first_name.isalpha():
            self.__first_name = first_name
        else:
            raise ValueError("The first name should not contain numbers.")
        if last_name == "" or type(last_name) is str and last_name.isalpha():
            self.__last_name = last_name
        else:
            raise ValueError("The last name should not contain numbers.")

    # TODO Create a getter and setter for the first_name property (DONE)
    @property
    def first_name(self):
        """
        The getter property of attribute first_name

        ChangeLog: (Who, When, What)
            PSheehy, 2026-03-06, Created the property

        :return: the first name with capitalization of the first letter
        """
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        """
        The setter property of attribute first_name.
            Will raise ValueError if a digit is used in the name.

        ChangeLog: (Who, When, What)
            PSheehy, 2026-03-06, Created the property

        :param value: the value that needs to be checked and set as
                        Class Person's first name

        :return: None
        """
        # Checks if value is empty or has no numbers
        if value == "" or type(value) is str and value.isalpha():
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    # TODO Create a getter and setter for the last_name property (DONE)
    @property
    def last_name(self):
        """
        The getter property of attribute last_name

        ChangeLog: (Who, When, What)
            PSheehy, 2026-03-06, Created the property

        :return: the last name with capitalization of the first letter
        """
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        """
        The setter property of attribute last_name.
            Will raise ValueError if a digit is used in the name.

        ChangeLog: (Who, When, What)
            PSheehy, 2026-03-06, Created the property

        :param value: the value that needs to be checked and set as
                        Class Person's last name

        :return: None
        """
        if value == "" or type(value) is str and value.isalpha():
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    # TODO Override the __str__() method to return Person data (DONE)
    def __str__(self):
        """
        Return method for Person Class object

        ChangeLog: (Who, When, What)
            PSheehy, 2026-03-06, Created Method

        :return: How Person should be printed.
        """
        return f"{self.first_name}, {self.last_name}"

# TODO Create a Student class the inherits from the Person class (DONE)
class Student(Person):
    """
    The Data class representing a students's data, inherits from the person class

    Properties:
    - Inherits from Person class
    - course_name

    ChangeLog: (Who, When, What)
        PSheehy, 2026-03-06, Created Class
    """
    # TODO call to the Person constructor and pass it the first_name and last_name data (DONE)
    def __init__(self, first_name: str = "", last_name: str = "", course_name: str = ""):
        super().__init__(first_name=first_name, last_name=last_name)

        # TODO add a assignment to the course_name property using the course_name parameter (DONE)
        if course_name == "" or type(course_name) is str:
            self.__course_name = course_name
        else:
            raise ValueError("The course name is not a recognized structure.")

    # TODO add the getter for course_name (DONE)
    @property
    def course_name(self):
        """
        The getter property of attribute course_name

        ChangeLog: (Who, When, What)
            PSheehy, 2026-03-06, Created the property

        :return: the course name with capitalization of the first letter
        """
        return self.__course_name.title()

    # TODO add the setter for course_name (DONE)
    @course_name.setter
    def course_name(self, value: str):
        """
        The setter property of attribute course_name.
            Will raise ValueError if there is a data type mismatch.

        ChangeLog: (Who, When, What)
            PSheehy, 2026-03-06, Created the property

        :param value: the value that needs to be checked and set as
                        Class Studen'ts's course name

        :return: None
        """
        if value == "" or type(value) is str:
            self.__course_name = value
        else:
            raise ValueError("The course name is not a recognized structure.")

    # TODO Override the __str__() method to return the Student data (DONE)
    def __str__(self):
        """
        Return method for Student Class object

        ChangeLog: (Who, When, What)
            PSheehy, 2026-03-06, Created Method

        :return: How Student should be printed.
        """
        return f"{self.first_name}, {self.last_name}, {self.course_name}"



# Processing -------------------------------------------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list = []):
        """ This function reads data from a json file and loads it into a list of
            Student object rows then returns the list filled with student data.

        ChangeLog: (Who, When, What)
            RRoot,1.1.2030,Created function
            PSheehy, 2026-03-06, Updated function to use new Student Class,
                and follow best practice by passing list object

        :param file_name: string data with name of file to read from
        :param student_objects: reference to the list for storage, empty by default

        :return: list
        """
        file = None

        try:
            # Get a list of dictionary rows from the data file
            file = open(file_name, "r")
            json_students = json.load(file)

            # Convert the list of dictionary rows into a list of Student objects
            #student_objects = []
            # TODO replace this line of code to convert dictionary data to Student data (DONE)
            #student_objects = json_students
            for student in json_students:
                student_object: Student = Student(first_name=student["FirstName"],
                                                 last_name=student["LastName"],
                                                 course_name=student["CourseName"])
                student_data.append(student_object)

        except Exception as e:
            IO.output_error_messages(message=\
                    "Error: There was a problem with reading the file.", error=e)

        finally:
            if file is not None and file.closed == False:
                file.close()

        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of
            Student objects

        ChangeLog: (Who, When, What)
            RRoot,1.1.2030,Created function
            PSheehy, 2026-03-06, Updated function to convert list of new Student data
                to json compatable dictionary rows

        :param file_name: string data with name of file to write to
        :param student_data: list of Student object rows to be writen to the file

        :return: None
        """
        file = None

        try:
            # TODO Add code to convert Student objects into dictionaries (DONE)
            json_students: list = []
            for student in student_data:
                student_object: dict \
                    = {"FirstName": student.first_name,
                       "LastName": student.last_name,
                       "CourseName": student.course_name}
                json_students.append(student_object)

            file = open(file_name, "w")
            json.dump(json_students, file, indent=2)

            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file is not None and file.closed == False:
                file.close()


# Presentation ------------------------------------------------------------------------ #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
            RRoot,1.1.2030,Created function
            PSheehy, 2026-03-06, Updated to display using Student Class object

        :param student_data: list of Student object rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:

            # TODO Add code to access Student object data instead of dictionary data (DONE)
            #print(f'Student {student["FirstName"]} '
            #      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
            print(student)

        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name,
            with a course name from the user

        ChangeLog: (Who, When, What)
            RRoot,1.1.2030,Created function
            PSheehy, 2026-03-06, Updated function to use Student Class object

        :param student_data: list of Student object rows to be filled with input data

        :return: list
        """
        student: Student = Student()

        try:
            #student_first_name = input("Enter the student's first name: ")
            #if not student_first_name.isalpha():
            #    raise ValueError("The last name should not contain numbers.")
            #student_last_name = input("Enter the student's last name: ")
            #if not student_last_name.isalpha():
            #    raise ValueError("The last name should not contain numbers.")
            #course_name = input("Please enter the name of the course: ")

            # TODO Replace this code to use a Student objects instead of a dictionary objects (DONE)
            #student = {"FirstName": student_first_name,
            #           "LastName": student_last_name,
            #           "CourseName": course_name}
            student.first_name = input("Enter the student's first name: ")
            student.last_name = input("Enter the student's last name: ")
            student.course_name = input("Enter the name of the registered course: ")

            student_data.append(student)

            print()
            print(f"You have registered {student.first_name} {student.last_name} for {student.course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body
#test = Person(first_name="Test",last_name="test")

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        print("Student data saved to file")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
