from random import randint

def minu_shuffle(järjend):
    for i in range(len(järjend)-1,0,-1):
        juhuslik = randint(0, i+1)
        järjend[i], järjend[juhuslik] = järjend[juhuslik], järjend[i]
    print(järjend)
        

    
minu_shuffle([1, 3, 3, 4, 5, 5, 5, 6, 6])

# kasutasin infot sellelt lehelt: https://stackoverflow.com/questions/17489477/shuffle-a-python-list-without-using-the-built-in-function