import pandas
#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
ok = True
while ok:
    word = input("type a word: ")
    try:
        lst_code = [alphabet_dict[letter.upper()] for letter in word]
        print(lst_code)
        ok = False
    except KeyError:
        print("sorry, only letters in the alphabet please")
