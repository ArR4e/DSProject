def minu_shuffle(a):
    from random import sample
    k_el = len(a)
    i = 0
    for el in a:
        ind = sample(range(0, len(a)), 1)
        for new_el in ind:
            number = new_el
        
        del a[i]
        i += 1
        a.insert(number,el)
    return a
    
