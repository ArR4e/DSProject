with open("kinganumbrid.txt") as f:
    numbers=f.readlines()
def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

for number in numbers:
    if is_number(number) == True:
        f = float(number)
        pik = 2/3*(f-2)
        print(round(pik))
    else:
        print("Vigane sisend")