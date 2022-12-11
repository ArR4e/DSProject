

def transponeeriK(maatriks):
   a = []
   a1 = []
   c = len(maatriks)
   b = len(maatriks[0])
   for i in range(b-1, -1, -1):
       for j in range(c-1, -1, -1):
           a.append(maatriks[j][i])
   a1 = [a[i:i+c] for i in range(0, c*b, c)]     
   return a1
           
print(transponeeriK([[4, 31, 67, 99]]))