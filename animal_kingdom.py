class AnimalKingdom:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

    def move(self):
        return f"{self.name} is moving."


class Rabbit(AnimalKingdom):
    def __init__(self, name):
        super().__init__(name)

    def hop(self):
        return f"{self.name} is hopping."

    def nibble(self):
        return f"{self.name} is nibbling on some plants."


class Snake(AnimalKingdom):
    def __init__(self, name, species=None):
        super().__init__(name)
        self.species = species

    def slither(self):
        if self.species:
            return f"{self.name} the {self.species} is slithering."
        return f"{self.name} is slithering."

    def hiss(self):
        if self.species:
            return f"{self.name} the {self.species} is hissing."
        return f"{self.name} is hissing."
