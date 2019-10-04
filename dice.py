# Ozarrian John
# Block 1
# Dice Rolling Simulator

import random

numRolls = int(input("Enter the amount of rolls: "))

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
rollNum = 1
while rollNum <= numRolls:
	print("Total Rolls: " + str(numRolls))
	randomNum = random.randint(1, 6) 
	if randomNum == 1:
		print("Roll number: " + str(randomNum))
	if randomNum == 2:
		print("Roll number: " + str(randomNum))
	if randomNum == 3:
		print("Roll number: " + str(randomNum))
	if randomNum == 4:
		print("Roll number: " + str(randomNum))
	if randomNum == 5:
		print("Roll number: " + str(randomNum))
	if randomNum == 6:
		print("Roll number: " + str(randomNum))
	break