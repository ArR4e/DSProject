#bussid

failinimi = input('Sisestage failinimi: ')
fail = open(failinimi, 'r', encoding = 'UTF-8')

def vaiksem(el1, el2):
    #return el1 < el2
    if el1[0] != el2[0]:
        return el1[0] < el2[0]
    else:
        return el1[1] < el2[1]

def järjesta_punktid(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1, len(a)):
            #if a[j] < a[min]:
            if vaiksem(a[j], a[min]):
                min = j
        if i != min:
            a[i], a[min] = a[min], a[i]

graafik = []
for rida in fail:
    #print(rida.rstrip())
    graafik.append(rida.split())
print(graafik)

järjesta_punktid(graafik)
