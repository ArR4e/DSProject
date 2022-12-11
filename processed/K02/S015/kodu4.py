sis = input("Sisend fail: ")
val = input("Väljund fail: ")
count = 0
with open(sis,"r") as sisend:
    with open(val, "w") as valjund:
        for i in sisend:
            count += i.lower().count('hello')
            if "hello" in i:
                i = i.replace("hello", "tere")
            if "Hello" in i :
                i = i.replace("Hello",  "Tere")
            valjund.write(i)
                
                          
        print(count)