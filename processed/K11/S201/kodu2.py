def transponeeriK(m):
    m =(m[::-1])
    result = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    result = (result[::-1])
    return (result)