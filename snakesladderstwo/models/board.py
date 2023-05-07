class Board:
	def __init__(self, size):
		self.size = size
		self.snakesList = []
		self.laddersList = []
		self.playersCurrentPositions = {}

	def setSize(self, size):
		self.size = size

	def getSize(self):
		return self.size

	def setSnakesList(self, snakesList):
		self.snakesList = snakesList

	def getSnakesList(self):
		return self.snakesList

	def setLaddersList(self, laddersList):
		self.laddersList = laddersList

	def getLaddersList(self):
		return self.laddersList

	def setPlayerCurrentPosition(self, playersCurrentPositions):
		self.playersCurrentPositions = playersCurrentPositions

	def getPlayerCurrentPosition(self):
		return self.playersCurrentPositions