def moos(big_n, small_n, weight):
    if big_n * 5 + small_n < weight or weight % 5 > small_n:
        return -1
    else:
        big_max = weight // 5
        if big_n > big_max:
            big = big_max
            space = weight - big_max * 5
            return space + big_max
        if weight - big_n * 5 == 0:
            return big_n
        else:
            space = weight - big_n * 5
            return space + big_n
        #else:
            