from locations.location import Location

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