sisend_fail = input("Sisestage sisiendi failinimi: ")
väljund_fail = input("Sisestage väljundi failinimi: ")

with open(sisend_fail, 'r') as sisend:
    sissetulev = sisend.read()
    print(sissetulev.count('Hello'))
    väljund = sissetulev.replace('Hello', 'Tere')
    with open(väljund_fail, 'w') as väljaminev:
        väljaminev.write(väljund)
        