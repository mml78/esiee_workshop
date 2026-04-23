"""Simple superhero utilities."""


class Superhero:
    def __init__(self, name, powers, origin, friends, age):
        self.name = name
        self.powers = list(powers)
        self.origin = origin
        self.friends = friends
        self.age = age
        self.energy = 100

    def print_name(self):
        print(self.name)

    def print_attributes(self):
        print("Superhero attributes are:")
        print(self.name)
        print(self.powers)
        print(self.origin)
        print(self.friends)
        print(self.age)

    def add_power(self, power):
        if power not in self.powers:
            self.powers.append(power)

    def fly(self):
        self.add_power("Flight")
        self.energy -= 50
        print(f"{self.name} takes off into the sky")

    def turn_invisible(self):
        if self.energy >= 1:
            self.add_power("Invisibility")
            self.energy -= 1
            print(f"{self.name} becomes completely invisible")

    def super_strength(self):
        if self.energy >= 10:
            self.add_power("Super Strength")
            self.energy -= 10
            print(f"{self.name} becomes strong")

    def teleportation(self):
        if self.energy >= 10:
            self.add_power("Teleportation")
            self.energy -= 10
            print(f"{self.name} instantly teleports")

    def shoot_lasers(self):
        if self.energy >= 20:
            self.add_power("Shoot Lasers")
            self.energy -= 20
            print(f"{self.name} shoots lasers from eyes")

    def mod_weapons(self):
        if self.energy >= 20:
            self.add_power("Transform the weapon")
            self.energy -=20
            print(f"{self.name}: Transformation of the weapon complete!")
        else:
            print(f"{self.name}: Low energy! Cannot transform the weapon.")

    def shield(self):
        if self.energy >=10:
            self.energy -= 10
            print(f"{self.name} activates the shield!")
        else :
            print("Low energy ! Cannot activate the shield")


# Example usage
if __name__ == "__main__":
    ironman = Superhero("IronMan", ["tech"], "Earth", "Pepper", 35)
    ironman.print_name()
    ironman.print_attributes()
    ironman.fly()


# Spiderman
    spiderman = Superhero("Spiderman", ["web-shooting", "spider-sense"], "Queens", "Ned", 17)
    spiderman.print_name()
    spiderman.super_strength()


# Doctor Strange
    dr_strange = Superhero("Doctor Strange", ["magic"], "New York", "Wong", 42)
    dr_strange.print_name()
    dr_strange.teleportation() 