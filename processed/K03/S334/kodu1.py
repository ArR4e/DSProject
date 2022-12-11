atulu = float(input("Sisesta aastatulu: " ))
mt = 0

if atulu <= 6000:
    mt = atulu
elif atulu > 6000 and atulu <= 14400:
    mt = 6000 
elif atulu > 14400 and atulu <= 25200:
    mt = 6000 - 6000 / 10800 * (atulu - 14400)
elif atulu > 25200:
    mt = 0
print(f"Maksuvaba tulu on {round(mt, 2)} eurot.")

