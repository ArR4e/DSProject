pikkus = int(input("Kui pikka elektriliini sul vaja on?"))
vahe = int(input("Kui suur vahe peab elektripostide vahel olema?"))

post = pikkus//vahe
postkont = pikkus%vahe
if post < 1:
    post = post + 2
elif post >= 1 and postkont > 0:
    post = post + 2
elif post >= 1 and postkont == 0:
    post = post + 1
str(post)
print("Sul peab olema", post,"posti.")