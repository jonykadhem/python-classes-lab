class Character():
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level
        
    def describe(self):
        print(f'Name: {self.name} | Health: {self.health} | Level: {self.level}')
        
    def takeDamage(self,amount):
        self.amount = amount
        self.health -= amount
        print(f'{self.name} takes {self.amount}. Remaining health: {self.health}')
        


class Warrior(Character):
    warriors = []
    def __init__(self, name, health=100, level=4):
        Character.__init__(self, name, health, level)
        Warrior.warriors.append(self)
        
    def attack(self, target):
        damage = self.level * 5
        target.health -= damage
        
        print(f'{self.name} attacks {target.name} for {damage} damage!')
        
    @classmethod
    def listWarriors(cls):
        print("\n--- 🛡️ All Warrior Statuses ---")
        for warrior in cls.warriors:
            warrior.describe()
        

class Healer(Character):
    def __init__(self, name, health=100, level=3):
        Character.__init__(self, name, health, level)
    
    def heal(self, target):
        if target.health == 100 or target.health == 0:
            print(f"{target.name} can not be healed ")
        elif target.name == self.name:
            print('can not heal your self')
        else:
            healer = self.level * 4
            target.health += healer
            print(f'{self.name} heals {target.name} for {healer} health') 
        

# --- Characters Setup ---
darkNight_123 = Warrior("darkNight_123")
the_samboosaMan = Warrior("the_samboosaMan")
hmany_313 = Character("hmany_313", health=100, level=4)
f_thekiller_911 = Healer("Fadhel")


print("--- ⚔️ Battle Begins! ---")
darkNight_123.attack(hmany_313)
the_samboosaMan.attack(hmany_313)
f_thekiller_911.heal(hmany_313)
the_samboosaMan.attack(f_thekiller_911)
f_thekiller_911.heal(f_thekiller_911)
Warrior.listWarriors()