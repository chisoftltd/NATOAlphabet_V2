import pandas

# TODO 1. Create a dictionary in this format:
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data_list = {row.letter: row.code for (index, row) in nato_data.iterrows()}
print(nato_data_list)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
game_on = True
while game_on:
    try:
        user_word = input("Enter a word: ").upper()
        user_nato_list = [nato_data_list[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(user_nato_list)
    finally:
        more_word = input("More word? 'y' or 'n' ").lower()
        if more_word == "n":
            print("Thank you, bye!")
            game_on = False
