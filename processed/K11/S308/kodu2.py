m=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def transponeeriK(m):
    järjend1=[]
    järjend2=[]
    järjend3=[]
    järjend=[]
    for row in m :
        row.reverse()
        järjend1.append(row)
    järjend1.reverse()
    #print(järjend1)
    rez = [[järjend1[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    #print('\n')
    #rez.reverse()
    for row in rez:
        järjend.append(row)
    return järjend
print(transponeeriK(m))
