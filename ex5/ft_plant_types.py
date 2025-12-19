#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: int, age: int):
        '''
        Initialize the Plant object by setting up the basic vairables,
        verifying that all inputs are valids
        '''
        assert height >= 0, "Height should be a positive value"
        assert age >= 0, "Age should be a positive value"
        self.name = name
        self.__height = height
        self.__age = age
        print("Plant created:", self.name)

    def set_height(self, h: int):
        '''
        Modifying the height if the new value is valid
        '''
        if h < 0:
            print(f"\nInvalid operation attempted: height {h}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = h
            print(f"Height updated: {self.__height}cm [OK]")

    def get_height(self):
        '''
        Returning the height in order to protect the direct variable access
        '''
        return self.__height

    def set_age(self, age: int):
        '''
        Modifying the age if the new value is valid
        '''
        if age < 0:
            print(f"\nInvalid operation attempted: age {age}cm [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = age
            print(f"Age updated: {self.__age}cm [OK]")

    def get_age(self):
        '''
        Returning the age in order to protect the direct variable access
        '''
        return self.__age

    def get_info(self, plant_type: str):
        '''
        Return the state of the Plant
        '''
        start = f"{self.name} ({plant_type}):"
        return f"{start} {self.__height}cm, {self.__age} days,"


class Flower(Plant):

    def __init__(self, name: str, height: int, age: int, color: str):
        '''
        Initialize the Flower object by using the Plant class
        '''
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        '''
        Simulate the Flower bloom
        '''
        print(self.name, " is blooming beautifully!\n")

    def print_info(self):
        '''
        Print datas about the Flower object
        '''
        print(self.get_info("Flower"), f"{self.color} color")
        self.bloom()


class Tree(Plant):

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        '''
        Initialize the Tree object by using the Plant class
        '''
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        '''
        Simulate the Tree shade
        '''
        area = 5 * self.trunk_diameter * self.get_height()
        print(self.name, f"provides {area} square meters of shade\n")

    def print_info(self):
        '''
        Print datas about the Tree object
        '''
        print(self.get_info("Tree"), f"{self.trunk_diameter} diameter")
        self.produce_shade()


class Vegetable(Plant):

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        '''
        Initialize the Vegetable object by using the Plant class
        '''
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def print_info(self):
        '''
        Print datas about the Vegetable object
        '''
        print(self.get_info("Vegetable"), f"{self.harvest_season} season")
        print(f"{self.name} is rich in vitamin {self.nutritional_value}\n")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    f1 = Flower("Tulipe", 25, 15, "red")
    f2 = Flower("Rose", 15, 30, "white")
    t1 = Tree("Chene", 12, 5491, 2000)
    t2 = Tree("Pommier", 2, 1643, 30)
    v1 = Vegetable("Carotte", 20, 156, "automne", "B6")
    v2 = Vegetable("Pomme de terre", 17, 94, "été", "C")

    f1.print_info()
    t1.print_info()
    v1.print_info()
