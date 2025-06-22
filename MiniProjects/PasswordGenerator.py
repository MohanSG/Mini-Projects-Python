import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How many letters would you like?"))
nr_number = int(input("How many numbers would you like?"))
nr_symbols = int(input("How many symbols would you like?"))

random_letters=[]
random_numbers=[]
random_symbols=[]
password=[]

for letter in range(1, nr_letters+1):
    random_letters.append(letters[random.randint(0, len(letters)-1)])

for number in range(1, nr_number+1):
    random_numbers.append(numbers[random.randint(0, len(numbers)-1)])

for symbol in range(1, nr_symbols):
    random_symbols.append(symbols[random.randint(0, len(symbols)-1)])

password.extend(random_letters)
password.extend(random_numbers)
password.extend(random_symbols)
random.shuffle(password)

final_password = ''.join(password)
print(final_password)