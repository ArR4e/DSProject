failinimi = input("Sisesta failinimi: ")
f = open(failinimi, "r")

järjend = []

for rida in f:
    rida = rida.rstrip()
    järjend.append(rida.split(" "))
    
f.close()

for alamjärjend in järjend:
    alamjärjend[2].replace('\n', '')
    
#print(järjend)

def selection_sort(A):
    for i in range(0, len(A)-1):
        s = i
        for j in range(i, len(A)):
            if A[j] < A[s]:
                s = j
        A[i], A[s] = A[s], A[i]

selection_sort(järjend)
#print(järjend)

for buss in järjend:
    for buss2 in järjend:
        if buss2[0] < buss[0] and buss2[1] > buss[1] and int(buss2[2]) > int(buss[2]):
            järjend.remove(buss2)
            
for buss in järjend[::-1]:
    for buss2 in järjend:
        if buss2[0] < buss[0] and buss2[1] > buss[1] and int(buss2[2]) > int(buss[2]):
            järjend.remove(buss2)  
            
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")
for buss in järjend:
    print(buss[0], buss[1], buss[2])