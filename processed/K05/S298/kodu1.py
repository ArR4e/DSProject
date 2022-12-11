user = input("palun sisestage enda nimi: ")
parool1 = ""
parool2 = ""
tagurpidi1 = ""
x = False
y = False


def parool():
    global parool1
    global parool2
    parool1 = input("palun sisestage parool: ")
    parool2 = input("sisestage parool uuesti: ")
    kattub()
    
def kattub():
    if parool1 == parool2:
        pikkus()
    else:
        print("paroolid ei kattu!")
        parool()

def pikkus():
    if len(parool1) >= 8:
        numbrid()
    else:
        print("parool peab olema vähemalt 8 märki pikk!")
        parool()
        
def numbrid():
    global x
    global y
    for i in parool1:
        if i.isdigit() == True:
             x = True
        else:
            y = True
    numbrid2()
    
def numbrid2():
    global x
    global y
    if y == True and x == True:
        tagurpidi()
    else:
        y = False
        x = False
        print("paroolis pole kasutusel nii tähed kui ka numbrid")
        parool()
        
def tagurpidi():
    global tagurpidi1
    for i in parool1:
        tagurpidi1 = i + tagurpidi1
    f = open("users.txt", "w")
    f.write(user + ":" + tagurpidi1)
       
parool()
