def elektriliin(liini_pikkus, postide_vahe):
    if postide_vahe > liini_pikkus:
        print("Liini pikkus on väiksem kui postide vahe")
    else:
        print(int(liini_pikkus / postide_vahe) + 1)

elektriliin(100, 10)
elektriliin(5, 10)