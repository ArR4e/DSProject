def moos(suur,väike,kokku):
    if kokku//5 >suur:
        if kokku-suur*5>väike:
            return -1
        else:
            return suur +kokku -suur*5
    else:
        if kokku - 5*(kokku//5)>väike:
            return -1
        else:
            return kokku//5 + kokku - 5*(kokku//5)