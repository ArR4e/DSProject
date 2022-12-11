from datetime import timedelta
import datetime

failinimi = input("Sisesta failinimi: ")
# failinimi="sõiduplaanid.txt"
f=open(failinimi, encoding="utf-8")
lines = f.readlines()
ajad=[]
for line in lines:
    line=line.strip().split(" ")
    algus=line[0]
    lõpp=line[1]
    
    t1 = algus
    t2 = lõpp
    formated_t1 = datetime.datetime.strptime(t1, '%H:%M')
    formated_t2 = datetime.datetime.strptime(t2, '%H:%M')
    time0=timedelta(hours=0, minutes=0)
    time1=timedelta(hours=formated_t1.time().hour, minutes=formated_t1.time().minute)
    time2=timedelta(hours=formated_t2.time().hour, minutes=formated_t2.time().minute)
    kestus=time2-time1
    line.append(kestus)
    ajad.append(line)
# print(ajad)
minimum=ajad[0][3]
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")
for i in ajad:
    if i[3]<=minimum:
        print (i[0], i[1], i[2])
        
#https://stackoverflow.com/questions/15148491/min-and-max-of-a-list-without-using-min-max-function
#https://stackabuse.com/converting-strings-to-datetime-in-python/
#https://blog.softhints.com/python-3-subtrack-time/