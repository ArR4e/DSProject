import string
import random

def suurväike(sõne):
    kvm1 = string.punctuation
    kvm2 = random.randint(1, len(kvm1))
    for i in sõne:
        if i in kvm1:
            sõne = sõne.replace(i, kvm1[kvm2])
    return sõne.swapcase()