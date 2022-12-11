from turtle import *
def hulknurk(n, a):
    if n > 2:
        for x in range(n):
            forward(a)
            right(360/n)
    else:
        print('Sisestage vähemalt 3 nurka.')

n = int(input('Sisesta hulknurga külgede arv: '))
a = int(input('Sisesta hulknurga külje pikkus: '))
hulknurk(n, a)
    
    
    
    