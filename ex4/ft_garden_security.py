#!/usr/bin/env python3

class SecurePlant:

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

    def plant_state(self):
        '''
        Print the current state of the Plant object
        '''
        start = f"Current plant: {self.name} "
        print(f"{start}({self.__height}cm, {self.__age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 15, 20)
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    plant.plant_state()
