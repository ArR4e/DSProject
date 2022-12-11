a=int(input('Sisesta üks arv: '))
korrad=0
ruutsummad=0
summar=1
b=0
while korrad<a:
    korrad=korrad+1
    ruutsummad=ruutsummad+korrad
    summar=korrad**2
    b=b+summar
print("Summa erinevus on:",ruutsummad**2-b)