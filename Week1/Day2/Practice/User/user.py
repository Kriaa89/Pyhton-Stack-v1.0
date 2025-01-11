# define a class User
class User: 
    # constructor metghod to initialize the attribute of the class
    def __init__(self, first_name, last_name, email, age,):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member = False
        self.gold_card_points = 0
# display_info(self) - Have this method print all of the users' details on separate lines.
    def display_info(self):
        print(f" Hello, my name is {self.first_name} {self.last_name}.")
        print(f"my email is {self.email}")
        print(f"I'm {self.age} old.")
        print(f"I'm {self.age}")
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        self.gold_card_points -= amount

user=User(
    "ali","hajji","alihajji@gmail.com", 20 
)
user.display_info()
user.enroll()
user.spend_points(50)


user2 = User(
    "yessine", "Kriaa", "yessinekriaa@gmail.com", 20
)
user2.spend_points(80)
user2.display_info()
