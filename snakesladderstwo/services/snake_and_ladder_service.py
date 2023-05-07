from snakesladderstwo.models.board import Board
from snakesladderstwo.services.diceservice import DiceService

class SnakeAndLadderService:
	
	def __init__(self , size = 100):
		self.board = Board(size)
		self.initial_num_of_players = 0

	def setPlayers(self , players):
		# Here we can directly assign players also but I am following sequence
		self.players_queue = []
		players_current_position = {}
		for player in players:
			self.players_queue.append(player)
			players_current_position[player.getId()] = 0
		self.initial_num_of_players = len(players)
		self.board.playersCurrentPositions = players_current_position

	def setSnakes(self , snakes):
		self.board.snakesList = snakes

	def setLadders(self , ladders):
		self.board.laddersList = ladders

	def numAfterRollingTheDice(self):
		return DiceService().roll_dice()

	def hasPlayerWon(self, player):
		return self.board.playersCurrentPositions[player.getId()] == self.board.getSize()

	def is_game_completed(self):
		return self.initial_num_of_players > len(self.players_queue)

	def playerPositionAfterGoingThroughLaddersAndSnake(self, player, position):
		print("Processing position " + str(position) + " for " + player.getName())
		for snake in self.board.snakesList:
			if snake.getStart() == position:
				print("Snake alert at position " + str(position) + " moving from " + str(position) + " to " + str(snake.getEnd()))
				position = snake.getEnd()
				continue

		for ladder in self.board.laddersList:
			if ladder.getStart() == position:
				print("Ladder alert at position " + str(position) + " moving from " + str(position) + " to " + str(ladder.getEnd()))
				position = ladder.getEnd()
				continue

		return position


	def movePlayer(self, player, num_achieved_after_rolling_dice):

		# import pdb
		# pdb.set_trace()
		old_position = self.board.playersCurrentPositions[player.getId()]
		new_position = old_position + num_achieved_after_rolling_dice
		board_size = self.board.getSize()
		if new_position > board_size:
			new_position = old_position
		else:
			new_position = self.playerPositionAfterGoingThroughLaddersAndSnake(player , new_position)

		self.board.playersCurrentPositions[player.getId()] = new_position		


	def startGame(self):
		while(not self.is_game_completed()):
			player = self.players_queue.pop(0)
			num_achieved_after_rolling_dice = self.numAfterRollingTheDice()
			self.movePlayer(player , num_achieved_after_rolling_dice)
			if self.hasPlayerWon(player):
				print(player.getName() + " has won the game.")
			else:
				self.players_queue.append(player)


# can we set is_game_completed True inside hasPlayerWon?
