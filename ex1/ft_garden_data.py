#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: int, age: int):
        '''
        Initialize the Plant object by setting up the basic vairables
        '''
        self.name = name
        self.height = height
        self.age = age

    def print_plant(self):
        '''
        Print some datas about the Plant obect state
        '''
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===\n")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    plant1.print_plant()
    plant2.print_plant()
    plant3.print_plant()
