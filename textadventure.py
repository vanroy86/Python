from random import randint

# Rooms
livingRoom = ("Living Room", "You are standing next the the fire in the Living Room.")
kitchen = ("Kitchen", "You walk into the Kitchen.")
bathRoom = ("Bathroom", "There is blood on the floor, it\'s still wet.")
hallway = ("Hallway", "You are in the Hallway.")


# Movement
movement = {
	livingRoom: (kitchen, hallway),
	bathRoom: (hallway, ),
	kitchen: (livingRoom, ),
	hallway: (livingRoom, kitchen, bathRoom)
	
}

currentLocation = livingRoom

# Variables
#inventory is where we will store the items the player picks up
inventory = {"Gold":2, "Sword": 18}

# Drops
staff = {
"damage": 15
}

sword = {
"damage": 18
}

# Enemies
orc = {
"name": "Orc",
"attack": 15,
"defence": 5
}

spider = {
"name": "Spider",
"attack": 5,
"defence": 2
}

zombie = {
"name": "Zombie",
"attack": 7,
"defence": 2
}

dwarf = {
"name": "Dwarf",
"attack": 9,
"defence": 5
}

# Create a list of enemies to choose random ones when rooms are made
# Don't forget to add new enemies to this list!
enemies = [orc,spider,zombie,dwarf]
drops = [staff,sword]

# Create a list of drops to choose random ones when rooms are made

def exitGame():
    exit(0)

def pickUpItem(itemToPickUp):
	pass

def randomEnemy():
	randomint = randint(0,len(enemies) - 1)
	print "You see an enemy",",", "it has:"
	return enemies[randomint]

def printDict(dict_to_print):
	for i in dict_to_print.items():
		print dict_to_print[i][i]
	print "\n"

def printInventory():
	print "\t In you Inventory you have: "
	for x, y in inventory.items():
		print ('{} : {}'.format(x,y) )
	whatNext()

print "\t *****"
print "Welcome to a Text Adventrue"
print "\t *****"

# Game loop
#Don't remove user input, it'll cause an infinite loop
while True:
	print "\n" + currentLocation[1]
	print "You can go to: "

	for (i,t) in enumerate(movement[currentLocation]):
		print i + 1, t[0]

	choice = int(raw_input("\nMake a choice: "))
	currentLocation = movement[currentLocation][choice - 1]
