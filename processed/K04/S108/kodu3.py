def hulknurk(n,l):
    import turtle
    tt=turtle.Turtle()
    joonistusala=turtle.Screen()
    joonistusala.setup(width=350,height=350)
    for a in range(n):
        tt.forward(l)
        tt.right(360/n)
    turtle.done()

ns=int(input("Sisesta külgede arv: "))
ls=int(input("Sisesta külje pikkus: "))

hulknurk(ns,ls)