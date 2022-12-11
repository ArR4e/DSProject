mänguseis = ([['X',' ','O',' '],
              ['O','X',' ',' '],
              ['O',' ','X',' '],
              ['O',' ',' ','X']])


def võitja(mänguseis):
    X_loendur = 0
    O_loendur = 0
    seis = {}
    
    seis['X']= set()
    seis['O']= set()
    
    for sümbol in mänguseis:
        if sümbol == 'X':
            X_loendur += 1
        if sümbol == 'O':
            O_loendur += 1
 #peadiagonaalid    
    for i in range(1):
        for j in range(1):
            if mänguseis[i][j] == mänguseis[i+1][j+1] == mänguseis[i+2][j+2] == mänguseis[i+3][j+3] == 'X':
                 seis['X'] += 2
            else:
                if mänguseis[i][j] == mänguseis[i+1][j+1] == mänguseis[i+2][j+2]  == 'X' or mänguseis[i+1][j+1] == mänguseis[i+2][j+2]== mänguseis[i+3][j+3] == 'X':
                    seis['X'] +=1
                    
            if mänguseis[i][j] == mänguseis[i+1][j+1] == mänguseis[i+2][j+2] == mänguseis[i+3][j+3] == 'O':
                 seis['O'] +=2
            else:
                if mänguseis[i][j] == mänguseis[i+1][j+1] == mänguseis[i+2][j+2]  == 'O' or mänguseis[i+1][j+1] == mänguseis[i+2][j+2]== mänguseis[i+3][j+3] == 'O':
                    seis['O'] += 1
                    
            if mänguseis[i][j+3] == mänguseis[i+1][j+2] == mänguseis[i+2][j+1] == mänguseis[i+3][j] == 'X':
                 seis['X'] +=2
            else:
                if mänguseis[i][j+3] == mänguseis[i+1][j+3] == mänguseis[i+2][j+1]  == 'X' or mänguseis[i+1][j+3] == mänguseis[i+2][j+1]== mänguseis[i+3][j] == 'X':
                    seis['X'] += 1
                    
            if mänguseis[i][j+3] == mänguseis[i+1][j+2] == mänguseis[i+2][j+1] == mänguseis[i+3][j] == 'O':
                 seis['O'] +=2
            else:
                if mänguseis[i][j+3] == mänguseis[i+1][j+3] == mänguseis[i+2][j+1]  == 'O' or mänguseis[i+1][j+3] == mänguseis[i+2][j+1]== mänguseis[i+3][j] == 'O':
                    seis['O'] += 1
                
#             if mänguseis[i][j] == mänguseis[i][j+1] == mänguseis[i][j+2] == mänguseis[i][j+3] == 'X':
#                  seis['X'].add(2)
#             if mänguseis[i][j] == mänguseis[i][j+1] == mänguseis[i][j+2] == mänguseis[i][j+3] == 'O':
#                  seis['O'].add(2)
#             if mänguseis[i][j] == mänguseis[i+1][j] == mänguseis[i+2][j] == mänguseis[i+3][j] == 'X':
#                  seis['X'].add(2)
#             if mänguseis[i][j] == mänguseis[i+1][j] == mänguseis[i+2][j] == mänguseis[i+3][j] == 'O':
#                  seis['O'].add(2)
#                  
    for i in range(2):
        for j in range(2):
            if mänguseis[i][j] == mänguseis[i+1][j] == mänguseis[i+2][j]  == 'X':
                seis['X'].add(1)
            if mänguseis[i][j] == mänguseis[i+1][j] == mänguseis[i+2][j]  == 'O':
                seis['O'].add(1)
                
#             if mänguseis[i][j] == mänguseis[i][j+1] == mänguseis[i][j+2] == 'X' or mänguseis[i][j+1] == mänguseis[i][j+2] == mänguseis[i][j+3] == 'X':
#                  seis['X'].add(1)
#             if mänguseis[i][j] == mänguseis[i][j+1] == mänguseis[i][j+2] == 'O' or mänguseis[i][j+1] == mänguseis[i][j+2] == mänguseis[i][j+3] == 'O':
#                  seis['O'].add(1)
#             if mänguseis[i][j] == mänguseis[i+1][j] == mänguseis[i+2][j] == 'X' or mänguseis[i+1][j] == mänguseis[i+2][j] == mänguseis[i+3][j] == 'X':
#                  seis['X'].add(1)
#             if mänguseis[i][j] == mänguseis[i+1][j] == mänguseis[i+2][j] == 'O' or mänguseis[i+1][j] == mänguseis[i+2][j] == mänguseis[i+3][j] == 'O':
#                  seis['O'].add(1)
#                  
#     for i in range(2):
#          for j in range(2):
#              if mänguseis[i][j] == mänguseis[i+1][j+1] == mänguseis[i+2][j+2] == 'X':
#                  seis['X'].add(1)
#              if mänguseis[i][j] == mänguseis[i+1][j+1] == mänguseis[i+2][j+2] == 'O':
#                  seis['O'].add(1)
#     
#     for i in range(2):
#         for j in range(2):
#             if mänguseis[i][j+2] == mänguseis[i+1][j+1] == mänguseis[i+2][j] == 'X':
#                 seis['X'].add(1)
#             if mänguseis[i][j+2] == mänguseis[i+1][j+1] == mänguseis[i+2][j] == 'O':
#                 seis['O'].add(1)
# 

#                  
#     for i in range(4):
#         for j in range(4):
#             if mänguseis[0][0] == mänguseis[0][1] == mänguseis[0][2] == mänguseis[0][3] == X:
#     
#     for i in range(4):
#         for j in range(4):
#             if mänguseis[0][0] == mänguseis[1][0] == mänguseis[2][0] == mänguseis[3][0] == X:
#       kolmesed ridades
   
    for i in range(2):
        for j in range(2):
            if mänguseis[i][j] == mänguseis[i][j+1] == mänguseis[i][j+2] == mänguseis[i][j+3] == 'X':
                seis['X'] += 1
            if mänguseis[i][j] == mänguseis[i][j+1] == mänguseis[i][j+2] == mänguseis[i][j+3] == 'O':
                seis['O'] += 1
    print(seis)
     
võitja(mänguseis)