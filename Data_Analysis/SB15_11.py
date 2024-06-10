def find_subsets_of_15_that_contain_11(combinations_15, combinations_11):
    subset = []
    set_11 = set(map(tuple, combinations_11))

    for comb15 in combinations_15:
        comb15_set = set(comb15)
        matching_subsets = {subset_11 for subset_11 in set_11 if set(subset_11).issubset(comb15_set)}
        if matching_subsets:
            subset.append(comb15)
            set_11 -= matching_subsets
        if not set_11:
            break

    return subset
