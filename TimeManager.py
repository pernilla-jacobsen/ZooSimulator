import MyClasses

""" Jag vill ha en Tid hanterare som ger klockslag över en dag. """
class TimeManager:
    def __init__(self, start_time=6):
        self.current_time = start_time  # Start at early morning (6:00 hours)
    
    def advance_time(self, hours):
        self.current_time = (self.current_time + hours) % 24  # Wrap around after 24 hours
    
    def get_current_time(self):
        return self.current_time
    
if __name__ == "__main__":
    time_manager = TimeManager()
    print(f"Current Time: {time_manager.get_current_time()} hours")

    myzoo = MyClasses.Zoo("Little Zoo")

    leo = MyClasses.Lion("Leo", 5)  
    simba = MyClasses.Lion("Simba", 4)
    ella = MyClasses.Elephant("Ella", 10)
    ollie = MyClasses.Elephant("Ollie", 8)  
    bill = MyClasses.Chimpanzee("Bill", 3)
    bob = MyClasses.Chimpanzee("Bob", 4)

    myzoo.add_animal(leo)
    myzoo.add_animal(ella)  
    myzoo.add_animal(bill)
    myzoo.add_animal(simba)
    myzoo.add_animal(ollie)     
    myzoo.add_animal(bob)

    visitor1 = MyClasses.Visitor("Alice", 28)  
    visitor2 = MyClasses.Visitor("Bob", 35)
    visitor3 = MyClasses.Visitor("Charlie", 10)
    visitor4 = MyClasses.Visitor("Diana", 22)  



    for _ in range(18):
        time_manager.advance_time(0.5) # Advance time by 30 minutes
        print(f"Advanced Time: {time_manager.get_current_time()} hours")
        
        if time_manager.get_current_time() == 10.0:
            myzoo.welcome_visitor(visitor1)
        if time_manager.get_current_time() == 12.0:
            myzoo.welcome_visitor(visitor2)
        if time_manager.get_current_time() == 11.0:
            myzoo.welcome_visitor(visitor3)
            myzoo.welcome_visitor(visitor4)
      
        myzoo.current_time(time_manager.get_current_time())