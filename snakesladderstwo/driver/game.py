import sys
sys.path.insert(0,'/home/isha/Documents/A/P/R/CodingPractice26Jan/CodingPractice/system_design/Machine-Coding/snakesandladders-master')
from snakesladderstwo.services.snake_and_ladder_service import SnakeAndLadderService
from snakesladderstwo.models.player import Player
from snakesladderstwo.models.snake import Snake
from snakesladderstwo.models.ladder import Ladder

#snakes
snakes = []
snakes.append(Snake(99,10))
snakes.append(Snake(84,65))
snakes.append(Snake(75,35))
snakes.append(Snake(66,23))
snakes.append(Snake(24,12))
snakes.append(Snake(18,3))
#ladders
ladders = []
ladders.append(Ladder(7,21))
ladders.append(Ladder(19,89))
ladders.append(Ladder(27,83))
ladders.append(Ladder(31,78))
ladders.append(Ladder(47,68))
ladders.append(Ladder(57,87))
ladders.append(Ladder(76,98))

# player

players = []
players.append(Player(1,'Tom'))
players.append(Player(2,'Jerry'))
players.append(Player(3,'Bob'))

snake_and_ladder_service = SnakeAndLadderService()
snake_and_ladder_service.setSnakes(snakes)
snake_and_ladder_service.setLadders(ladders)
snake_and_ladder_service.setPlayers(players)
snake_and_ladder_service.startGame()