class Pokemon:
    def __init__(self, name, type, level=1):
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
            print("{} now has {} health.".format(
                self.name, self.current_health))

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

    def attack(self, other_pokemon):
        if self.is_knocked_out:
            print("{} is knocked out and cannot attack.".format(self.name))
            return

        if (self.type == "Fire" and other_pokemon.type == "Water") or (self.type == "Water" and other_pokemon.type == "Grass") or (self.type == "Grass" and other_pokemon.type == "Fire"):
            damage = round(self.level * .05)
            print("{} attacked {} for {} damage.".format(
                self.name, other_pokemon.name, damage))
            print("It's not very effective.")
        elif (self.type == "Fire" and other_pokemon.type == "Grass") or (self.type == "Water" and other_pokemon.type == "Fire") or (self.type == "Grass" and other_pokemon.type == "Water"):
            damage = self.level * 2
            print("{} attacked {} for {} damage.".format(
                self.name, other_pokemon.name, damage))
            print("It's super effective!")
        else:
            damage = self.level
            print("{} attacked {} for {} damage.".format(
                self.name, other_pokemon.name, damage))

        other_pokemon.lose_health(damage)


class Trainer:
    def __init__(self, name, pokemon_list, num_potions):
        self.name = name
        self.pokemon_list = pokemon_list
        self.num_potions = num_potions
        self.current_pokemon = 0

    def __repr__(self):
        print("Trainer {} has the following Pokemon:".format(self.name))
        for pokemon in self.pokemon_list:
            print(pokemon)
        return "Their current active Pokemon is {}".format(self.pokemon_list[self.current_pokemon].name)

    def use_potion(self):
        if self.num_potions <= 0:
            print("{} does not have any potions.".format(self.name))
            return

        print("{} used a potion on {}.".format(self.name, self.pokemon_list[self.current_pokemon].name))
        self.pokemon_list[self.current_pokemon].gain_health(20)
        self.num_potions -= 1

    def switch_active_pokemon(self, new_pokemon):
        if new_pokemon >= 0 and new_pokemon < len(self.pokemon_list):
            if self.pokemon_list[new_pokemon].is_knocked_out:
                print("{} is knocked out.".format(self.pokemon_list[new_pokemon].name))
            elif self.current_pokemon == new_pokemon:
                print("{} is already {}'s active Pokemon.".format(self.pokemon_list[new_pokemon].name, self.name))
            else:
                self.current_pokemon = new_pokemon
                print("{}, I choose you!".format(self.pokemon_list[self.current_pokemon].name))

    def attack(self, other_trainer):
        self.pokemon_list[self.current_pokemon].attack(other_trainer.pokemon_list[other_trainer.current_pokemon])

squirtle = Pokemon("Squirtle", "Water")
charmander = Pokemon("Charmander", "Fire")
trainer = Trainer("Christopher", [squirtle, charmander], 1)

trainer.use_potion()
trainer.use_potion()
