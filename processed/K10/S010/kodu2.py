def võitja(maatriks):
    d={}
    kordajao=0
    kordajax=0
    for i in range(len(maatriks)):
        for j in range(len(maatriks[0])):
            try:
                if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]=='X':
                    kordajax+=1
                if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]=='O':
                    kordajao+=1
                if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]=='X':
                    kordajax+=1
                if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]=='O':
                    kordajao+=1
                if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2]=='X':
                    kordajax+=1
                if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2]=='O':
                    kordajaxo=1
                if maatriks[i+3][j]==maatriks[i+2][j+1]==maatriks[i+1][j+2]=='X':
                    kordajax+=1
                if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2]=='O':
                    kordajao+=1
            except:
                continue
    O=kordajao
    X=kordajax
    d['O']=O
    d['X']=X
    return d