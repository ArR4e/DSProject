palk=float(input("Palk"))
if palk>25200:
    vastus=0
elif palk>14400:
    vastus=6000-6000/10800*(palk-14400)
elif palk>6000:
    vastus=6000
elif palk<=6000:
    vastus=palk
print(round(vastus, 2))