import time
from person import Person
from abc import ABC, abstractmethod


class Report(ABC):

    @abstractmethod
    def generate_report(self):
        pass


# Decorator
def log_report(func):
    def wrapper(*args, **kwargs):
        print("\nGenerating Report...")
        time.sleep(1)
        result = func(*args, **kwargs)
        print("\nReport generated successfully\n")
        return result
    return wrapper


class Student(Person, Report):

    def __init__(self, name, rollno, physics, maths, chemistry, computer, english):
        super().__init__(name)

        self.rollno = rollno
        self.physics = physics
        self.maths = maths
        self.chemistry = chemistry
        self.computer = computer
        self.english = english

    def total_marks(self):
        return (
            self.physics +
            self.maths +
            self.chemistry +
            self.computer +
            self.english
        )

    def calc_avg(self):
        return self.total_marks() / 5

    def grade(self):
        avg = self.calc_avg()

        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 65:
            return "C"
        else:
            return "Fail. Try Again!"

    @log_report
    def generate_report(self):

        print("=" * 40)
        print("          STUDENT REPORT CARD")
        print("=" * 40)

        print(f"Name      : {self.name}")
        print(f"Roll No   : {self.rollno}")

        print("\nMARKS")
        print("-" * 40)
        print(f"Physics          : {self.physics}")
        print(f"Maths            : {self.maths}")
        print(f"Chemistry        : {self.chemistry}")
        print(f"Computer Science : {self.computer}")
        print(f"English          : {self.english}")
        print("-" * 40)

        print(f"Total Marks : {self.total_marks()}")
        print(f"Average     : {self.calc_avg():.2f}")
        print(f"Grade       : {self.grade()}")

    def save_student(self):

        with open("student.txt", "a") as f:
            f.write(
                f"{self.rollno},{self.name},{self.physics},"
                f"{self.maths},{self.chemistry},"
                f"{self.computer},{self.english}\n"
            )

    @staticmethod
    def search_student(roll_no):
        try:
            with open("student.txt", "r") as f:

                for line in f:
                    data = line.strip().split(",")

                    if data[0] == str(roll_no):
                        return Student(
                            data[1],          # name
                            data[0],          # rollno
                            int(data[2]),     # physics
                            int(data[3]),     # maths
                            int(data[4]),     # chemistry
                            int(data[5]),     # computer
                            int(data[6])      # english
                        )

        except FileNotFoundError:
            return None

        return None