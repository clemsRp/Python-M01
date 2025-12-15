# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: crappo <crappo@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/15 11:44:32 by crappo            #+#    #+#              #
#    Updated: 2025/12/15 11:56:18 by crappo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:

	def __init__(self, name: str, height: int, age: int):
		self.name = name
		self.height = height
		self.age = age

	def print_plant(self):
		print(f"{self.name}: {self.height}cm, {self.age} days old")

if __nane__ == "__main__":
	plant1 = Plant("Rose", 25, 30)
	plant2 = Plant("Sunflower", 80, 45)
	plant3 = Plant("Cactus", 15, 120)
	plant1.print_plant()
	plant2.print_plant()
	plant3.print_plant()