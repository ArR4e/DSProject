import string
import random

def suurväike(sõne):
        kvm = list(string.punctuation)
        asendus = random.choice(kvm)
        a = list(sõne)
        for char in a:
            if char in kvm:
                    a[a.index(char)] = asendus
                    uus = ''
            else:
                uus = ''
        uussõne = uus.join(a)
        return uussõne.swapcase()
