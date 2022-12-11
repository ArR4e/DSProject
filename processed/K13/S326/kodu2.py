import turtle as t

def fraktal(sugavus, suurus):
    if sugavus == 0:
        pass
    else:
        for i in range(4):
            t.fd(suurus)
            t.right(90)
        t.fd(suurus)
        fraktal(sugavus - 1, suurus / 3)
    t.exitonclick()
fraktal(5, 200)