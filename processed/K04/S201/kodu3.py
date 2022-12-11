n = int(input('Sisesta külgede arv: '))
a = int(input('Sisesta külje pikkus: '))
b = 180-((n-2)*180)/n
from turtle import *
import turtle
for x in range(n):
    forward(a)
    left(b)
