list1 = [2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]
def rek_abs(list1, summa):
    if isinstance(list1, list) == False:
        summatemp = 0
        for i in list1:
            summatemp += 1
    else:
        summatemp = 0
        for i in list1:
            summatemp += 1
        rek_abs(list1,(summa + summatemp))
        
        
def factorial(list1):
    summa = 0
    return rek_abs(list1, summa)

print(factorial(list1))