import json
import student

class User:
    def roll_number_exists(self, roll_no):
            
            with open("students.json" , 'r') as f:
                row = json.load(f)
                for student in row:
                    if student["roll_no"] == roll_no:
                        return True
    
            return False
                
        

    def load_users(self):
        try:
            with open("users.json", "r") as f:
                return json.load(f)
        except:
            return {}

    def save_users(self, users):
        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)

    def register(self):
        self.username = input("Username: ")
        self.password = input("Password: ")

        users = self.load_users()

        if self.username in users:
            print("User already exists!")
            return

        users[self.username] = self.password
        self.save_users(users)

        print("Registration successful!")

        roll_no = input("Enter roll number: ")
        if not self.roll_number_exists(roll_no):
            print("Invalid roll number")
            return

    def login(self):
        self.username = input("Username: ")
        self.password = input("Password: ")

        users = self.load_users()

        if users.get(self.username) == self.password:
            return True

        return False