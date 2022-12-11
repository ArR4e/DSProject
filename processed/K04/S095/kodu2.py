while True:
    u=input("Sisesta u: ")
    v=input("Sisesta v: ")
    x=input("Sisesta x: ")
    y=input("Sisesta y: ")
    c=float(299792.458)
    if u and v != "":
        break
def summa(u, v):
    esimene_ja_teine = (float(u)+float(v))/(1+((float(u))*(float(v)))/(c**2))
    see_ja_kolmas = (esimene_ja_teine+float(x))/(1+((esimene_ja_teine)*(float(x)))/(c**2))
    see_ja_neljas = (see_ja_kolmas+float(y))/(1+((see_ja_kolmas)*(float(y)))/(c**2))
    return see_ja_neljas

print("Kiiruste summa on", summa(u, v), "km/s")