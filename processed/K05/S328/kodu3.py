def moos(large, small, kg):
    box = 0
    boxes_required = kg // 5
    
    if large >= boxes_required:
        kg -= boxes_required * 5
        box += boxes_required
        if small >= kg:
            box += kg
            return box
        else:
            return -1
    elif small >= kg:
        return kg
    
    elif small >= (kg - large * 5):
        box += large
        box += kg - large * 5
        return box
    
    else:
        return -1

print(moos(2, 20, 25))