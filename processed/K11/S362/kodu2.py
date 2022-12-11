def transponeeriK(maatriks):
    maatriksT=[]
    if maatriks==[[]]:
        return maatriks
    else:
        
        a=len(maatriks[0])-1
        while a>-1:
            maatriksT_rida=[]
            for i in range((len(maatriks)-1),-1,-1):
                maatriksT_rida+=[maatriks[i][a]]
            #print(maatriksT_rida)
            maatriksT+=[maatriksT_rida]
            a=a-1
        return maatriksT
    
        
   
maatriks=[[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
# maatriks=[[1, 2], [3, 4], [5, 6], [7, 8]]
# maatriks=[[4, 31, 67, 99]]
# maatriks=[[]]


maatriksT=transponeeriK(maatriks)
print(maatriks)
print(maatriksT)
#peadiagonaali pidi transponeeritud
# maatriksT1=[]
# j=0
# while j<len(maatriks):
#     maatriksT1_rida=[]
#     for i in range(len(maatriks)):
#     
#         maatriksT1_rida+=[maatriks[i][j]]
#         print(maatriksT1_rida)
#     maatriksT1+=[maatriksT1_rida]
#     j=j+1
# 
# print(maatriksT1)
#[[9, 6, 3], [8, 5, 2], [7, 4, 1]]

#kõrvaldiagonaalipidi transponeerimine:

# maatriksT=[]
# a=2
# while a>-1:
#     maatriksT_rida=[]
#     for i in range(2,-1,-1):
#     
#         maatriksT_rida+=[maatriks[i][a]]
#         print(maatriksT_rida)
#     maatriksT+=[maatriksT_rida]
#     a=a-1
# print(maatriks)
# print(maatriksT)