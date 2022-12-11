from turtle import*

def ruutude_fraktral(f):
    if f == 1:
        a = 200
        right(90)
        forward(a)
        right(90)
        forward(a)
        right(90)
        forward(a)
        right(90)
        forward(a)
        right(90)
    if f == 1:
        return 0
    else:
        if f > 1:
            f -= 1
            for i in range(4):
                forward(100)
                left(90)
                if i < 3:
                    for i in range(4):
                        forward(50)
                        left(90)
                        if i < 3:
                            for i in range(4):
                                forward(25)
                                left(90)
                                left(180)
                        left(180)
                left(180)
        return ruutude_fraktral(f)
    
ruutude_fraktral(2)
