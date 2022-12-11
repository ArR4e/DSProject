# u ja v kiiruste summa valem Einsteini erirelatiivsusteooriast
def summa(u, v):
    return (u + v) / (1 + ((u * v) / (299792.458**2)))

# küsib kasutajalt 4 kiirust
u = float(input("Sisesta 1. kiirus "))
v = float(input("Sisesta 2. kiirus "))
x = float(input("Sisesta 3. kiirus "))
y = float(input("Sisesta 4. kiirus "))

# leiab 4 kiiruse summa kasutades summa()
kiirus = summa(summa(summa(u, v), x), y)
print("Kiiruste summa on", kiirus)
    