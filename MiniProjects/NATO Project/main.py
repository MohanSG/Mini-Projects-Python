import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index,row) in nato_df.iterrows()}

word = ''
while word != "exit":
    word = input("Choose a word: ").upper()
    try:
        word_list = [word_letter for word_letter in word]
        nato_list = [nato_dict[letter] for letter in word_list]
    except KeyError:
        print("Please type in a valid word")
    else:
        print(nato_list)

