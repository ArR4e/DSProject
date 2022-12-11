from turtle import *

def fraktal(n, pikkus):
    #if n//2 == 0:
        if n == 0:
            return
        if n == 1:
            forward(pikkus)
            left(90)
            forward(pikkus)
            left(90)
            forward(pikkus)
            left(90)
            forward(pikkus)
        if n > 1:
            forward(pikkus)
            fraktal(n-1, 0.5*pikkus)
            forward(pikkus)
            fraktal(n-1, 0.5*pikkus)
            forward(pikkus)
            fraktal(n-1, 0.5*pikkus)
            forward(pikkus)
#     if n//2 == 1:
#         if n == 0:
#             return
#         if n == 1:
#             forward(pikkus)
#             right(90)
#             forward(pikkus)
#             right(90)
#             forward(pikkus)
#             right(90)
#             forward(pikkus)
#         if n > 1:
#             forward(pikkus)
#             fraktal(n-1, 0.5*pikkus)
#             forward(pikkus)
#             fraktal(n-1, 0.5*pikkus)
#             forward(pikkus)
#             fraktal(n-1, 0.5*pikkus)
#             forward(pikkus)
        
fraktal(3,100)