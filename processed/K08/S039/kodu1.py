from random import sample, randint

def bingo():
    numbrid=[]
    #for nr in range(2):
    väike_nr=sample(range(1,4),1)
    keskmine_nr=sample(range(4,11),2)
    #for nr in range(2):
    #    uus_nr=randint(4,10)
    #    keskmine_nr+=[uus_nr]
    suur_nr=sample(range(11,21),2)
    numbrid=numbrid+väike_nr+keskmine_nr+suur_nr
    return numbrid
print(bingo())    
