def transponeeriK(m):
    return list(map(list,zip(*m[::-1])))[::-1]

print(transponeeriK([[4, 31, 67, 99]]))