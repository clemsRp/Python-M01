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


class Factory:

    def __init__(self):
        self.plants = []
        self.nb_plants = 0

    def add_plants(self, plants: list):
        try:
            for plant in plants:
                self.plants.append(Plant(plant[0], plant[1], plant[2]))
                self.nb_plants += 1
        except Exception as e:
            print("Error:", e)

    def get_infos(self):
        for plant in self.plants:
            plant.get_info()


if __name__ == "__main__":
    plants = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    factory = Factory()
    factory.add_plants(plants)
    factory.get_infos()

    print("\nTotal plants created: ", Plant.nb_plants)
