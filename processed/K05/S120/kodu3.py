
def moos(big_box, small_box, jam_weight):
    big_box_weight = 5
    small_box_weight = 1
    
    jam_remaining = jam_weight
    boxes_used = 0
    for i in range(big_box):
        
        if jam_remaining - big_box_weight >= 0:
            jam_remaining -= big_box_weight
            boxes_used += 1
        else:
            break
        
    if jam_remaining == 0:
        return boxes_used
    
    for i in range(small_box):
        jam_remaining -= small_box_weight
        boxes_used += 1
        
        if jam_remaining == 0:
            return boxes_used
    
    return -1