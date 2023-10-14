import pandas
#TODO 1. Create a dictionary in this format:

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    user_input = input("Enter a name: ").upper()
    try:
        user_list = [nato_dict[character] for character in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(user_list)


generate_phonetic()
