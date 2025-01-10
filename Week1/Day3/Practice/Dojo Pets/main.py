from ninja import Ninja
from pet import Pet


# create an instance of the Pet class to pass it to the ninja class
my_pet = Pet("Buddy", "dog", "sit")

ninja = Ninja("john", "Doe", my_pet, ["bone", "treat"], "dog food")

ninja.feed().walk().bathe()