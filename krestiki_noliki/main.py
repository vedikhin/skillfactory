from game import Game
from field import Field
from player_factory import PlayerFactory

game = Game(Field(), PlayerFactory())
game.play()