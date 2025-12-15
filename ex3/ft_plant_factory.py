# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: crappo <crappo@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/15 12:55:05 by crappo            #+#    #+#              #
#    Updated: 2025/12/15 17:17:32 by crappo           ###   ########.fr        #
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
	print("\nTotal plants created: ", len(plants))