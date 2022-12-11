def poisse_ja_tüdrukuid(list):
    m = 0
    n = 0
    for line in list:
        if line[-1] == 'P':
            m += 1
        elif line [-1] == 'T':
            n += 1
    return (m,n)