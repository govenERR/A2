from typing import Dict, Optional
from computer import Computer
class ResaleShop:
    """Creates an instance of the resale shop class
        Allows you to add and remove things from the inventory, display the inventory, and change things like the price, operating system, and refurbish the machine 
    """
    def __init__(self):
        self.inventory = []
    #creates list of inventory
    
    """Adds a new computer object to the inventory list
    """
    def buy(self, computer : Computer):
        self.inventory.append(computer)
        

    """Removes a computer object from the list
    """
    def sell(self, computer):
        if computer in self.inventory:
            self.inventory.pop(self.inventory.index(computer))
        else:
            print("This computer is not avaliable")
    
    """Prints all of the computers in the inventory as well as information about them
    """
    def display(self):
        n = 1
        if self.inventory[0] != None:
            for computer in self.inventory:
                print(n, computer.stringInfo())
                n += 1
        else:
            print("No inventory to display")

    """Changes the price of an object, tells you that can't happen if it's not in the inventory
    """
    def updatePrice(self, description, newPrice):
        change = False
        for computer in self.inventory:
            if description == computer.description:
                computer.price = newPrice
                print("Price of", description, "is now", newPrice)
                change = True
        if change == False:
            print(description, "is not in our inventory")
    
    """Changes the value of the computer according to how old it is, and optionally updates the OS
    """
    def refurbish(self, description, newOS : Optional[str]):
        for computer in self.inventory:
            if description == computer.description:
                if self.year_made < 2000:
                    self.price = 0
                elif self.year_made < 2012:
                    self.price = 250
                elif self.year_made < 2018:
                    self.price = 550
                else:
                    self.price = 1000
                if newOS != None:
                    self.operating_system = newOS
                    
        

def main():
    c1 = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
    c2 = Computer("Microsoft Surface Pro", "Qualcomm Snapdragon X Plus", 512, 16, "Windows 11", 2024, 1349)
    resaleShop = ResaleShop()
    resaleShop.buy(c1)
    resaleShop.buy(c2)
    print(resaleShop.inventory)
    resaleShop.sell(c1)
    print(resaleShop.inventory)
    resaleShop.display()
    resaleShop.updatePrice("Microsoft Surface Pro", 999)



if __name__ == "__main__": main()
