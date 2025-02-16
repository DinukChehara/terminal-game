
class Player:

    def __init__(self, name="default", max_health=10, location = ""):
        
        self.name = name
        self.max_health = max_health
        self.health = 10
        self.location = location
        self.inventory = []
        self.level = 0
        self.attack_damage_multiplier = 1
        self.attack_damage = 1 * self.attack_damage_multiplier
        self.quests_completed = 0
        self.coins = 0

        self.attributes = {
            "max_health" : self.max_health,
            "health" : self.health,
            "location" : self.location,
            "inventory" : self.inventory,
            "level" : self.level,
            "attack_damage_multiplier" : self.attack_damage_multiplier,
            "attack_damage" : self.attack_damage,
            "quests_completed" : self.quests_completed,
            "coins" : self.coins
        }

    def __repr__(self):
        return f"Name: {self.name} | Health: {self.health}/{self.max_health} | Level: {self.level} | Attack Damage: {self.attack_damage} | Inventory: {self.inventory} | Location: {self.location} | Quests Completed: {self.quests_completed} | Coins: {self.coins}"

    def say(self, message: str):
        print(f"{self.name}(Player): {message}")

    def setHealth(self, value):
        self.health = value

    def setMaxHealth(self, value):
        if value < self.health:
            self.max_health = self.health
        else:
            self.max_health = value

    def gainHealth(self, amount):
        if self.health + amount <= self.max_health:
            self.health +=amount

    def loseHealth(self, amount):
        if self.health - amount >= 0:
            self.health -=amount

    def setLevel(self, value):
        self.level = value

    def increaseLevel(self, amount):
        self.level += amount

    def setAttackDamageMultiplier(self, value):
        self.attack_damage_multiplier = value

    def increaseAttackDamageMultiplier(self, amount):
        self.attack_damage_multiplier += amount

    def setLocation(self, location):
        self.location = location

    def setInventory(self, items:list):
        self.inventory = items

    def dropItem(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def pickUpItem(self, item):
        self.inventory.append(item)

    def setQuestsCompleted(self, value):
        self.quests_completed = value
    
    def increaseQuestsCompleted(self, amount):
        self.quests_completed += amount       

    def setCoins(self, value):
        if value<0:
            self.coins = 0
        else:
            self.coins = value

    def addCoins(self, amount):
        self.coins += amount

    def subtractCoins(self, amount):
        self.coins -= amount