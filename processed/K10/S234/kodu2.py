def võitja (maatriks):
    oosid=0
    ikse=0
    for rida in range(2):
        for tulp in range(2):
            if maatriks[rida][tulp]=="X" and maatriks[rida+1][tulp+1]=="X" and maatriks[rida+2][tulp+2]=="X":#vaatan diagonaalid
                ikse+=1
            if maatriks[rida][tulp]=="O" and maatriks[rida+1][tulp+1]=="O" and maatriks[rida+2][tulp+2]=="O":#vaatan diagonaalid
                oosid+=1
            if maatriks[rida][tulp+2]=="X" and maatriks[rida+1][tulp+1]=="X" and maatriks[rida+2][tulp]=="X":#vaatan diagonaalid
                ikse+=1
            if maatriks[rida][tulp+2]=="O" and maatriks[rida+1][tulp+1]=="O" and maatriks[rida+2][tulp]=="O":#vaatan diagonaalid
                oosid+=1
    for lisand in range(2):
        for väikerida in range(4):#vaatan read
            if maatriks[väikerida][0+lisand]=="X" and maatriks[väikerida][1+lisand]=="X" and maatriks[väikerida][2+lisand]=="X":
                ikse+=1
            if maatriks[väikerida][0+lisand]=="O" and maatriks[väikerida][1-+lisand]=="O" and maatriks[väikerida][2+lisand]=="O":
                oosid+=1
    for lisand in range(2):
        for väiketulp in range(4):#vaatan tulbad
            if maatriks[0+lisand][väiketulp]=="X" and maatriks[1+lisand][väiketulp]=="X" and maatriks[2+lisand][väiketulp]=="X":
                ikse+=1
            if maatriks[0+lisand][väiketulp]=="O" and maatriks[1+lisand][väiketulp]=="O" and maatriks[2+lisand][väiketulp]=="O":
                oosid+=1
    vastus={}
    vastus["X"]=ikse
    vastus["O"]=oosid
    return(vastus)
