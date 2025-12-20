#!/usr/bin/env python3

class Plant:
    nb_plants = 0

    def __init__(self, name: str, height: int, age: int):
        '''
        Initialize the Plant object by setting up the basic vairables
        '''
        self.name = name
        self.height = height
        self.date = age
        Plant.nb_plants += 1

    def grow(self):
        self.height += 1

    def age(self):
        self.date += 1

    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.date} days)")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        plant.get_info()
    print("\nTotal plants created: ", Plant.nb_plants)
