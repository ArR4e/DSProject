def seosta_lapsed_ja_vanemad(laps,nimi):
    f = open(laps,'r')
    g = open(nimi,'r')
    nimed ={}
    lapsed = {}
    vanemadlist = []
    vanemadhulk = set()
    while True:
        x = g.readline()
        if x == '':
            break
        x = x.strip('\n').split(' ')
        nimed[x[0]] = (x[1]+' '+x[2])
    
    while True:
        y = f.readline()
        if y == '' :
            break
        y = y.strip('\n').split(' ')
        y[1] = nimed[y[1]]
        if y[1] in lapsed:
            lapsed[y[1]].add(nimed[y[0]])
            
        else:
            lapsed[y[1]] = set()
            lapsed[y[1]].add(nimed[y[0]])
            
    for i in lapsed.keys():
        print(i+':',str(lapsed[i]).strip('{').strip('}'))
              
    f.close()
    g.close()
    
seosta_lapsed_ja_vanemad('lapsed.txt','nimed.txt')