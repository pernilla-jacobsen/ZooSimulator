import MyClasses
from random import choice, randint
from time import sleep
import threading

""" Jag vill ha en Tid hanterare som ger klockslag över en dag. """
class TimeManager:
    def __init__(self, start_time=6):
        self.current_time = start_time  # Start at early morning (6:00 hours)
    
    def advance_time(self, hours):
        self.current_time = (self.current_time + hours) % 24  # Wrap around after 24 hours
    
    def get_current_time(self):
        return self.current_time

""" Skapar ett antal besökare med slumpmässiga namn och åldrar. """    
def visitor_creator(num_visitors= 1):
    names = ["Alice", "Bob", "Charlie", "Diana", "Ellen", "Fred", "Göran", "Harald", "Ivan", "Johan","Karin","Lena","Mia","Nina","Olle","Pernilla","Sven","Tina"]
    ages = [5, 7,8,9,10,11,13, 20 ,25,30,35,40,45,50,55,60] # högre sannlighet för barn
    visitors = []

    for _ in range(num_visitors):
        name = choice(names)
        age = choice(ages)
        visitors.append(MyClasses.Visitor(name, age))
    return visitors

""" Startar ett zoo med några djur. """
def start_zoo():
    myzoo = MyClasses.Zoo("Little Zoo")

    myzoo.add_animal(MyClasses.Lion("Leo", 5))
    myzoo.add_animal(MyClasses.Lion("Simba", 4))  
    myzoo.add_animal(MyClasses.Elephant("Ella", 10))
    myzoo.add_animal( MyClasses.Elephant("Ollie", 8) )
    myzoo.add_animal(MyClasses.Chimpanzee("Bill", 3))     
    myzoo.add_animal(MyClasses.Chimpanzee("Bob", 4))
    myzoo.add_animal(MyClasses.Chimpanzee("Berit", 3))
    myzoo.add_animal(MyClasses.Chimpanzee("Britta", 4))

    return myzoo

def run_zoo_simulation(myzoo):
    time_manager = TimeManager()
    print(f"Current Time: {time_manager.get_current_time()} hours")

    while True:
    # den här loopen simulerar livet i zoo tills vi stoppar det manuellt  (fn-b på mitt tangentbord)  
        sleep(5)  # wait for 5 second to simulate time passing
        time_manager.advance_time(0.5) # Advance time by 30 minutes
        print(f"Advanced Time: {time_manager.get_current_time()} hours")
        # Create random visitors and welcome them to the zoo
        if myzoo.is_open: 
            myzoo.welcome_queue(visitor_creator(randint(0, 5)))
        # Update zoo status based on current time
        myzoo.current_time(time_manager.get_current_time())
    

def input_listener():
    """Lyssnar på användarens input för att stoppa simuleringen."""
    while True:
        user_input = input("Skriv 'exit' för att stoppa simuleringen: ")
        if user_input.lower() == 'exit':
            print("Stoppar simuleringen...")
            break


if __name__ == "__main__":
    #initialize zoo 
    
    myzoo = start_zoo()

    print("Huvudprogram: Skapar trådar.")
    # Skapa trådobjekt

    t1 = threading.Thread(target=run_zoo_simulation, name="Zoo business", args=(myzoo,))
    t2 = threading.Thread(target=input_listener, name="User input listener", args=(myzoo,))

    # Starta trådarna
    t1.start() # Anropar run_zoo_simulation
    t2.start() # Anropar input_listener
    

    print("Huvudprogram: Trådar är startade. Väntar på att de ska bli klara.")

    # Vänta på att båda trådarna ska slutföras
    t1.join()
    t2.join()

    print("Huvudprogram: Båda trådarna är färdiga. Programmet avslutas.")

  


