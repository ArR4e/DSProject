liin=int(input("Kui pikk on elektriliin meetrites? "))
if liin==0:
    print("Meil läheb vaja 1 posti. Siiski, ma soovitan tõsiselt kaaluda seda, kas seda ühtegi vaja läheb.")
else:
    post=int(input("Mitme meetri kaugusel võivad postid üksteisest maksimaalselt olla? "))
    if liin//post==liin/post:
        print("Meil läheb vaja vähemalt", int(1+liin//post), "posti.")
    else:
        print("Meil läheb vaja vähemalt", int(2+liin//post), "posti.")