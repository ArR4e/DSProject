a=[[" ", "X","X","X"],
   ["O", "O","O"," "],
   ["O", " ","X"," "],
   ["O", " ","X"," "]]
X=0
O=0
# for rida in a:
#     for i in range(2):
#         if rida[i]==rida[i+1]==rida[i+2]:
#             if rida[i]=="X":
#                 X+=1
#             elif rida[i]=="O":
#                 O+=1


for rida in a:
    for i in range(2):
        for j in range(4):
            if a[i][j]==a[i+1][j]==a[i+2][j]:
                if rida[j]=="X":
                    X+=1
                elif rida[j]=="O":
                    O+=1

print(X)
print(O)