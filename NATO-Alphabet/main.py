import pandas

# TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for index, row in data.iterrows()}
#print(new_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_input():
    user_input = input("Put a word or something, you know\n").upper()
    try:
        user_nato = [new_dict[letter] for letter in user_input]
    except KeyError:
        print("Only letters in the field, please")
        generate_input()
    else:
        print(user_nato)
generate_input()