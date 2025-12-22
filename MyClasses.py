from random import choice

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.is_open = False
        self.time = 0       
        self.visitors = []
        self.visitor_counter = 0

    def add_animal(self, Animal):
        self.animals.append(Animal)

    def get_animals(self):
        return self.animal

    def welcome_queue(self, x):
        for visitor in x:
            self.welcome_visitor(visitor)

    def welcome_visitor(self, visitor):
        if not self.is_open:
            print(f"Sorry, {visitor.name}, the zoo is currently closed.")
            return
        else: 
            print(f"Welcome to {self.name}, {visitor.name}!")
            visitor.current_animal = 0
            self.visitor_counter += 1 # Increment visitor counter
            self.visitors.append(visitor)

    def bye_visitor(self, visitor):
        if visitor in self.visitors:
            self.visitors.remove(visitor)
            print(f"Goodbye, {visitor.name}! Thanks for visiting {self.name}.")
        else:
            print(f"{visitor.name} is not in the zoo.")

    def visit_next_animal(self, visitor):
        if visitor.current_animal < len(self.animals):
            animal = self.animals[visitor.current_animal]
            animal.interact(visitor)
            visitor.current_animal += 1
            print(f"{visitor.name} visited {animal.name} the {animal.species}.")
        else:
            print(f"{visitor.name} has visited all animals in the zoo.")
            self.bye_visitor(visitor)
       
    
    def feed_animals(self, food_amount):
        for animal in self.animals:
            animal.feed(food_amount)

    def __str__(self):
        animal_list = ", ".join(str(animal) for animal in self.animals)
        return f"Zoo Name: {self.name}, Animals: {animal_list}"
    
    def current_time(self, time):
        self.time = time

        if 9 <= self.time < 19:
            if not self.is_open:
                self.is_open = True
                print(f"{self.name} is now OPEN.")
        else:   
            if self.is_open:
                print(f"{self.name} is now CLOSED.")
                for visitor in self.visitors:
                    self.bye_visitor(visitor)
                print(f"Today, {self.visitor_counter} visitors came to the zoo.")
                self.visitor_counter = 0 # reset counter for the next day

            self.is_open = False
            

        for animal in self.animals:
            animal.interact_animal(choice(self.animals,))  # Animals interact with each other randomly
            animal.getting_hungry(3)  # Animals get hungrier over time
            if animal.isdead():
                print(f"{animal.name} the {animal.species} has died Incident report written.")
                self.animals.remove(animal)
                print(f"All visitors are affected negatively by the death of {animal.name}!")
                for visitor in self.visitors:
                    visitor.happiness_level -= 20

        # move the visitors to the next animal
        if self.is_open:
            for visitor in self.visitors:
                self.visit_next_animal(visitor)  
            


        if self.time in [7.0,12.0,19.0]:
            self.feed_animals(20)
            print("Feeding time for the animals!")
        

        print(self)


class Visitor:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.happiness_level = 0

    def see_animal(self, animal):
        if self.age > 12:
            self.happiness_level += 3
        else:
            self.happiness_level += 20

    def __str__(self):
        return f"Visitor Name: {self.name}, Age: {self.age}, Happiness Level: {self.happiness_level}"

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

    def interact(self, visitor):
        visitor.see_animal(self)

    def interact_animal(self, animal):
        pass

    def getsAttacked(self, attacker):
        pass

    def isdead(self):   
        return self.health_level <= 0

    def __str__(self):
        return f"{self.name} the {self.species} (Health: {self.health_level})"

class Carnivore(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.diet = "Carnivore"


class Herbivore(Animal):   
    def __init__(self, name, age):
        super().__init__(name, age)
        self.diet = "Herbivore"

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.species = "Lion"

    def roars(self):
        if self.health_level < 20:
            print("The lion is too weak to roar.")
            return False
        print("Roar!")
        self.getting_hungry(20)
        return True
    
    def interact(self, visitor):
        visitor.see_animal(self)
        if self.roars():
            visitor.happiness_level += 15

    def interact_animal(self, animal):
        if isinstance(animal, Lion):
            print(f"{self.name} the Lion purrs and kisses {animal.name} the Lion.")
        else:
            print(f"{self.name} the Lion is hungry! And tries to eat {animal.species}.")
            animal.getsAttacked(self)
            return
        
    def getsAttacked(self, attacker):
        if self.health_level < 30:
            print(f"Lion {self.name} got hurt by {attacker.name} the {attacker.species}") 
            self.getting_hungry(5)
        else:
            print(f"{self.name} the Lion ignored the attack from {attacker.name} the {attacker.species}!")

class Elephant(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.species = "Elephant"
    
    def squirt_water(self):
        if self.health_level < 30:
            print("The elephant is too weak to squirt water.")
            return False
        
        print("Squirt!")
        self.getting_hungry(30)
        return True
    
    def interact(self, visitor):
        visitor.see_animal(self)
        if self.squirt_water():
            visitor.happiness_level += 7

    def interact_animal(self, animal):
        if isinstance(animal, Elephant):
            print(f"{self.name} and {animal.name} honks and stamps happily.")
        else:
            print(f"{self.name} the Elephant charges {animal.species}.")
            animal.getsAttacked(self)
            return
        
    def getsAttacked(self, attacker):
        if attacker.health_level > 50:
            print(f"{self.name} the Elephant got hurt by {attacker.name} the {attacker.species}!")
            self.getting_hungry(50)
        else:
            print(f"{self.name} the Elephant dodged the attack from {attacker.name} the {attacker.species}!")
    


class Chimpanzee(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.species = "Chimpanzee"
    
    def making_monkey_sounds(self):
        if self.health_level < 5:
            print("The chimpanzee is too weak to make sounds.")
            return False
            
        print("Ooh ooh aah aah!")
        self.getting_hungry(5)
        return True
    
    def interact(self, visitor):
        visitor.see_animal(self)
        if self.making_monkey_sounds():
            visitor.happiness_level += 12
    
    def interact_animal(self, animal):
        if isinstance(animal, Chimpanzee):
            print(f"{self.name} and {animal.name} dance a monkey dance.")
        else:
            print(f"{self.name} the Chimpanzee throughs a cocnut at {animal.species}.")
            animal.getsAttacked(self)
            return
        
    def getsAttacked(self, attacker):
        if attacker.health_level > 30:
            print(f"{self.name} the Chimpanzee got hurt by {attacker.name} the {attacker.species}!")
            self.getting_hungry(40)
        else:
            print(f"{self.name} the Chimpanzee dodged the attack from {attacker.name} the {attacker.species}!")

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
    
    ville = Visitor("Ville", 30)
    anna = Visitor("Anna", 25)
    elina = Visitor("Elina", 12)

    my_zoo.welcome_visitor(ville)
    my_zoo.welcome_visitor(anna)
    my_zoo.welcome_visitor(elina)
    my_zoo.welcome_visitor(ville)
    my_zoo.welcome_visitor(anna)
    my_zoo.welcome_visitor(elina)

    print(f"{ville.name}'s happiness level: {ville.happiness_level}")
    
    print(my_zoo)
    
