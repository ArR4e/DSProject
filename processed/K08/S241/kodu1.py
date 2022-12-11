from random import sample
def bingo():
    while True:
        a = sample(range(1, 11), 3)
        if (a == [1,2,3] or # TRUE or TRUE -> TRUE ehk kui üks neist on TRUE siis sulgudes on TRUE ja rakendub break
        a == [1,3,2] or # tsükkel jääb seisma
        a == [2,1,3] or # kui ükski neist ei ole TRUE siis kõik on FALSE
        a == [2,3,1] or # FALSE or FALSE -> FALSE ja break ei rakendu ning tsükkel algab otsast peale st genereerib uue a
        a == [3,1,2] or # aga oleks vaja, et ta teeb vaid ühe korra läbi - juhul kui a ei sisalda 1,2,3 
        a == [3,2,1]): # või siis kaks või rohkem korda juhul kui sisaldab 
            break
        b = sample(range(11, 21), 2)
        print(a + b)
bingo()