students = []

# Login Screen
def login():
    key = "keep"
    while key == "keep":
        options = int(input(" "
                            "\nEnter 1 for add a student."
                            "\nEnter 2 for remove a student."
                            "\nEnter 3 for add more than one student."
                            "\nEnter 4 for remove more than one student."
                            "\nEnter 5 to access student list."
                            "\nEnter 6 for get the number of student."
                            "\nEnter 7 for exit."
                            "\n"
                            "\n"))
        if options == 7:
            exit()
            key = "exit"
        elif options == 1:
            addStudent()
        elif options == 2:
            removeStudent()
        elif options == 3:
            addMultipleStudent()
        elif options == 4:
            removeMultipleStudent()
        elif options == 5:
            studentList()
        elif options == 6:
            findStudentNumber()
        else:
            print("Undefined action. Please try again.")

# Blank
def blank():
    print(" ")

# Add Student
def addStudent():
    blank()
    name = input("Enter the name of the student: ")
    blank()
    surname = input("Enter the surname of the student: ")
    students.append(name + " " + surname)
    blank()
    print(f"The student named {name} {surname} was added to the list succesfully.")

# Remove Student
def removeStudent():
    blank()
    name = input("Enter the name of the student: ")
    blank()
    surname = input("Enter the surname of the student: ")
    students.remove(name + " " + surname)
    blank()
    print(f"The student named {name} {surname} has been removed from the list succesfully.")

# Multiple Student Adding
def addMultipleStudent():
    blank()
    studentNumber = int(input("Enter the number of students: "))
    i = 0

    while i < studentNumber:
        blank()
        name = input("Enter the name of the student: ")
        blank()
        surname = input("Enter the surname of the student: ")
        students.append(name + " " + surname)
        blank()
        print(f"The student named {name} {surname} was added to the list succesfully.")
        i += 1

# Multiple Student Removing
def removeMultipleStudent():
    blank()
    studentNumber = int(input("Enter the number of students: "))
    i = 0

    while i < studentNumber:
        blank()
        name = input("Enter the name of the student: ")
        blank()
        surname = input("Enter the surname of the student: ")
        students.remove(name + " " + surname)
        blank()
        print(f"The student named {name} {surname} was removed to the list succesfully.")
        i += 1

# Student List
def studentList():
    student = 0
    for student in range(len(students)):
        blank()
        print(students[student])
        student = student + 1

# Find Student
def findStudentNumber():
    blank()
    name = input("Please enter the name of the student whose number will be asked: ")
    blank()
    surname = input("Please enter the surname of the student whose number will be asked: ")
    student = name + " " + surname
    i = 0 

    while i < len(students):
        if students[i] == student:
            blank()
            print(f"The number of the student named {name} {surname} is {i}.")

        i = i + 1

# Exit
def exit():
    blank()
    print("Exiting now.")

login()