def moos(suured_karbid, väiksed_karbid, moos_kg):
    suured_moosikarbid = moos_kg // 5
    kasutada_suuri = min(suured_karbid, suured_moosikarbid)
    väikseid_vaja = moos_kg - 5 * kasutada_suuri
    if väikseid_vaja <= väiksed_karbid:
        return(kasutada_suuri + väikseid_vaja)
    else:
        return -1
# def moos(suured_karbid, väiksed_karbid, moos_kg):
#         suur_moosikarp = int(moos_kg // 5)
#         väike_moosikarp = int(moos_kg % 5)
#         if suured_karbid * 5 + väiksed_karbid * 1 >= moos_kg:
#             if  moos_kg - suur_moosikarp > väiksed_karbid:
#                 return (-1)
#             if moos_kg == 0:
#                 return 0
#             if suur_moosikarp >= suured_karbid and väike_moosikarp >= väiksed_karbid:
#                 karpide_arv = (moos_kg // 5) + (moos_kg % 5)
#             else:
#                 karpide_arv = suured_karbid + (moos_kg - suured_karbid * 5)
#             return karpide_arv
#         
#         else:
#             return (-1)

