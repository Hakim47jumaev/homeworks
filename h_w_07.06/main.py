class Person:
    def __init__(self,name,surname,birthday,adrees,country,city,region,profession,gender) :
        self.name=name
        self.surname=surname
        self.birthday=birthday
        self.adress=adrees
        self.country=country
        self.city=city
        self.region=region
        self.profession=profession
        self.gender=gender
    def get_info(self):
        return f"{self.name} {self.surname} ,{self.birthday} ,{self.adress} ,{self.country} ,{self.city} ,{self.region} ,{self.profession} ,{self.gender}"


class User(Person):
    def __init__(self, name, surname, birthday, adrees, country, city, region, profession, gender,username,password1,password2):
        super().__init__(name, surname, birthday, adrees, country, city, region, profession, gender)
        self.username=username
        self.password1=password1
        self.password2=password2
    def __str__(self) :
                return f"{self.name} {self.surname} ,{self.birthday} ,{self.adress} ,{self.country} ,{self.city} ,{self.region} ,{self.profession} ,{self.gender}"

user_list=[] 
class UserManager:
    def sign_up(self):
        new_user=User(input("enter name --> "),input("enter surname --> "),input("enter birthday --> "),
                      input("enter adress --> "),input("enter country --> "),
                      input("enter city --> "),input("enter region --> "),input("enter profession --> "),
                      input("enter gender --> "),input("enter username --> "),
                      input("enter password1 --> "),input("enter password2 --> "))
        with open("users.txt", "a") as file:
            file.write(f"{new_user.name} {new_user.surname} {new_user.birthday} {new_user.adress} {new_user.country} {new_user.city} {new_user.region} {new_user.profession} {new_user.gender} {new_user.username} {new_user.password1} {new_user.password2} \n" )
        user_list.append(new_user)
    def   get_users(self):
        with open("users.txt", "r") as file:
            line = file.readlines()
            for i in line:
                
                print(i,end="")
                print("-"*50)
    def login(self, username, password):
        with open(self.users.txt, "r") as file:
            users = file.readlines()
            for user in users:
                saved_username, saved_password = user.strip().split(",")
                if saved_username == username and saved_password == password:
                    print("You have successfully entered the system.")
                    return True
            print("Username or password is incorrect.")
            return False
                    
                

   
         

               
         
ob1=UserManager()
while True:
     print(f"""
   1.Registration
   2.Login
   3.Users
    4.exit
""")
     choise=input("enter your choise --> ")
     print()
     match choise:
        case "1":
               ob1.sign_up()
        case "2":
               ob1.login(input("enter username --> "),input("enter password --> "))
               print("-"*20)
        case "3":
               ob1.get_users()
        case "4":
               break
        case _:
               print("error ")