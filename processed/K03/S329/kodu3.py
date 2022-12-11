print("Tere, kallis kasutaja")
print("Palun sisestage loomuliku numbri ja ma kuvan ekraanile õige vastuse.")
print("Õige vastuse all pean silmas esimese n naturaalarvu summa ruudu ja ruutude summa erinevust.")

n = int(input("Palun kirjutage naturaalarv: "))

def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

def square_of_sum(n):
    return sum(range(1, n+1)) ** 2

a = square_of_sum(n) - sum_of_squares(n)

print(a)