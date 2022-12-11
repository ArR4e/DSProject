liin = float(input("Sisestage elektriliini pikkuse: "))
post = float(input("Sisestage postide kaugust: "))

if post > liin or liin <= 0 or post <= 0:
    print("Valedad andmed.")
else:
    post_1 = int(liin / post) + 1
    print("Minimaalselt on vaja " + str(post_1) + " postit")
 