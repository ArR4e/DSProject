i = open("inglise.txt")
text = i.read().replace('Hello','Tere')
e = open("eesti.txt","w")
e.write(text + "\n")
i.close()
e.close()