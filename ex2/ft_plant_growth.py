# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: crappo <crappo@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/15 11:50:39 by crappo            #+#    #+#              #
#    Updated: 2025/12/15 12:54:25 by crappo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:

	def __init__(self, name: str, height: int, age: int):
		self.name = name
		self.height = height
		self.date = age

	def grow(self):
		self.height += 1

	def age(self):
		self.date += 1

	def get_info(self):
		print(f"{self.name}: {self.height}cm, {self.date} days old")

if __name__ == "__main__":
	diff = 0
	plant1 = Plant("Rose", 25, 30)
	plant2 = Plant("Sunflower", 80, 45)
	plant3 = Plant("Cactus", 15, 120)
	plants = [plant1, plant2, plant3]
	print("=== Day 1 ===")
	plant1.get_info()
	for k in range(6):
		diff += 1
		for plant in plants:
			plant.grow()
			plant.age()
	print("=== Day 7 ===")
	plant1.get_info()
	print(f"Growth this week: +{diff}cm")
