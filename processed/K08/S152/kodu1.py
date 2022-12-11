from random import sample
def bingo():
    list1 = sample(range(1,11),3)
    list2 = sample(range(11,21),2)
    tulemus= list1 + list2
   
    if 1 in list1 and 2 in list1 and 3 in list1:
        list1 = sample(range(1,11),3)  
        tulemus= list1 + list2   
    return(tulemus)
bingo()
    
    