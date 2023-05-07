class Player:
	
	def __init__(self , id, name):
		self.id = id
		self.name = name

	def setId(self, id):
		self.id = id

	def getId(self):
		return self.id

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	# I don't think so, we need getter here