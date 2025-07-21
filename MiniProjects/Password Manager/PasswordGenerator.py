import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = 12
nr_number = 4
nr_symbols = 4

random_letters=[random.choice(letters) for _ in range(nr_letters)]
random_numbers=[random.choice(numbers) for _ in range(nr_number)]
random_symbols=[random.choice(symbols) for item in range(nr_symbols)]

password=[]

def generate_password():
    password.extend(random_letters)
    password.extend(random_numbers)
    password.extend(random_symbols)
    random.shuffle(password)

    final_password = ''.join(password)
    return final_password