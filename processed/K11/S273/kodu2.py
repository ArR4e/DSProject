def transponeeriK(X):
       
    for rida in X:
        rida = rida.reverse()
    
    X = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
    
    for rida in X:
        rida = rida.reverse()
        
    return X