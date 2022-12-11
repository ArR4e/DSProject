# automaatne kontroll kahjuks ei töötanud - annab errorit:
# You are using an encrypted connection.
# To use an encrypted connection with the execution servers it is required you accept its certificates.
# If you have problems with this process, you can try to use a http (unencrypted) connection or other browser.
# Please, click on the following links (server #) and accept the offered certificate.
# Server 10


f = open('kinganumbrid.txt')
num_lines = sum(1 for line in open('kinganumbrid.txt'))
count = 0
   
while num_lines > count:
    try:
        kinganumber = f.readline()
        pikkus = 2/3 * (float(kinganumber) - 2)
        print(round(pikkus))
        count += 1
    except:
        print("Vigane sisend")
        count += 1

f.close()

