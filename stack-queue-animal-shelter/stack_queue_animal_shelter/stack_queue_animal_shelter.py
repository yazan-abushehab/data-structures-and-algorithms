class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.timestamp = 0
    
    def enqueue(self, animal):
        animal.timestamp = self.timestamp
        self.timestamp += 1
        
        if animal.species == "dog":
            self.dogs.append(animal)
        elif animal.species == "cat":
            self.cats.append(animal)
    
    def dequeue(self, pref=None):
        if pref == "dog":
            if self.dogs:
                return self.dogs.pop(0)
        elif pref == "cat":
            if self.cats:
                return self.cats.pop(0)
        else:
            if self.dogs and self.cats:
                if self.dogs[0].timestamp < self.cats[0].timestamp:
                    return self.dogs.pop(0)
                else:
                    return self.cats.pop(0)
            elif self.dogs:
                return self.dogs.pop(0)
            elif self.cats:
                return self.cats.pop(0)
        
        return None
