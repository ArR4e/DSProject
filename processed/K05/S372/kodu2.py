import random
import string
def suurväike(sõne):
    vahetus = ""
    kirjavahemärk = str(random.choice(string.punctuation))
    for täht in sõne:
        if täht.isupper() == True:
            vahetus += täht.lower()
        elif täht in string.punctuation:
            vahetus += kirjavahemärk
        else:
            vahetus += täht.upper()
    return vahetus
