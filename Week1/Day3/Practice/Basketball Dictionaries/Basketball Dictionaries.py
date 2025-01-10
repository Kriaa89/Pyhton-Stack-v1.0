# Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["teame"]

kevin = {
        "name": "Kevin Durant",
        "age":34, 
        "position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
#Create instances using individual player dictionaries.
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)


players = [
    {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"},
    {"name": "Jason Tatum", "age":44, "position": "small forward", "team": "Boston Celtics"},
    {"name": "Kyrie Irving", "age":26, "position": "small forward", "team": "Brooklyn Nets"},
    {"name": "Kevin Durant", "age":31, "position": "small forward", "team": "Brooklyn Nets"},
    {"name": "Kevin Durant", "age":32, "position": "small forward", "team": "Brooklyn Nets"}
]
new_team = [] # we decalare a varibale to store the new team inside it 
# we create this for loop to iterate over the players list and create a new instance of the PLayer class for each player in the list
# the loop takes the data of each player and passe it to the Player class 
for data in players:
    new_team.append(Player(data)) # in this line we append the new instance of the Player class to the new_team [] list

