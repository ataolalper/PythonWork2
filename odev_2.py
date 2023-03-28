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
                            " "))
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

# Add Student
def addStudent():
    name = input("Enter the name of the student: ")
    surname = input("Enter the surname of the student: ")
    students.append(name + " " + surname)
    print(f"The student named {name} {surname} was added to the list succesfully.")

# Remove Student
def removeStudent():
    name = input("Enter the name of the student: ")
    surname = input("Enter the surname of the student: ")
    students.remove(name + " " + surname)
    print(f"The student named {name} {surname} has been removed from the list succesfully.")

# Multiple Student Adding
def addMultipleStudent():
    studentNumber = int(input("Enter the number of students: "))
    i = 0

    while i < studentNumber:
        name = input("Enter the name of the student: ")
        surname = input("Enter the surname of the student: ")
        students.append(name + " " + surname)
        print(f"The student named {name} {surname} was added to the list succesfully.")
        i += 1

# Multiple Student Removing
def removeMultipleStudent():
    studentNumber = int(input("Enter the number of students: "))
    i = 0

    while i < studentNumber:
        name = input("Enter the name of the student: ")
        surname = input("Enter the surname of the student: ")
        students.remove(name + " " + surname)
        print(f"The student named {name} {surname} was removed to the list succesfully.")
        i += 1

# Student List
def studentList():
    student = 0
    for student in range(len(students)):
        print(students[student])
        student = student + 1

# Find Student
def findStudentNumber():
    name = input("Please enter the name of the student whose number will be asked: ")
    surname = input("Please enter the surname of the student whose number will be asked: ")
    student = name + " " + surname
    i = 0 

    while i < len(students):
        if students[i] == student:
            print(f"The number of the student named {name} {surname} is {i}.")

        i = i + 1

# Exit
def exit():
    print("Exiting now.")

login()