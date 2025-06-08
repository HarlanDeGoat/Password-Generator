import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the my Password Generator!\n")
no_l = int(input("How many letters would you like in your password?\n"))
no_s = int(input(f"How many symbols would you like?\n"))
no_n = int(input(f"How many numbers would you like?\n"))


p_list = []
for char in range(0, no_l):
    p_list.append(random.choice(letters))

for char in range(0, no_s):
    p_list.append(random.choice(symbols))

for char in range(0, no_n):
    p_list.append(random.choice(numbers))

print(p_list)
random.shuffle(p_list)

password = ""
for char in p_list:
    password += char

print(f"Your password is: {password}")

