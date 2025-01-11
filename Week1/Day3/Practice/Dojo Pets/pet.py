class Pet:
    def __init__(self, name, type, triks): 
        self.name = name # this is an attribute
        self.type = type # this is an attribute
        self.triks = triks # this is an attribute
        self.health = 100 # this is an attribute and the value is 100 this why we don't need to pass it the init method because it is always the same 
        self.energy = 100 
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(f"{self.name} sleepy and energy is {self.energy}") # test the sleep method  
        return self
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} is eating and he is energy is {self.energy} and health is {self.health}") # test the eat method 
        return self
# play() - increases the pet's health by 5 
    def play(self):
        self.health +=5
        print(f"{self.name} is playing and his health is {self.health}") # test the play method
        return self
    def noise(self):
        print(f"{self.name} is making noise")
        return self