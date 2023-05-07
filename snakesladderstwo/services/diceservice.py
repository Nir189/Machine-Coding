import random

class DiceService:
	
	def roll_dice(self):
		random_number = random.randint(1,6)
		return random_number