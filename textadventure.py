from sys import exit
from random import randint

# This is just a base class for all other scenes.
class Scene(object):
	# This is the main entry point for each scene, it should describe the Scene and any Land Sharks/Items in it.
	def enter(self):
		print "Ooops! Something went wrong, you shouldn't see this!"
		exit(-1)

# This is the Class that controls which Scene the player is in and which ones they can go to next
class Engine(object):
	def __init__(self, sceneMap):
		self.sceneMap = sceneMap
	
	def play(self):
		currentScene = self.sceneMap.openingScene()

		while True:
			# This loop will change the scene
			print "\n------"
			nextSceneName = currentScene.enter()
			currentScene = self.sceneMap.nextScene(nextSceneName)

class Death(Scene):

	quips = [
		"You died."
		"You really suck at this. You died."
		"Loser, you died!"
	]

	# This method will choose a random Death.quip and print it to the screen
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)

class MainCorridor(Scene):

	def enter(self):
		print "Land Sharks have boarded your ship and they've taken your doughnut."
		print "\n"
		print "Your mission is to retrieve your doughnut and then get to the deck of the ship and escape in a life boat."
		print "You are running down the Main Corridor when a slimey Land Shark comes round the corner. It's blocking your path to the Armory and about to eat you."
		
		action = raw_input(">")

		if action == "run":
			print "You try to sprint past the Land Shark but it grabs you by the legs and eats your head."
			return "Death"
		if action == "fight":
			print "As you throw a punch at the formidable Land Shark it opens its mighty jaws rips you apart."
			print "\n"
			print "'Mmmmm, tastes like chicken', the Land Shark growls"
			return "Death"
		if action == "sneak":
			print "You jump into a tiny vent and crawl you way passed the Land Shark and into the Armory."
			print "You're surrouded by weapons."
			return "Armory"


class Armory(Scene):

	def enter(self):
		
		print "You make your way out of the vent and into the Armory. You do a quick scan of the room to see if there are any Land Sharks hiding but you can't see any."
		print "\n"
		print "You grab a pistol and make a dash for the door up to the deck but it's locked. Looks like theres a 4 pin code."
		doorCode = "%d%d%d%d" % (randint(1,9),randint(1,9),randint(1,9),randint(1,9))
		print doorCode
		action  = int(raw_input(">"))		
		if doorCode == action:
			print "The door swings open with a great cluck. You run up and onto the Deck of the Ship"
			return "Deck"
		else:
			return "Death"

class Deck(Scene):

	def enter(self):
		pass

class LifeBoat(Scene):

	def enter(self):
		pass

class Map(object):

	scenes = {
		"Death": Death(),
		"MainCorridor": MainCorridor(),
		"Armory": Armory(),
		"Deck": Deck(),
		"LifeBoat": LifeBoat()
	}

	def __init__(self, startScene):
		self.startScene = startScene

	def nextScene(self, sceneName):
		return Map.scenes.get(sceneName)

	def openingScene(self):
		return self.nextScene(self.startScene)

adventureMap = Map("MainCorridor")
adventureGame = Engine(adventureMap)
adventureGame.play()
