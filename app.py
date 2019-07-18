import json
from difflib import get_close_matches

data = json.load(open('data.json'))
valve = "--------------------------------------------------"


def translate(w):
    try:
        if w in data:
            for list in data[w]:
                print(list)
            print(valve)
            return ""
        elif w.title() in data:
            for list in data[w.title()]:
                print(list)
            print(valve)
            return ""
        elif w.upper() in data:
            for list in data[w.upper()]:
                print(list)
            print(valve)
            return ""
        elif len(get_close_matches(w, data.keys())) > 0:
            v = get_close_matches(w, data.keys(), cutoff=0.8)[0]
            re_input = input(f"The word doesen't exist. Do you mean to say '{v.upper()}' word. Enter Y / N to continue: ").lower()
            if re_input == 'y' or re_input == 'yes':
                print(valve)
                for list in data[v]:
                    print(list)
                print(valve)
                return ""
            else:
                return "We didn't understand the word you entered."
        else:
            return f"'{w}' doesen't exist in out dictionary."
    except:
        return f"'{w}' doesen't exist in out dictionary."


print(valve)
word = input("Enter the word: ").lower()

print(translate(word))

