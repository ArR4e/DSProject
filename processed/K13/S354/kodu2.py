from turtle import *

def fun(n, p):
    if n >= 1:
        for i in range(4):
            forward(p)
            left(90)
            if i< 3:
                
                fun(n-1, p/2)
            left(180)
speed(0)
fun(2, 100)
            
#     pikkus=100/2**(n-1)
#     if n == 1:
#         for i in range(4):
#             forward(pikkus/2**(n-1))
#             left(90)

   
#     pikkus=100/2**(tase-1)
#     if tase >= 1:
#         forward(pikkus)
#         fun(tase-1)
#         left(90)
#         forward(pikkus)
#         fun(tase-1)
#         left(90)
#         forward(pikkus)
#         fun(tase-1)
#         left(90)














# def fun(tase):
#     pikkus = 100
#     if tase == 1 atased pikkus = 100:
#         for i itase ratasege(4):
#             forward(pikkus/2**(tase-1))
#             left(90)
#     else:
#         fun(1)
#         
        
        
        
            
#         for i itase ratasege(2):
#             forward(pikkus)
#             for i itase ratasege(4):
#                 forward(pikkus/2**(tase))
#                 right(90)
#             
#             left(90)
#         forward(pikkus)
#         left(90)
#         
#         
#         
# # def fraktal(tase, pikkus):
#     if tase == 1:
#         forward(pikkus)
#         backward(pikkus)
#     else:
#         forward(pikkus)
#         left(90)
#         fraktal(tase-1, pikkus * 0.7)
#         right(180)
#         fraktal(tase-1, pikkus * 0.7)
#         left(90)
#         backward(pikkus)