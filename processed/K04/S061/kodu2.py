esimene = float(input("Esimese keha kiirus vaatleja suhtes on:"))
teine = float(input("Teise keha kiirus esimese keha suhtes on:"))
kolmas = float(input("Kolmanda keha kiirus teise keha suhtes on:"))
neljas = float(input("Neljanda keha kiirus kolmanda keha suhtes on:"))
c = 299792.458
def summa(u, v):
    lugeja_uv = u + v
    nimetaja_uv = 1 + u * v / c**2
    uvsumma = lugeja_uv / nimetaja_uv
    return uvsumma

e_t = summa(esimene, teine)
e_t_k = summa(e_t, kolmas)
e_t_k_n = summa(e_t_k, neljas)

print("Kiiruste summa on", str(e_t_k_n), "km/s.")