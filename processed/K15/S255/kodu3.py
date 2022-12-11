
jarjend = []
with open(f'{input("sisesta faili nimi: ")}', 'r', encoding = 'UTF-8') as header:
    for i in header:
        jarjend.append([i.split()[0], i.split()[1], int(i.split()[2])])
    for l in range(len(jarjend) - 1):
        if int(jarjend[l][2]) > int(jarjend[l+1][2]):
            jarjend[l], jarjend[l+1] = jarjend[l+1], jarjend[l]
    for j in range(len(jarjend)-  1):
        for k in range(len(jarjend) - 1):
            a = jarjend[k][0].split(':')
            b = jarjend[k+1][0].split(':')
            c = jarjend[j][1].split(':')
            d = jarjend[j+1][1].split(':')
            
            if (int(c[0]) * 60 + int(c[1])) - (int(a[0]) * 60 + int(a[1])) < (int(d[0]) * 60 + int(d[1])) - (int(b[0]) * 60 + int(b[1])):
                jarjend[k], jarjend[k+1] = jarjend[k+1], jarjend[k]
#         for l in range(len(jarjend) - 1):
#             if (int(c[0]) * 60 + int(c[1])) - (int(a[0]) * 60 + int(a[1])) < (int(d[0]) * 60 + int(d[1])) - (int(b[0]) * 60 + int(b[1])) and int(jarjend[l][2]) > int(jarjend[l+1][2]):
#                 jarjend[l], jarjend[l+1] = jarjend[l+1], jarjend[l]
# Kui see lisada, siis ta sorteerib uuesti läbi ja vaatab hindasid ka. Odavamad lühema sõiduajaga piletid satuvad prioriteeti
for i in jarjend:
    print(f'{i[0]} {i[1]} {i[2]}')
# Mina ei tea, mis oli väärtuste tähtsused, seega ma jätan nii nagu ta on.