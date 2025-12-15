# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: crappo <crappo@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/15 17:17:55 by crappo            #+#    #+#              #
#    Updated: 2025/12/15 17:53:37 by crappo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class SecurePlant:

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

	def plant_state(self):
		print(f"Current plant: {self.name} ({self.__height}cm, {self.__age} days)")

if __name__ == "__main__":
	print("=== Garden Security System ===")
	plant = SecurePlant("Rose", 15, 20)
	plant.set_height(25)
	plant.set_age(30)
	plant.set_height(-5)
	plant.plant_state()