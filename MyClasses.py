class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, Animal):
        self.animals.append(Animal)

    def get_animals(self):
        return self.animal

    def __str__(self):
        animal_list = ", ".join(str(animal) for animal in self.animals)
        return f"Zoo Name: {self.name}, Animals: {animal_list}"

class Visitor:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.happiness_level = 0

    def see_animal(self, animal):
        self.happiness_level += 5

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.species = "Unknown"
        self.health_level = 100

    def feed(self, food_amount):
        self.health_level = min(100, self.health_level + food_amount)

    def myHealth(self):
        return self.health_level
    
    def getting_hungry(self, amount):
        self.health_level = max(0, self.health_level - amount)  

    def __str__(self):
        return f"{self.name} the {self.species}"
    
class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.species = "Lion"

class Elephant(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.species = "Elephant"

class Chimpanzee(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.species = "Chimpanzee"



#test
if __name__ == "__main__":   
    my_zoo = Zoo("My Little Zoo")
    
    leo = Lion("Leo", 5)
    ella = Elephant("Ella", 10)
    bob = Chimpanzee("Bob", 3)
    bill = Chimpanzee("Bill", 4)
    
    my_zoo.add_animal(leo)
    my_zoo.add_animal(ella)
    my_zoo.add_animal(bob)
    my_zoo.add_animal(bill) 
    
    print(leo)
    
    print(my_zoo)
    
