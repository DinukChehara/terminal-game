from locations.location import Location
import os
import time
from player import Player

class Village(Location):
    
    def __init__(self):
        
        super().__init__(name="Village", required_level=0, tier=0, price=0)
        
        self.quests = {
                    "Find the Lost Chicken": 1,
                    "Gather Herbs for the Healer": 2,
                    "Defend the Village from Bandits": 3,
                    "Deliver a Package to the Blacksmith": 1,
                    "Investigate the Haunted Forest": 3
                    }
        
        self.quest_dialogues = {
                "Farmer": {
                    "completed": False,  # Tracks if the quest is completed
                    "dialogue1": "Farmer: 'Clucky, my chicken, is missing! Can you find her?'",
                    "dialogue2": "Farmer: 'She was last seen near the well. Please hurry!'",
                    "options": {
                        "1": {"text": "'I’ll find Clucky.'", "response": "Farmer: 'Thank you!'"},
                        "2": {"text": "'Not right now.'", "response": "Farmer: 'Alright, let me know if you change your mind.'"}
                    }
                },
                "Healer": {
                    "completed": False,  # Tracks if the quest is completed
                    "dialogue1": "Healer: 'I need 5 herbs from the forest. Can you help?'",
                    "dialogue2": "Healer: 'The forest is dangerous, so be careful!'",
                    "options": {
                        "1": {"text": "'I’ll get the herbs.'", "response": "Healer: 'Thank you!'"},
                        "2": {"text": "'I can’t help.'", "response": "Healer: 'No problem.'"}
                    }
                },
                "Village Guard": {
                    "completed": False,  # Tracks if the quest is completed
                    "dialogue1": "Guard: 'Bandits are attacking! Will you help us?'",
                    "dialogue2": "Guard: 'We need all the help we can get!'",
                    "options": {
                        "1": {"text": "'I’ll fight.'", "response": "Guard: 'Thank you! Follow me!'"},
                        "2": {"text": "'I’m not ready.'", "response": "Guard: 'Stay safe, then.'"}
                    }
                },
                "Merchant": {
                    "completed": False,  # Tracks if the quest is completed
                    "dialogue1": "Merchant: 'Can you deliver this package to the blacksmith?'",
                    "dialogue2": "Merchant: 'He’s near the forge. It’s urgent!'",
                    "options": {
                        "1": {"text": "'I’ll deliver it.'", "response": "Merchant: 'Great! Thanks!'"},
                        "2": {"text": "'I’m busy.'", "response": "Merchant: 'Alright, no worries.'"}
                    }
                },
                "Elder": {
                    "completed": False,  # Tracks if the quest is completed
                    "dialogue1": "Elder: 'The forest feels strange. Can you investigate?'",
                    "dialogue2": "Elder: 'Be careful—it’s not safe out there.'",
                    "options": {
                        "1": {"text": "'I’ll check it out.'", "response": "Elder: 'Thank you!'"},
                        "2": {"text": "'I’d rather not.'", "response": "Elder: 'Let me know if you change your mind.'"}
                    }
                }
            }

        
    
    def __repr__(self):
        return super().__repr__()
    
    def Welcome():
        print(welcome_dialogue = """
        You arrive at the peaceful village of Greenhaven. The air is fresh, and the villagers greet you with warm smiles.
        The village elder approaches you and says:
        'Welcome, traveler! Our village could use your help. Speak to the villagers to learn more.'
        """)
    
    def giveQuestDialogue(self):
        return super().giveQuestDialogue()
    
    def questFindChiken(self, player:Player):
        #location 1 - The well
        while True:
            os.sys("clear")
            print(f"You arrive at the well where Clucky was last seen. There are feathers scattered around, and you hear faint clucking in the distance.")
            time.sleep(2)
            print("\nChoose:\n 1. Follow the clucking sound\n 2. Search around the well for clues\n 3. Return to the farm for more information.\n")
            
            choice = input(">> ")
            os.sys("clear")
            if choice == "1":
                print("\nYou head towards the sound, leading you deeper into the forest.\n")
                break
            elif choice == "2":
                print("\nYou find a trial of feathers leading toward the forest.\n")
                break
            elif choice == "3":
                print("\nFarmer: 'I don't know much else, but I hopeyou find her!'\n")
                break
            else:
                continue
        
        #location 2 -The forest
        while True:
            os.sys("clear")
            print(f"The forest is dense and slightly eerie. You hear the clucking sound again, but it’s faint.")
            time.sleep(2)
            print("\nChoose:\n 1. Follow the clucking sound deeper into the forest.\n 2. Call out for Clucky.\n 3. Turn back—it’s too dangerous.\n")
            
            choice = input(">> ")
            os.sys("clear")
            if choice == "1":
                print("\nYou venture further and find Clucky stuck in a bush.\n")
                break
            elif choice == "2":
                print("\nClucky responds with loud clucking, and you locate her nearby.\n")
                break
            elif choice == "3":
                print("\nYou return to the village without finding Clucky. The Farmer is disappointed.'\n")
                break
            else:
                continue
        
        #location 3 - Deep forest
        while True:
            os.sys("clear")
            print(f"You find Clucky stuck in a bush, flapping her wings helplessly.")
            time.sleep(2)
            print("\nChoose:\n 1. Free Clucky from the bush.\n 2. Leave her—she’s too much trouble.\n")
            
            choice = input(">> ")
            os.sys("clear")
            if choice == "1":
                print("\nYYou carefully untangle her and pick her up.\n")
                time.sleep(2)
                print("Famer: 'You founde her! Thank you so much! Here's a reward for your help.'")
                time.sleep(1)
                print("+20 Coins\n+1 Completed Quest\n+1 Level")

                self.quest_dialogues["Farmer"]["completed"] = True
                player.increaseQuestsCompleted(1)
                player.addCoins(20)
                player.increaseLevel(1)
                break
            elif choice == "2":
                print("\nYou abandon Clucky and return to the village. The Farmer is upset.\n")
                time.sleep(2)
                print("Famer: 'Oh no...I hope she's okay. Please keep looking if you can.'")
                time.sleep(2)
                print("You failed the quest!")
                break
            else:
                continue
        time.sleep(3)
        os.sys("clear")





