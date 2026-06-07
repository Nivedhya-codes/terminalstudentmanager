from student import Student
from auth import User


def add_student():
    name = input("Enter name: ")
    roll_no = input("Enter roll number: ")

    physics = int(input("Enter Physics marks: "))
    maths = int(input("Enter Maths marks: "))
    chemistry = int(input("Enter Chemistry marks: "))
    computer = int(input("Enter Computer Science marks: "))
    english = int(input("Enter English marks: "))

    student = Student(name, roll_no, physics, maths, chemistry, computer, english)
    student.save_student()

    print("\nStudent added successfully!\n")


def view_marks():
    roll_no = input("Enter roll number: ")
    student = Student.search_student(roll_no)

    if student:
        print("\n--------------- MARKS ----------------")
        print(f"Physics          : {student.physics}")
        print(f"Maths            : {student.maths}")
        print(f"Chemistry        : {student.chemistry}")
        print(f"Computer Science : {student.computer}")
        print(f"English          : {student.english}")
        print("--------------------------------------\n")
    else:
        print("\nStudent not found!\n")


def view_report():
    roll_no = input("Enter roll number: ")
    student = Student.search_student(roll_no)

    if student:
        student.generate_report()
    else:
        print("\nStudent not found!\n")


def show_menu():
    print("\n==========================")
    print(" SMART STUDENT MANAGER ")
    print("==========================")
    print("1. Add Student")
    print("2. View Marks")
    print("3. View Report Card")
    print("4. Exit")


def main():

    print("\n")
    print(" ============================================= ")
    print("   ABC SCHOOL STUDENT MANAGEMENT SYSTEM")
    print(" ============================================= ")
    print("\n")
    user = User()

    # AUTH SECTION 
    while True:
        print("\n1. Register")
        print("\n2. Login")
        print("\n3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            user.register()

        elif choice == "2":
            if user.login():
                print("\nLogin successful!\n")
                break
            else:
                print("Try again!")

        elif choice == "3":
            exit()

        else:
            print("Invalid choice")

    # STUDENT SYSTEM 
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_marks()

        elif choice == "3":
            view_report()

        elif choice == "4":
            print("\nExiting program...")
            break

        else:
            print("\nInvalid choice!")


if __name__ == "__main__":
    main()