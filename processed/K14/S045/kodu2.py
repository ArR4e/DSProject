global print_queue
print_queue = str()

def väljasta_liin(eellane, järglane, sugupuu):
    global print_queue
    print_queue = print_queue + eellane + "\n"
    if eellane == järglane:
        print(print_queue.strip())
        print_queue = str() #reset
        return True
    sugupuu_v_list = list(sugupuu.values())
    sugupuu_k_list = list(sugupuu.keys())
    for i in range(len(sugupuu_v_list)):
        if eellane in sugupuu_v_list[i]:
            return väljasta_liin(sugupuu_k_list[i], järglane, sugupuu)
    return False
