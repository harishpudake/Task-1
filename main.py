# #### Password Strength Checker ####

import string
from visual import *

def strength(parameters):
	minimum = [8, 1, 1, 1, 1]
	scores = [5, 2, 1, 1, 1]
	for i in range(5):
		if parameters[i] < minimum[i]:
			scores[i] = 0

	if sum(scores) == 10:
		print("Your password strength score is 10 out of 10.")
		print("Your password is safe and strong!")
	else:
		print(f"Your password strength score is {sum(scores)} out of 10.")
		print("Following is the breakdown of your password strength:\n")
		load_details(parameters)



def check(password):
	special_character = set(string.punctuation)
	special = sum(1 for char in password if char in special_character)
	length = len(password)
	uppercase = sum(1 for char in password if char.isupper())
	lowercase = sum(1 for char in password if char.islower())
	digits = sum(1 for char in password if char.isdigit())
	parameters = [length, special, uppercase, lowercase, digits]
	strength(parameters)



# Start
load_logo()
load_animation("starting your application...")

password = input("Enter your password: ")

load_logo()
load_animation("determining password strength...")
check(password)

print("\n\nThank you for using my 'Password Strength Checker Tool'!")
