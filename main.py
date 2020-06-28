import json
from difflib import get_close_matches as gcm

data = json.load(open("data.json"))

def find_meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()] 
    else:
        matches = gcm(word,data.keys())
        if len(matches) > 0:
            return "Did you mean " + str(matches[0]) + " instead"
        else:
            return "Word Not Found"

search_word = input("Enter the word to search: ")

meaning = find_meaning(search_word)
if type(meaning) == list:
    for m in meaning:
        print(m + "\n")
else:
    print(meaning)
