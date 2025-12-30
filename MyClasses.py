from random import choice
import InternalLog


class Visitor:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.happiness_level = 0
        self.current_animal = 0

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

    def get_zoo_log(self, log):
        self.log = log

# Health management, the same for all animals
    def feed(self, food_amount):
        self.health_level = min(100, self.health_level + food_amount)

    def myHealth(self):
        return self.health_level
    
    def getting_hungry(self, amount):
        self.health_level = max(0, self.health_level - amount)  

    def isdead(self):   
        return self.health_level <= 0

    def __str__(self):
        return f"{self.name} the {self.species} (Health: {self.health_level})"
    
# Interactions to be implemented in subclasses
    def interact(self, visitor):
        visitor.see_animal(self)

    def interact_animal(self, animal):
        # super kollar om det är samma djur som iteragerar med sig själv
        if self == animal:
            self.log.add(f"{self.name} the {self.species} looks at itself in the mirror.", level="ANIMAL")
            return True
        else:
            return False

    def getsAttacked(self, attacker):
        pass


# Subclasses for specific animal types, affecting behavior and interactions under attack
class Carnivore(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.diet = "Carnivore"

class Herbivore(Animal):   
    def __init__(self, name, age):
        super().__init__(name, age)
        self.diet = "Herbivore"

# actual animal classes

class Lion(Carnivore):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.species = "Lion"

    def roars(self):
        if self.health_level < 20:
            self.log.add("The lion is too weak to roar.", level="ANIMAL")
            return False
        self.log.add("Roar!", level="ANIMAL")
        self.getting_hungry(2)
        return True
    
    def interact(self, visitor):
        super().interact(visitor)
        if self.roars():
            visitor.happiness_level += 15

    def interact_animal(self, animal):
        if super().interact_animal(animal):
            return
        else:
            if isinstance(animal, Lion):
                self.log.add(f"{self.name} the Lion purrs and kisses {animal.name} the Lion.", level="ANIMAL")
            else:
                if animal.diet == "Herbivore":
                    self.log.add(f"{self.name} the Lion is hungry! And tries to eat {animal.name} the {animal.species}.", level="ANIMAL")
                    animal.getsAttacked(self)
                else:
                    self.log.add(f"{self.name} the Lion growls at {animal.name} the {animal.species} and retreats.", level="ANIMAL")
            return
        
    def getsAttacked(self, attacker):
        if self.health_level < 30:
            self.log.add(f"Lion {self.name} got hurt by {attacker.name} the {attacker.species}", level="ANIMAL") 
            self.getting_hungry(5)
        else:
            self.log.add(f"{self.name} the Lion ignored the attack from {attacker.name} the {attacker.species}!", level="ANIMAL")

class Elephant(Herbivore):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.species = "Elephant"
    
    def squirt_water(self):
        if self.health_level < 30:
            self.log.add("The elephant is too weak to squirt water.", level="ANIMAL")
            return False
        
        self.log.add("Squirt!", level="ANIMAL")
        self.getting_hungry(3)
        return True
    
    def interact(self, visitor):
        super().interact(visitor)
        if self.squirt_water():
            visitor.happiness_level += 7

    def interact_animal(self, animal):
        if super().interact_animal(animal):
            return
        else:
            if isinstance(animal, Elephant):
                self.log.add(f"{self.name} and {animal.name} honks and stamps happily.", level="ANIMAL")
            else:
                self.log.add(f"{self.name} the Elephant charges {animal.name} the {animal.species}.", level="ANIMAL")
                animal.getsAttacked(self)
                return
        
    def getsAttacked(self, attacker):
        if attacker.diet == "Carnivore" and attacker.health_level > 60:
            self.log.add(f"{self.name} the Elephant got hurt by {attacker.name} the {attacker.species}!", level="ANIMAL")
            self.getting_hungry(20)
        else:
            self.log.add(f"{self.name} the Elephant dodged the attack from {attacker.name} the {attacker.species}!", level="ANIMAL")
    


class Chimpanzee(Herbivore):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.species = "Chimpanzee"
    
    def making_monkey_sounds(self):
        if self.health_level < 5:
            self.log.add("The chimpanzee is too weak to make sounds.", level="ANIMAL")
            return False
            
        self.log.add("Ooh ooh aah aah!", level="ANIMAL")
        self.getting_hungry(3)
        return True
    
    def interact(self, visitor):
        visitor.see_animal(self)
        if self.making_monkey_sounds():
            visitor.happiness_level += 12
    
    def interact_animal(self, animal):
        if super().interact_animal(animal):
            return
        else:
            if isinstance(animal, Chimpanzee):
                self.log.add(f"{self.name} and {animal.name} dance a monkey dance.", level="ANIMAL")
            else:
                self.log.add(f"{self.name} the Chimpanzee throughs a cocnut at {animal.name} the {animal.species}.", level="ANIMAL")
                animal.getsAttacked(self)
                return
        
    def getsAttacked(self, attacker):
        if attacker.diet == "Carnivore" and attacker.health_level > 15:
            self.log.add(f"{self.name} the Chimpanzee got hurt by {attacker.name} the {attacker.species}!", level="ANIMAL")
            self.getting_hungry(15)
        else:
            self.log.add(f"{self.name} the Chimpanzee dodged the attack from {attacker.name} the {attacker.species}!", level="ANIMAL")

class Gazelle(Herbivore):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.species = "Gazelle"
    
    def jumps_around(self):
        if self.health_level < 5:
            self.log.add("The gazelle is to weak to jump.", level="ANIMAL")
            return False
            
        self.log.add("The gazelle jumps elegantly", level="ANIMAL")
        self.getting_hungry(3)
        return True
    
    def interact(self, visitor):
        visitor.see_animal(self)
        if self.jumps_around():
            visitor.happiness_level += 2
    
    def interact_animal(self, animal):
        if super().interact_animal(animal):
            return
        else:
            if isinstance(animal, Gazelle):
                self.log.add(f"{self.name} and {animal.name} makes beautiful jumps.", level="ANIMAL")
            else:
                self.log.add(f"{self.name} the Gazelle tries to stab {animal.name} the {animal.species}.", level="ANIMAL")
                animal.getsAttacked(self)
                return
        
    def getsAttacked(self, attacker):
        if attacker.diet == "Carnivore" and attacker.health_level > 15:
            self.log.add(f"{self.name} the Gazelle got hurt by {attacker.name} the {attacker.species}!", level="ANIMAL")
            self.getting_hungry(15)
        else:
            self.log.add(f"{self.name} the Gazelle couldnt avoid the attack from {attacker.name} the {attacker.species}!", level="ANIMAL")
            self.getting_hungry(5)

class Tiger(Carnivore):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.species = "Tiger"
    
    def prance(self):
        if self.health_level < 5:
            self.log.add("The tiger is too weak to prance.", level="ANIMAL")
            return False
            
        self.log.add("The tiger prances around his cage glaring at the visitor", level="ANIMAL")
        self.getting_hungry(3)
        return True
    
    def interact(self, visitor):
        visitor.see_animal(self)
        if self.prance():
            visitor.happiness_level += 12
    
    def interact_animal(self, animal):
        if super().interact_animal(animal):
            return
        else:
            if isinstance(animal, Tiger):
                self.log.add(f"{self.name} and {animal.name} decided to take a nap together.", level="ANIMAL")
            else:
                self.log.add(f"{self.name} the Tiger wants to take a bite of {animal.name} the {animal.species}.", level="ANIMAL")
                animal.getsAttacked(self)
                return
        
    def getsAttacked(self, attacker):
        if attacker.diet == "Carnivore" and attacker.health_level > 50:
            self.log.add(f"{self.name} the Tiger got hurt by {attacker.name} the {attacker.species}!", level="ANIMAL")
            self.getting_hungry(30)
        else:
            self.log.add(f"{self.name} the Tiger dodged the attack from {attacker.name} the {attacker.species}!", level="ANIMAL")


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.is_open = False
        self.time = 0       
        self.visitors = []
        self.visitor_counter = 0
        self.incident_counter = 0
        self.log = InternalLog.InternalLog()
        self.day = 0 
        self.overall_happiness = 0

    

# Hantering av djur i zoo
    # Djur-mapping
    animal_types = {
        "elephant": Elephant,
        "lion": Lion,
        "chimpanzee": Chimpanzee,
        "gazelle": Gazelle,
        "tiger": Tiger
    }

    def add_general_animal(self, animal, name, age):
        cls = self.animal_types.get(animal.lower())
        if cls is None:
            return False  # okänt djur

        self.add_animal(cls(name.capitalize(), age))
        return True
    
    def current_known_animals(self):
        return self.animal_types.keys()

    def add_animal(self, Animal):
        Animal.get_zoo_log(self.log)
        self.animals.append(Animal)
        self.log.add(f"{Animal.name} the {Animal.species} has been added to the zoo.", level="ZOO")

    def get_animals(self):
        return self.animals

    def feed_animals(self, food_amount):
        for animal in self.animals:
            if animal.myHealth() < 50:
                animal.feed(food_amount)
                self.log.add(f"{animal.name} the {animal.species} has been fed.", level="ZOO")

# Hantering av besökare i zoo
    def welcome_queue(self, x):
        for visitor in x:
            self.welcome_visitor(visitor)

    def welcome_visitor(self, visitor):
        if not self.is_open:
            self.log.add(f"Sorry, {visitor.name}, the zoo is currently closed.")
            return
        else: 
            self.log.add(f"Welcome to {self.name}, {visitor.name}!", level="VISITOR")
            visitor.current_animal = 0
            self.visitor_counter += 1 # Increment visitor counter
            self.visitors.append(visitor)

    def bye_visitor(self, visitor):
        if visitor in self.visitors:
            self.overall_happiness += visitor.happiness_level
            self.visitors.remove(visitor)
            self.log.add(f"Goodbye, {visitor}! Thanks for visiting {self.name}.",level="VISITOR")
        else:
            print(f"{visitor.name} is not in the zoo.")

    def empty_visitors(self):
        # make a copy of the visitor list to avoid modification during iteration
        v_copy = self.visitors.copy()
        for visitor in v_copy:
                self.bye_visitor(visitor)
        # se till att alla verkligen är borta (behövs kanske inte längre)
        self.visitors.clear()

    def visit_next_animal(self, visitor):
        if visitor.current_animal < len(self.animals):
            animal = self.animals[visitor.current_animal]
            animal.interact(visitor)
            visitor.current_animal += 1
            self.log.add(f"{visitor.name} visited {animal.name} the {animal.species}.", level="VISITOR")
        else:
            self.log.add(f"{visitor.name} has visited all animals in the zoo.", level="VISITOR")
            self.bye_visitor(visitor)
       
    
   
# print zoo status
    def __str__(self):
        animal_list = ", ".join(str(animal) for animal in self.animals)
        
        return f"Zoo Name: {self.name}, Animals: {animal_list}."
    
    def time_step_animals(self):
        # Handle animal interactions and health updates over a time ste
        dead_animals = []
        # Animal interactions and health updates
        for animal in self.animals:
            copy_of_animals = self.animals.copy()
            copy_of_animals.remove(animal)
            animal.interact_animal(choice(copy_of_animals))  # Animals interact with each other, not themselves
            animal.getting_hungry(3)  # Animals get hungrier over time
            if animal.isdead():
                self.log.add(f"{animal.name} the {animal.species} has died Incident report written.", level="ZOO")
                self.incident_counter += 1
                dead_animals.append(animal)
                self.log.add(f"All visitors are affected negatively by the death of {animal.name}!", level="ZOO")
                for visitor in self.visitors:
                    visitor.happiness_level -= 20

        # Remove dead animals from the zoo
        for dead_animal in dead_animals:    
            self.animals.remove(dead_animal)

        # feed animals if needed
        self.feed_animals(20)

    def time_step_visitors(self):
        # Move visitors to the next animal
            for visitor in self.visitors:
                self.visit_next_animal(visitor)         
    
# Hantering av tid och dess påverkan på zoo
    def current_time(self, time):
        self.time = time
        self.log.add(f"Current time updated to {self.time} hours.", level="ZOO")

        # öppna eller stäng zoo beroende på tid
        if 9 <= self.time < 19:
            if not self.is_open:
                self.is_open = True
                self.day += 1
                self.log.add(f"{self.name} is now OPEN. {self}", level="ZOODAY")
        else:   
            if self.is_open:
                self.log.add(f"{self.name} is now CLOSED. {self}", level="ZOODAY")
                self.empty_visitors()
                if self.visitor_counter > 0:
                    self.log.add(f"Today, {self.visitor_counter} visitors came to the zoo. Average happiness = {self.overall_happiness/self.visitor_counter}. The number of incidents today: {self.incident_counter}.", level="ZOODAY")
                else:
                    self.log.add(f"Today, no visitors came to the zoo. The number of incidents today: {self.incident_counter}.", level="ZOODAY")
                self.visitor_counter = 0 # reset counter for the next day
                self.overall_happiness = 0 # reset overall happiness for the next day
                self.incident_counter = 0 # reset incident counter for the next day
            self.is_open = False
            
        # uppdatera djur och besökare i zoo
        self.time_step_animals()
        if self.is_open:
            self.time_step_visitors()
            
        self.log.add(f"End of time step {self.time}, day {self.day}: {self}", level="ZOO")
        
    # random acts from input
    def storm_event(self):
        self.log.add("A sudden storm hits the zoo! Affects all animals health level and the visitors goes home sad", level="ZOO")
        for animal in self.animals:
            animal.getting_hungry(10)
        for visitor in self.visitors:
            visitor.happiness_level -= 15
        self.empty_visitors()
        self.incident_counter += 1

    def fire_event(self):
        self.log.add("A fire breaks out in the zoo! Emergency protocols activated.", level="ZOO")
        for animal in self.animals:
            animal.getting_hungry(20)
        for visitor in self.visitors:
            visitor.happiness_level -= 50
        self.empty_visitors()
        self.incident_counter += 1


# hämta loggar
    def get_zoo_log(self):
        return self.log.get_level("ZOODAY")
    
    def get_all_log(self):
        return self.log.get_all()


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
    
