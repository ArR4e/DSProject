def moos(suur, väike, moos_kg):
    purk=0
    s_purk=5
    üle= moos_kg - s_purk
    if moos_kg != 0:
        if moos_kg >= s_purk:
            if ((5*suur)+väike) >= moos_kg:
                while moos_kg > 5 or moos_kg == 0:
                    if suur >= 0:
                        moos_kg -= s_purk
                        purk += 1
                if (moos_kg % s_purk) <= väike:
                    while moos_kg != 0:
                        moos_kg -= 1
                        väike -= 1
                        purk += 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return 0
    return purk
    