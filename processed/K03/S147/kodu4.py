num = open("kinganumbrid.txt")
def main():
    while True:
        rida = num.readline()
        if rida == "":
            break
        try:
            print(round(2/3*(int(rida)-2)))
        except:
            print("Vigane Sisend")
            return main()
main()
num.close()