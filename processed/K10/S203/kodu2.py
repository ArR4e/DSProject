def võitja(maatriks):
    arv_x = 0
    arv_o = 0
    sõnastik = {}
#     read
    if maatriks[0][0]==maatriks[0][1]==maatriks[0][2]=='X':
        arv_x += 1
    if maatriks[0][0]==maatriks[0][1]==maatriks[0][2]=='O':
        arv_o += 1
    if maatriks[0][1]==maatriks[0][2]==maatriks[0][3]=='X':
        arv_x += 1
    if maatriks[0][1]==maatriks[0][2]==maatriks[0][3]=='O':
        arv_o += 1
    if maatriks[1][0]==maatriks[1][1]==maatriks[1][2]=='X':
        arv_x += 1
    if maatriks[1][0]==maatriks[1][1]==maatriks[1][2]=='O':
        arv_o += 1
    if maatriks[1][1]==maatriks[1][2]==maatriks[1][3]=='X':
        arv_x += 1
    if maatriks[1][1]==maatriks[1][2]==maatriks[1][3]=='O':
        arv_o += 1
    if maatriks[2][0]==maatriks[2][1]==maatriks[2][2]=='X':
        arv_x += 1
    if maatriks[2][0]==maatriks[2][1]==maatriks[2][2]=='O':
        arv_o += 1
    if maatriks[2][1]==maatriks[2][2]==maatriks[2][3]=='X':
        arv_x += 1
    if maatriks[2][1]==maatriks[2][2]==maatriks[2][3]=='O':
        arv_o += 1
    if maatriks[3][0]==maatriks[3][1]==maatriks[3][2]=='X':
        arv_x += 1
    if maatriks[3][0]==maatriks[3][1]==maatriks[3][2]=='O':
        arv_o += 1
    if maatriks[3][1]==maatriks[3][2]==maatriks[3][3]=='X':
        arv_x += 1
    if maatriks[3][1]==maatriks[3][2]==maatriks[3][3]=='O':
        arv_o += 1
#     veerud
    if maatriks[0][0]==maatriks[1][0]==maatriks[2][0]=='X':
        arv_x += 1
    if maatriks[0][0]==maatriks[1][0]==maatriks[2][0]=='O':
        arv_o += 1
    if maatriks[1][0]==maatriks[2][0]==maatriks[3][0]=='X':
        arv_x += 1
    if maatriks[1][0]==maatriks[2][0]==maatriks[3][0]=='O':
        arv_o += 1
    if maatriks[0][1]==maatriks[1][1]==maatriks[2][1]=='X':
        arv_x += 1
    if maatriks[0][1]==maatriks[1][1]==maatriks[2][1]=='O':
        arv_o += 1
    if maatriks[1][1]==maatriks[2][1]==maatriks[3][1]=='X':
        arv_x += 1
    if maatriks[1][1]==maatriks[2][1]==maatriks[3][1]=='O':
        arv_o += 1
    if maatriks[0][2]==maatriks[1][2]==maatriks[2][2]=='X':
        arv_x += 1
    if maatriks[0][2]==maatriks[1][2]==maatriks[2][2]=='O':
        arv_o += 1
    if maatriks[1][2]==maatriks[2][2]==maatriks[3][2]=='X':
        arv_x += 1
    if maatriks[1][2]==maatriks[2][2]==maatriks[3][2]=='O':
        arv_o += 1
    if maatriks[0][3]==maatriks[1][3]==maatriks[2][3]=='X':
        arv_x += 1
    if maatriks[0][3]==maatriks[1][3]==maatriks[2][3]=='O':
        arv_o += 1
    if maatriks[1][3]==maatriks[2][3]==maatriks[3][3]=='X':
        arv_x += 1
    if maatriks[1][3]==maatriks[2][3]==maatriks[3][3]=='O':
        arv_o += 1
#     diagonaalid
    if maatriks[1][0]==maatriks[2][1]==maatriks[3][2]=='X':
        arv_x += 1
    if maatriks[1][0]==maatriks[2][1]==maatriks[3][2]=='O':
        arv_o += 1
    if maatriks[0][0]==maatriks[1][1]==maatriks[2][2]=='X':
        arv_x += 1
    if maatriks[0][0]==maatriks[1][1]==maatriks[2][2]=='O':
        arv_o += 1
    if maatriks[1][1]==maatriks[2][2]==maatriks[3][3]=='X':
        arv_x += 1
    if maatriks[1][1]==maatriks[2][2]==maatriks[3][3]=='O':
        arv_o += 1
    if maatriks[0][1]==maatriks[1][2]==maatriks[2][3]=='X':
        arv_x += 1
    if maatriks[0][1]==maatriks[1][2]==maatriks[2][3]=='O':
        arv_o += 1
    if maatriks[2][0]==maatriks[1][1]==maatriks[0][2]=='X':
        arv_x += 1
    if maatriks[2][0]==maatriks[1][1]==maatriks[0][2]=='O':
        arv_o += 1
    if maatriks[3][0]==maatriks[2][1]==maatriks[1][2]=='X':
        arv_x += 1
    if maatriks[3][0]==maatriks[2][1]==maatriks[1][2]=='O':
        arv_o += 1
    if maatriks[2][1]==maatriks[1][2]==maatriks[0][3]=='X':
        arv_x += 1
    if maatriks[2][1]==maatriks[1][2]==maatriks[0][3]=='O':
        arv_o += 1
    if maatriks[3][1]==maatriks[2][2]==maatriks[1][3]=='X':
        arv_x += 1
    if maatriks[3][1]==maatriks[2][2]==maatriks[1][3]=='O':
        arv_o += 1
    sõnastik['O']=arv_o
    sõnastik['X']=arv_x
    return sõnastik