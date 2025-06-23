from cipherart import art

def caesar(encode_or_decode, original_text, shift_amount):
    output_text = ''

    if encode_or_decode == "decode":
        shift_amount *= -1
        
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:  
            new_position = alphabet.index(letter) + shift_amount
            new_position %= len(alphabet)
            output_text += alphabet[new_position]
        
    print(f"Here is the {encode_or_decode}d result: {output_text} \n")

not_finished = True
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
print(art)

while not_finished:
    direction = input("\nWould you like to encode or decode?\n").lower()
    text = input(f"Type in the text you would like to {direction}\n").lower()
    shift = int(input("Type in your shift number\n"))
    caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)

    again = input("Type 'yes' to go again. Otherwise, type 'no': ").lower()
    if again == "no":
        not_finished = False