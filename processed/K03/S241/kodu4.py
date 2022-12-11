fail_sisse = open("kinganumbrid.txt")
for rida in fail_sisse:
    try:
        kinganr=float(rida.strip())
        print("Jalalaba pikkus on ", round(2/3*(kinganr-2),2), " sentimeetrit")
    except:
        print("??? see pole küll miski number...vigane rida")