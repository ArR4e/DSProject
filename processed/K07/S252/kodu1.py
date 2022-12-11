sisend = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']
def poisse_ja_tüdrukuid(sisend):
    countT = 0
    countP = 0
    for tmp in sisend:
        arr = tmp.split(" ")
        if(arr[len(arr)-1] == "T"):
            countT += 1
        elif(arr[len(arr)-1]== "P"):
            countP += 1
        return (countP,countT)
    
result= poisse_ja_tüdrukuid(sisend)
print(result)
    