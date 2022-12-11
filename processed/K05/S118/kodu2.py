import random
import string

def suurväike(sõne):
    tagastatav = ""
    asendus = string.punctuation[random.randint(0, 31)]
    for märk in sõne:
        if märk.isalpha():
            if märk.isupper():
                tagastatav+=märk.lower()
            else:
                tagastatav+=märk.capitalize()
        elif märk.isdigit():
            tagastatav+=märk
        elif märk == " ":
            tagastatav+=" "
        else:
            tagastatav+=asendus
    return tagastatav
