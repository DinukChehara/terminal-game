from game import Game
from player import Player
from locations.village import Village

player = Player()
village = Village()
game = Game()

game.giveQuests(player, village)