def võitja(mat):
    BBW={}
    eh={'O': 0, 'X': 0}
    #range(len(mat))=range(len(mat[0]))=range(4) antud ülesandes, aga tahtsin pikemalt panna
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            BBW[(i,j)]=mat[i][j]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            el=mat[i][j]
            try:
                if el == BBW[(i-1,j)] and el == BBW[(i+1,j)]: #ridamisi kesmise järgi kolmik
                    eh[el]+=1
            except: pass
            try:
                if el == BBW[(i,j-1)] and el == BBW[(i,j+1)]: #veergimisi kesmise järgi kolmik
                    eh[el]+=1
            except: pass
            try:
                if el == BBW[(i+1,j+1)] and el == BBW[(i-1,j-1)]: #tõus diag kesmise järgi kolmik
                    eh[el]+=1
            except: pass
            try:
                if el == BBW[(i-1,j+1)] and el == BBW[(i+1,j-1)]: #lang diag kesmise järgi kolmik
                    eh[el]+=1
            except: pass
    return eh