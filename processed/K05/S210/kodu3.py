def moos(a,b,c):
    mituväikest = 0
    if c <= a * 5 + b:
        mitusuurt = c // 5
        if mitusuurt <= a:
            mituväikest = c - mitusuurt*5
            if mituväikest > b:
                return (-1)
            else:
                return mitusuurt + mituväikest
        else:
            if mitusuurt > a:
                mituväikest = c - a * 5
                return (a + mituväikest)
        return(mitusuurt + mituväikest)
    else:
        return (-1)
print(moos(2,20,25))