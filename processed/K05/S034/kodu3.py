def moos(x, y, z):
# x = suurte karpide arv (5kg), y = väikeste karpide arv(1kg), z = keedetava moosi kogus kilogrammides
    kasutatud_karpide_arv = 0
    # vaatame, kas keedetavat moosi üldse on:
    if z > 0:
        # vaatame, kas suuri 5 kg seid karpe on
        if x > 0:
            # kui moosi kogus on suurem või võrdne 5 kg-iga ning suuri karpe on siis kasutame neid.
            while z >= 5 and x > 0:
                if z - 5 >= 0:
                    z -= 5
                    x -= 1
                    kasutatud_karpide_arv += 1
            # kui kogu moos sai suurtesse purkidesse ära paigutatud siis tagastame kasutataud karpide arvu.
            if z == 0:
                return kasutatud_karpide_arv
            # kui moosi jäi veel järgi siis vaatame, kas meil on piisavalt väikeseid 1 kg-seid karpe, et kogu moos ära mahutada.
            if y >= z and y!=0 :
                kasutatud_karpide_arv += z
                return kasutatud_karpide_arv
            # kui kogu moos karpidesse täpselt ära ei mahtunud siis tagastame arvu -1.
            else:
                return -1
        # kui suuri karpe pole siis vaatame, kas väikestest piisab.
        else:
            #kui väikeseid karpe pole ning eelmisest tingimusest saime, et moosi on siis tagastame arvu -1.
            if y == 0:
                return -1
            else:
                # kui väikesed karbid mahutavad kogu ülejäänud moosi ära siis tagastame kasutatud karpide arvu.
                if y >= z and y!=0:
                    kasutatud_karpide_arv += z
                    return kasutatud_karpide_arv
                # kui väikeseid karpe on liiga vähe, et kogu moosi ära mahutada siis tagastame arvu -1.
                else:
                    return -1
    # kui moosi pole siis tagastame arvu 0.
    else:
        return 0