#!/usr/bin/env python3

class Plant:
    nb_plants = 0

    def __init__(self, name: str, height: int):
        '''
        Initialize the Plant object by setting up the basic vairables,
        verifying that all inputs are valid
        '''
        if height < 0:
            print("Height should be a positive value")
            return
        self.name = name
        self.__height = height
        Plant.nb_plants += 1

    def set_height(self, h: int):
        '''
        Modifying the height if the new value is valid
        '''
        if h < 0:
            print(f"\nInvalid operation attempted: height {h}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = h

    def get_height(self):
        '''
        Returning the height in order to protect the direct variable access
        '''
        return self.__height

    def grow(self):
        self.set_height(self.get_height() + 1)
        print(f"{self.name} grew 1cm")

    def get_info(self):
        '''
        Return the state of the Plant
        '''
        return f"- {self.name}: {self.__height}cm"


class FloweringPlant(Plant):
    nb_flowering_plants = 0

    def __init__(self, name: str, height: int, color: str):
        '''
        Initialize the FloweringPlant object by using the Plant class
        '''
        super().__init__(name, height)
        self.color = color
        FloweringPlant.nb_flowering_plants += 1

    def get_info(self):
        '''
        Return the state of the Plant
        '''
        return f"{super().get_info()}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    nb_prize_flower = 0

    def __init__(self, name: str, height: int, color: str, points: int):
        '''
        Initialize the PrizeFlower object by using the FloweringPlant class
        '''
        super().__init__(name, height, color)
        self.points = points
        PrizeFlower.nb_prize_flower += 1

    def get_info(self):
        '''
        Return the state of the Plant
        '''
        return f"{super().get_info()}, Prize points: {self.points}"


class GardenManager:
    nb_gardens = 0
    total_growth = 0

    class GardenStats:

        @staticmethod
        def valid_height(height: int):
            return height > 0

    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []
        self.score = 0
        GardenManager.nb_gardens += 1

    def add_plant(self, plant: Plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all_plants(self):
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            GardenManager.total_growth += 1

    def display_plants(self):
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.get_info())

    def show_info(self):
        print(f"\n=== {self.owner}'s Garden Report ===")
        self.display_plants()

        print(f"\nPlants added: {len(self.plants)}, ", end="")
        print(f"Total growth: {GardenManager.total_growth}cm")
        print("Plant types: ", end="")

        r = Plant.nb_plants
        f = FloweringPlant.nb_flowering_plants
        p = PrizeFlower.nb_prize_flower

        print(f"{r - f} regular, ", end="")
        print(f"{f - p} flowering, ", end="")
        print(f"{p} prize flowers")

    def get_score(self):
        score = 0
        for plant in self.plants:
            score += plant.get_height()
        return score

    @classmethod
    def create_garden_network(cls, *gardens: "GardenManager") -> None:
        print("\nHeight validation test:")
        print("Garden scores -", end="")
        for k in range(len(gardens)):
            score = gardens[k].get_score()
            print(f" {gardens[k].owner}: {score}", end="")
            if k != len(gardens) - 1:
                print(",", end="")
        print("\nTotal gardens managed:", cls.nb_gardens)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice = GardenManager("Alice")
    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 25, "yellow", 10))

    alice.grow_all_plants()
    alice.show_info()
    GardenManager.create_garden_network(alice)
