letter = ""
letter_list = []

with open('./Input/Letters/starting_letter.txt') as file:
    letter = file.read()
    
with open('./Input/Names/invited_names.txt') as file:
    for line in file.readlines():
        name = line.replace("\n", '')
        ready_letter = letter.replace("[name]", name)
        
        with open(f"./Output/ReadyToSend/{name}'s letter", "w") as new_letter:
            new_letter.write(ready_letter)