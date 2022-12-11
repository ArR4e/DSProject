from random import randint
def minu_shuffle(arr):
    
    for i in range(len(arr)):
        juhuslik_arv=randint(0,len(arr)-1)
        arr[i],arr[juhuslik_arv]=arr[juhuslik_arv],arr[i]


