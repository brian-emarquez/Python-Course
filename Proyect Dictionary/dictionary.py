import json
from difflib import get_close_matches

data = json.load(open("Proyect Dictionary/data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("pugger tus pasos con las teclas equivocadas")
        else:
            return("ha ingresado una entrada incorrecta, ingrese solo y o n")
    else:
        print("pugger tus pasos con las teclas equivocadas")



word = input("Ingrese la palabra que desea buscar: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
