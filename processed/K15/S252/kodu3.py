import time
from datetime import datetime

def bubbleSort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j][0] > arr[j + 1][0] :
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
def loe_failist(failSoiduplaan ):    
    tmplist = []
    sonastik = {}
    
 with open(failSoiduplaan) as file:
        for line in file:          
            tmpVal = line.rstrip() # üks rida failist lugeda
            arr = tmpVal.split(" ") # siia kõi väärtused eraldi, eraldan tühiku alusel
            valjumine = arr[0] # 
            saabumine =arr[1] #          
            hind = arr[2] #                        
            time_1 = datetime.strptime(valjumine,"%H:%M")
            time_2 = datetime.strptime(saabumine,"%H:%M")
            time_interval = (time_2 - time_1).total_seconds() / 60.0
             rida = (arr[0],arr[1],arr[2],time_interval)     
            tmplist.append(rida)     
    return tmplist
#failiNimi = input("Sisesta failinimi:") #sõiduplaan.txt
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
time_list = loe_failist("soiduplaan.txt")
print(time_list)
sortedList = bubbleSort(time_list)

maxTimeInterval = 0
maxCost = 0
for rida in sortedList:
    if maxTimeInterval < rida[3]:
        maxTimeInterval = rida[3]
    if maxCost < int(rida[2]):
        maxCost = int(rida[2])


print(maxCost)
print(maxTimeInterval)
# remove too expensive andtoo long trips
filteredList = []
for rida in sortedList:
    if int(rida[2]) <  maxCost and int(rida[3]) < maxTimeInterval:
        filteredList.append(rida)     
print(filteredList)


print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")
for rida in filteredList:
    print(rida[0] +" "+ rida[1]+" "+ str(rida[2]))
