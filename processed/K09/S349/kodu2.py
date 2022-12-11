järjend = [1,2,3,4,5,6,7,8,9,10]
import random

def minu_shuffle(järjend):
    print(f"Originaal list on: {järjend}.")
    for i in range(len(järjend)-1, 0, -1):
        indeks = random.randint(0, i+1)
        järjend[i], järjend[indeks] = järjend[indeks], järjend[i]
    print(f"Sassi aetud list on: {str(järjend)}.")
        
        
minu_shuffle(järjend)