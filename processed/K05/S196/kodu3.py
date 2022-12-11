def moos(suuri_karpe, väikseid_karpe, kg):
    max_kg = suuri_karpe * 5 + väikseid_karpe
    if kg > max_kg:
        print(-1)
    else:
        kasutatud_karpe = 0
        while kg >= 5 and suuri_karpe >= 0:
            kasutatud_karpe += 1
            kg -= 5
            suuri_karpe -= 1
            if kg == 0 and suuri_karpe >= 0:
                print(kasutatud_karpe)
            elif kg > 0 and suuri_karpe == 0:
                break
            
        while kg >= 0:
            if väikseid_karpe > 0:
                kasutatud_karpe += 1
                väikseid_karpe -= 0
                kg -= 1
                if kg == 0 and väikseid_karpe >= 0:
                    print(kasutatud_karpe)
                    break
                elif kg > 0 and väikseid_karpe == 0:
                    print(-1)
                    break