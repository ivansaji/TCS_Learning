def setOperation(seta, setb):
    # Write your code here
    new_set_a = set(seta)
    new_set_b = set(setb)
    if len(new_set_b) < 10000 and len(new_set_b) < 10000:

        seta_union_setb = new_set_a.union(new_set_b)
        seta_union_setb_list = list(seta_union_setb)
        seta_union_setb_list.sort()

        seta_inter_setb = new_set_a.intersection(new_set_b)
        seta_inter_setb_list = list(seta_inter_setb)
        seta_inter_setb_list.sort()

        seta_diff_setb = new_set_a.difference(new_set_b)
        seta_diff_setb_list = list(seta_diff_setb)
        seta_diff_setb_list.sort()

        setb_diff_seta = new_set_b.difference(new_set_a)
        setb_diff_seta_list = list(setb_diff_seta)
        setb_diff_seta_list.sort()

        seta_symm_setb = new_set_a.symmetric_difference(new_set_b)  # <-- change to .symmetric_difference
        seta_symm_setb_list = list(seta_symm_setb)
        seta_symm_setb_list.sort()

        new_set_a_frozen = frozenset(new_set_a)

        return seta_union_setb, seta_inter_setb, seta_diff_setb, setb_diff_seta,seta_symm_setb, new_set_a_frozen