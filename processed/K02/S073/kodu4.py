inputFile = str(input("Ingliskeelne fail: "))
outputFile = str(input("Salvestakase ümber: "))

inputText = open(inputFile, "r").read()

print(inputText.count("Hello"))

translatedFile = open(outputFile, "w")
translatedFile.write(inputText.replace("Hello", "Tere"))
translatedFile.close()