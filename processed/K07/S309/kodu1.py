def poisse_ja_tüdrukuid(datalist):

    #variables for the counts of male and female names
    malecount = 0
    femalecount = 0

    #loop through the list and count males and females
    for item in datalist:
        if(str(item[-1]) == "P"):
            malecount += 1
        elif(str(item[-1]) == "T"):
            femalecount += 1
    
    #return a tuple of both counts
    return (malecount, femalecount)