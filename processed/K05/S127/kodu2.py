import string
from random import choice
def suurväike(s):
    suvaline="join(random.choises(string.punctuation, k=1)"
    return s.swapcase().replace('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', suvaline)
print(suurväike("MdsaMFSKA!%&()dfafMsfk"))

#ei oska asendada