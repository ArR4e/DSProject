def transponeeriK(mat):
    return [list(i)[::-1]for i in zip(*mat)][::-1]
    