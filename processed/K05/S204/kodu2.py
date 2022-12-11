import string
import random


a=str(input("Palun sisesta suvaline sõne:"))
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
result_str = (random.choice('''!()-[]{};:'"\,<>./?@#$%^&*_~'''))


def suurväike(a):
    for i in a:       
        if i not in punctuation:   
        
            if i.islower():
                print(i.upper(),end="")
                
        
            elif i.isupper():
                print (i.lower(),end="")
                
            
        else:
            
            if i in punctuation:
                print(result_str,end="")
                
            
            
            

suurväike(a)