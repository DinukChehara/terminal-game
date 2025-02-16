import os
import time


class Location:

    def __init__(self, name=None, required_level=0, tier=0, price=0):
        
        self.name = name
        self.required_level = required_level
        self.tier = tier
        self.price = price
        self.quests = {}
        self.quest_dialogues = {}
        self.quest_index = 0

    def __repr__(self):
        return f"Name: {self.name}, required level: {self.required_level}, tier: {self.tier}, price: {self.price}"
    
    def giveQuestDialogue(self, player_name):

        quest_givers = list(self.quest_dialogues.keys())
        quest_dialogues = self.quest_dialogues[quest_givers[self.quest_index]]
        self.quest_index +=1 

        dia1 = quest_dialogues["dialogue1"]
        dia2 = quest_dialogues["dialogue2"]

        opt1 = quest_dialogues["options"]["1"]["text"]
        opt2 = quest_dialogues["options"]["2"]["text"]

        response1 = quest_dialogues["options"]["1"]["response"]
        response2 = quest_dialogues["options"]["2"]["response"]

        os.system("clear")

        print("----QUEST----\n")
        time.sleep(1)
        print(dia1)
        time.sleep(3)
        print(dia2)
        time.sleep(3)

        print("\nYour response: \n")
        print(f"1. {opt1}")
        print(f"2. {opt2}")

        while True:
            user_response = input("\n>> ")

            os.system("clear")

            print("----QUEST----\n")
            print(dia1)
            print(dia2)
             
            if user_response == "1":
                print(f"\n{player_name}: {opt1}\n")
                time.sleep(3)
                print(response1)
                time.sleep(3)
                break
            elif user_response == "2":
                print(f"\n{player_name}: {opt2}\n")
                time.sleep(3)
                print(response2)
                time.sleep(3)
                break
            else:
                continue
        if user_response == "1":
            return True
