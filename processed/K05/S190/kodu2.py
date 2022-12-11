import string
import random

def suurväike(sisend):
    tähtede_vahetus = sisend.swapcase()
    
    märk = random.choice(string.punctuation)
    
    for i in tähtede_vahetus:
        if i in string.punctuation:
            tähtede_vahetus = tähtede_vahetus.replace(i,märk)
        
    return(tähtede_vahetus)
        

sisend = input("Sisesta mingi fraas, kasutades suuri-väikseid tähti ning kirjavahemärke: ")


print(suurväike(sisend))


