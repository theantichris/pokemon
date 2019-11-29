class Pokemon:
    def __init__(self, name, type, level = 1):
        self.name = name
        self.type = type
        self.level = level
        self.max_health = level * 5
        self.current_health = self.max_health
        self.is_knocked_out = False

    def __repr__(self):
        return "{} is a level {} {} type Pokemon with {} max health.".format(self.name, self.level, self.type, self.max_health)

    def lose_health(self, health):
        print("{} took {} damage.".format(self.name, health))
        self.current_health -= health
        if self.current_health <= 0:
            self.current_health = 0
            self.knock_out()
        else:
            print("{} now has {} health.".format(self.name, self.current_health))

    def gain_health(self, health):
        print("{} healed {} damage.".format(self.name, health))
        if self.current_health == 0:
            self.revive()
            health -= 1
        self.current_health += health
        if self.current_health > self.max_health:
            self.current_health = self.max_health
        print("{} now has {} health.".format(self.name, self.current_health))
    
    def knock_out(self):
        self.is_knocked_out = True
        print("{} has been knocked out.".format(self.name))
    
    def revive(self):
        self.is_knocked_out = False
        if self.current_health <= 0:
            self.current_health = 1
        print("{} has been revived.".format(self.name))

pokemon = Pokemon("Squirtle", "Water")
print(pokemon)
pokemon.lose_health(5)
pokemon.gain_health(4)
