import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index,row) in nato_df.iterrows()}

word = input("Choose a word: ").upper()
word_list = [word_letter for word_letter in word]
nato_list = [nato_dict[letter] for letter in word_list]

print(nato_list)

