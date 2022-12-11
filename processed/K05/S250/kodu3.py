def moos(s_karpide_arv,v_karpide_arv,moosi_kogus):
    s_k_maht = 5
    v_k_maht = 1
    if (moosi_kogus // (s_k_maht)) != s_karpide_arv:
        if (moosi_kogus-s_karpide_arv*s_k_maht)-v_karpide_arv*v_k_maht > 0:
            return -1
        if moosi_kogus-((moosi_kogus // (s_k_maht))*s_k_maht)-v_karpide_arv*v_k_maht > 0:
            return -1
        else:
            if (moosi_kogus-(s_karpide_arv*s_k_maht)) <= v_karpide_arv:
                if (s_karpide_arv*s_k_maht)>moosi_kogus:
                    return (moosi_kogus // (s_k_maht)) + (moosi_kogus-((moosi_kogus//(s_k_maht))*s_k_maht))
                return ((s_karpide_arv)) + (moosi_kogus-((s_karpide_arv)*s_k_maht))
    if (moosi_kogus // (s_k_maht)) == s_karpide_arv:
        if (moosi_kogus%(s_karpide_arv*s_k_maht))==0:
            return s_karpide_arv
        if (moosi_kogus%(s_karpide_arv*s_k_maht))!=0:
            if (moosi_kogus-(s_karpide_arv*s_k_maht)) <= v_karpide_arv:
                return s_karpide_arv+(moosi_kogus-(s_karpide_arv*s_k_maht))
    