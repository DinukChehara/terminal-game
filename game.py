import json
import time
import os

from locations.village import Village
from player import Player

#locations
village = Village()
player = Player()

class Game:

    def __init__(self): 
        
        #item : price

        self.items = {
            "sword": 50,
            "shield": 30,
            "potion": 10,
            "key": 5,
            "map": 15,
            "bread": 2,
            "saphire_gem": 1000
        }
        
        #location : level

        self.locations = {
            village.name: village.required_level,
            "forest": 0,
            "castle": 1,
            "dungeon": 2
        }

    def menu(self):
        options = [1,2,3]
        print("Choose an option:\n1. New\n2. Load\n3. Exit\n")
        while True:
            option = input(">> ")
            if option in options:
                break

            elif option == "1":
                os.system("clear")
                print("\nCreating new game instance!\n")
                time.sleep(1)
                self.newPlayer()
                break
            elif option == "2":
                os.system("clear")
                print("\nLoading player list!\n")
                time.sleep(1)
                self.load() 
                break
            elif option == "3":
                os.system("clear")
                print("\nExiting!\n")
                exit()
            else:
                print("\nInvalid choice!\n")

    def playerExists(self, player):
        try:
            with open("save.json", "r") as f:
                data = json.load(f)
                if player in data:
                    return True
                else:
                    return False
        except:
            return False

    def newPlayer(self):
        while True:
            player_name = input("Enter a player name: ")
            if self.playerExists(player_name):
                print(f"Player name {player_name} already exists! Please enter a different name.\n")
                continue
            else:
                break
        return Player(name=player_name)

    def save(self, player):
        try:
            with open("save.json", "r") as f:
                data = json.load(f)
        except:
            data = None

        if not data:
            data = {}
        
        data[player.name] = (player.attributes)

        with open("save.json", "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        try:
            with open("save.json", "r") as f:
                data = json.load(f)
                for player, attributes in data.items():
                    print(f"{player}:  {attributes}")
                print('\n')
                
                while True:
                    choose = input("Choose a player to load: ")
                    if choose in data:
                        break
                    else:
                        print("Player invalid! Please enter one from the above list.\n")

            print(f"{choose} : {attributes}")
            player = self.setPlayerAttributes(player, choose, attributes)
            self.start()
        except:
            pass 

    def setPlayerAttributes(player:Player, player_name:str, attributes:dict):

        player.name = player_name
        
        for key in attributes():
            player.attributes[key] == attributes[key]
        return player
    
    def start():
        print("Starting the game!")
        time.sleep(2)
        os.system("clear")
        pass

        if player.location == "":
            player.setLocation("Village")            