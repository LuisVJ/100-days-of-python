student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create dictionary
alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter:row.code for (index, row) in alphabet_data.iterrows()}

# Ask for word and return code list
while(True):
    word = input("Enter a word: ").upper()
    try:
        code_list = [alpha_dict[letter] for letter in word]
    except KeyError as char:
        print(f"Sorry, only letters in the alphabet please. {char} is not a valid letter")
    else:
        break

print(code_list)

