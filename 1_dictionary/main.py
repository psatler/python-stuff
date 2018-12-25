import json
# This is a python library for 'Text Processing Services', as the offcial site suggests.
import difflib
from difflib import get_close_matches

# loading as a python dictionary
data = json.load(open("dictionary.json"))
print(type(data))

def retrieve_definition(word):
    word = word.lower() # to lower case

    if word in data:
        return data[word]
    elif word.title() in data: # To make sure the program return the definition of words that start with a capital letter (e.g. Delhi, Texas)
        return data[word.title()]
    elif word.upper() in data: # To make sure the program return the definition of acronyms (e.g. USA, NATO)
        return data[word.upper()]
    #3rd elif: To find a similar word
    #-- len > 0 because we can print only when the word has 1 or more close matches
    #-- In the return statement, the last [0] represents the first element from the list of close matches
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean %s instead? " % get_close_matches(word, data.keys())[0])
        if (action == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action == "n"):
            return ("The word doesn't exist, yet.")
        else:
            return ("We don't understand your entry. Apologies. You should answer either y or n")
    else:
        return ("The word doesn’t exist, please double check it.")

# input from user
word_user = input("Enter a word: ")

# retrieve definition
output = retrieve_definition(word_user)
#If a word has more than one definition, print them recursively
if type(output) == list:
    for item in output:
        print("-",item)
#For words having single definition
else:
    print("-",output)