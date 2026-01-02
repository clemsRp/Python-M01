#!/usr/bin/env python3

class Plant:
    '''
    Simulate the behaviour of a plant
    '''
    nb_plants = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        '''
        Initialize the Plant object by setting up the basic vairables
        '''
        self.name = name
        self.height = height
        self.date = age
        Plant.nb_plants += 1

    def grow(self) -> None:
        '''
        Simulate the growth of a plant increasing her height
        '''
        self.height += 1

    def age(self) -> None:
        '''
        Simulate the ages of a plant increasing the date
        '''
        self.date += 1

    def get_info(self) -> None:
        '''
        Display some information about the plant
        '''
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
