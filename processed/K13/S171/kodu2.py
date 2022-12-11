from turtle import*
def joonista(n):
    length = 100
    depth = n
    ruut(depth, length)

def ruut(n,a):
    fd(a)
    if n > 1:
        for i in range(3):
            ruut(n-1,a/2)
            fd(a)

    else:
            right(90)
            fd(a)
            right(90)
            fd(a)
            right(90)
            fd(a)




speed('fastest')
joonista(5)
exitonclick()