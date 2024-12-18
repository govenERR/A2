class Computer:
    """ The computer class stores information for all of the computers in the resale store. 
        This is also where methods to change a computer directly are.
    """
    def __init__(self, description:str, processor_type:str, hard_drive_capacity:int, memory:int, operating_system:str, year_made:int, price:int):
        #creates computer class
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    # What methods will you need?
    """Sets a new price directly to the class
    """
    def setPrice(self, newPrice: int):
        self.price = newPrice
    """Changes the OS directly in the class
    """
    def setOS(self, newOS: int):
        self.operating_system = newOS
    """Creates converts all of the attributes into strings, so that the resale shop can easily print them in the display() method
    """
    def stringInfo(self):
        return "description:", str(self.description), "processor type:", str(self.processor_type), "hard drive capacity:", str(self.hard_drive_capacity) , "memory:", str(self.memory), "os:", str(self.operating_system), "year:", str(self.year_made), "price:", str(self.price)
        
def main():
    computer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 99)
    print(computer.price)
    computer.setPrice(12)
    print(computer.price)


main()
