import re
fail = open("aadressid.txt")
print("Kasutajanimed on:")
for rida in fail:
    sonad = rida.split("/")
    kasutajanimi = r"^~\w+$"
    tartu = "www.ut.ee"
    if tartu in sonad:
        for sona in sonad:
            if re.match(kasutajanimi, sona):
                muster = r"\~"
                sona = re.sub(muster, "", sona)
                print(sona)
fail.close()
