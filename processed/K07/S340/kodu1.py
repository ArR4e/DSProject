def poisse_ja_tüdrukuid(järjend):
  
    f = open(järjend) 
    poisse=0
    tüdrukuid=0
    for rida in f:
        jupid = rida.split()
        if jupid[-1] == "P":
            poisse += 1
            continue
        elif jupid[-1] == "T":
            tüdrukuid += 1
            continue
        else:
            break
    print("(",poisse,", ",tüdrukuid,")")
    f.close()

järjend = poisse_ja_tüdrukuid("poissetydrukuid.txt")
    
       