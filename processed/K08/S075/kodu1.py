from random import sample
def bingo():
    numbrid=[]
    numbrid+=sample(range(1,11),3)+sample(range(11,21),2)
    while numbrid[0]==1 or numbrid[0]==2 or numbrid[0]==3:
        if numbrid[1]==1 or numbrid[1]==2 or numbrid[1]==3:
            if numbrid[2]==1 or numbrid[2]==2 or numbrid[2]==3:
                numbrid=[]
                numbrid+=sample(range(1,10),3)+sample(range(11,20),2)
            else:
                break
        else:
            break
    return numbrid
    
print(bingo())