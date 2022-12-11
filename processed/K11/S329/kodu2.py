# 2. Maatriksi transponeerimine kõrvaldiagonaali järgi

# m - maatriks
# tr_m - transponeeritud maatriksiks

def transponeeriK(m):
    tr_m = []
    a = len(m[0])
    for el in m:
        if a != len(el):
            print("Maatriksit ei transponeerida, kuna elemente pole.")
            return
    for x in range(len(m[0])):
        järjend = []
        for y in m:
           järjend.append(y[-1])
           y.pop()
        järjend.reverse()
        tr_m.append(järjend)
    return(tr_m)        

#m = [[1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]]

#m = [[1, 2],
#     [3, 4],
#     [5, 6],
#     [7, 8]]

#m = [[4, 31, 67, 99]]
#m = eval(input("Sisestage maatriks: "))

#tr_m = transponeeriK(m)
#print(tr_m)