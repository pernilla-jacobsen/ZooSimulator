class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, Animal):
        self.animals.append(Animal)

    def get_animals(self):
        return self.animals

    def __str__(self):
        return f"Zoo Name: {self.name}, Animals: {', '.join(self.animals)}"


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.species = "Unknown"

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
    
    
    
    print(my_zoo)
    
