import json

class Student:

    def __init__(self, name, roll_no, physics, maths, chemistry, computer, english):
        self.name = name
        self.roll_no = roll_no
        self.physics = physics
        self.maths = maths
        self.chemistry = chemistry
        self.computer = computer
        self.english = english

    def load_students(self):
        try:
            with open("students.json", "r") as f:
                return json.load(f)
        except:
            return []

    def save_students(self, students):
        with open("students.json", "w") as f:
            json.dump(students, f, indent=4)

    def save_student(self):
        students = self.load_students()

        students.append({
            "name": self.name,
            "roll_no": self.roll_no,
            "physics": self.physics,
            "maths": self.maths,
            "chemistry": self.chemistry,
            "computer": self.computer,
            "english": self.english
        })

        self.save_students(students)

    @staticmethod
    def search_student(roll_no):
        try:
            with open("students.json", "r") as f:
                students = json.load(f)
        except:
            return None

        for s in students:
            if s["roll_no"] == roll_no:
                return Student(
                    s["name"],
                    s["roll_no"],
                    s["physics"],
                    s["maths"],
                    s["chemistry"],
                    s["computer"],
                    s["english"]
                )

        return None

    def generate_report(self):
        total = self.physics + self.maths + self.chemistry + self.computer + self.english
        percent = total / 5
        if percent >= 90:
            grade = "A+"
        elif percent >= 80:
            grade = "A"
        elif percent >= 70:
            grade = "B+"
        elif percent >= 60:
            grade = "B"
        elif percent >= 50:
            grade = "C"
        else:
            grade = "Fail"

        print("\n")
        print("====================================================")
        print("                ABC SCHOOL REPORT CARD")
        print("====================================================")
        print(f"Student Name      : {self.name}")
        print(f"Roll Number       : {self.roll_no}")
        print("----------------------------------------------------")
        print(f"Physics           : {self.physics}")
        print(f"Mathematics       : {self.maths}")
        print(f"Chemistry         : {self.chemistry}")
        print(f"Computer Science  : {self.computer}")
        print(f"English           : {self.english}")
        print("----------------------------------------------------")
        print(f"Total Marks       : {total}/500")
        print(f"Percentage        : {percent:.2f}%")
        print(f"Grade             : {grade}")
        print("====================================================")
        print("                 END OF REPORT")
        print("====================================================")
        print("\n")
