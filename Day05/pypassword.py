import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] 
print("welcome to password generator app")
number_of_letters=int(input("How many characters would you like in your passowrd ?"))
number_of_numbers=int(input("How many numbers would you like in your passowrd ?"))
number_of_symbols=int(input("How many symbols would you like in your passowrd ?"))
random_alphabets = random.sample(alphabets, (number_of_letters-number_of_numbers)-number_of_symbols)
# print(random_alphabets)
random_numbers = random.sample(numbers, number_of_numbers)
# print(random_numbers)
random_symbols = random.sample(symbols, number_of_symbols)
# print(random_symbols)
combined_random_letters = random_alphabets + random_numbers + random_symbols
print(combined_random_letters)
final_password = random.sample(combined_random_letters, len(combined_random_letters))
final_string_password = "".join(final_password)
print(f"Your password is : {final_string_password}")
