# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: clement <clement@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/16 15:24:47 by clement           #+#    #+#              #
#    Updated: 2025/12/16 18:11:09 by clement          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:

	def __init__(self, name, height, age):
		assert height >= 0, "Height should be a positive value"
		assert age >= 0, "Age should be a positive value"
		self.name = name
		self.__height = height
		self.__age = age
		print(f"Plant created:", self.name)

	def set_height(self, height):
		if height < 0:
			print(f"\nInvalid operation attempted: height {height}cm [REJECTED]\nSecurity: Negative height rejected\n")
		else:
			self.__height = height
			print(f"Height updated: {self.__height}cm [OK]")

	def get_height(self):
		return self.__height

	def set_age(self, age):
		if age < 0:
			print(f"\nInvalid operation attempted: age {age}cm [REJECTED]\nSecurity: Negative age rejected\n")
		else:
			self.__age = age
			print(f"Age updated: {self.__age}cm [OK]")

	def get_age(self):
		return self.__age

class Flower(Plant):

	def __init__(self, name, height, age, color):
		super().__init__(name, height, age)
		self.color = color

	def bloom(self):
		print(self.name, " is blooming beautifully!")

class Tree(Plant):
	


if __name__ == "__main__":
    pass