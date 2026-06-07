class User:
    def __init__(self, username="", password=""):
        self.username = username
        self.password = password

    def username_exists(self):
        try:
            with open("Users.txt" ,"r") as f:
                for line in f:
                    username, _ =line.strip().split(",",1)

                    if username == self.username:
                        return True

            return False
        
        except FileNotFoundError:
            return False

    
    def save_user(self):
        
        with open("Users.txt" ,'a') as f:
            f.write(f"{self.username},{self.password}\n")
            
    
        

    def register(self):
        
        print("\n=== User Registration ===")
        self.username = input("Username: ")
        
        if self.username_exists():
            print("Username already exists.")
            return
        
        while True:
            
            self.password = input("Password: ")
            if len(self.password) < 8:
                print("Password must be at least 8 characters long.")
            elif not any(char.islower() for char in self.password):
                print("Password must contain at least one lowercase letter.")

            elif not any(char.isupper() for char in self.password):
                print("Password must contain at least one uppercase letter.")

            elif not any(char.isdigit() for char in self.password):
                print("Password must contain at least one number.")

            elif not any(not char.isalnum() for char in self.password):
                print("Password must contain at least one special character.")

            else:
                print("Password accepted.")
                break


        self.save_user()
        print("Registration successful.")

    def login(self):
        print("\n=== User Login ===")

        self.username = input("Username: ")
        self.password = input("Password: ")

        try:
            with open("Users.txt", "r") as f:
                for line in f:
                    file_username, file_password = line.strip().split(",", 1)

                    if file_username == self.username and file_password == self.password:
                        print("Login successful.")
                        return True

            print("Invalid username or password.")
            return False

        except FileNotFoundError:
            print("No users found. Please register first.")
            return False
    
            
