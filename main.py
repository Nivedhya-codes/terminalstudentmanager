from student import Student
from auth import User


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
    print("1. View Marks")
    print("2. View Report Card")
    print("3. Exit")


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
            view_marks()

        elif choice == "2":
            view_report()

        elif choice == "3":
            print("\nExiting program...")
            break

        else:
            print("\nInvalid choice!")


if __name__ == "__main__":
    main()