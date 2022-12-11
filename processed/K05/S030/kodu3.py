#fn moos küsib a-5kg karpide arvu, b-1kg karpide arvu, c-moosi kogust
def moos(a, b, c):
    s=0
    while a==0:
        if (c>=5 and a>=1):
            c=c-5
            a-=1
            s+=1
            if c==0:
                break
        else:
            while b==0:
                if (b>=c):
                    c=c-1
                    s+=1
                    b-=1
                    if c==0:
                        break
    print(s)