class Pokemon:
    def __init__(self, name, type, max_health):
        self.name = name
        self.level = 1
        self.type = type
        self.max_health = max_health
        self.current_health = max_health
        self.is_knocked_out = False
    def lose_health(self, health):
        self.current_health -= health
        if self.current_health <= 0:
            self.current_health = 0
        print(self.name + " took " + str(health) + " damage and now has " + str(self.current_health) + " health.")
        if self.current_health == 0:
            self.knock_out()
    def gain_health(self, health):
        self.current_health += health
        if self.current_health > self.max_health:
            self.current_health = self.max_health
        print (self.name + " healed for " + str(health) + " and now has " + str(self.current_health) + " health.")
    def knock_out(self):
        self.is_knocked_out = True
        print(self.name + " is knocked out.")
    def revive(self):
        self.is_knocked_out = False
        print(self.name + " has been revived.")
        self.gain_health(1)

pokemon = Pokemon("Pikachu", "Electricity", 100)
pokemon.lose_health(101)
pokemon.revive()
pokemon.gain_health(10)
