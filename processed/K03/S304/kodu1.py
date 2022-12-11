a = float(input("sisesta aastatulu: "))
b = float(6000 - 6000/10800*(a - 14400))
c = round(b,2)

if a < 6000:
    print(f"Maksuvaba tulu on, {a} eurot.")
elif a < 14400:
    print("Maksuvaba tulu on 6000 eurot.")
elif a <= 25200:
    print(f"Maksuvaba tulu on, {c} eurot.")
elif a > 25200:
    print("Maksuvaba tulu on 0 eurot.")

    
