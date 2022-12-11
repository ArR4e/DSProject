def moos(number_large_boxes, number_small_boxes, kg):
    large_box_kg = 5
    small_box_kg = 1
    kg_2 =large_box_kg*number_large_boxes+small_box_kg*number_small_boxes
    if kg_2 == kg:
        return number_large_boxes+number_small_boxes
    elif kg == 0:
        return 0
    else:
        a = -1
        return int(a)
print(moos(2, 4, 14))
print(moos(3, 3, 18))
print(moos(2, 0, 10))
print(moos(5, 1, 9))
        