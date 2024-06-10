def find_subsets_of_15_that_contain_12(combinations_15, combinations_12):
    subset = []
    set_12 = set(map(tuple, combinations_12))

    for comb15 in combinations_15:
        comb15_set = set(comb15)
        matching_subsets = {subset_12 for subset_12 in set_12 if set(subset_12).issubset(comb15_set)}
        if matching_subsets:
            subset.append(comb15)
            set_12 -= matching_subsets
        if not set_12:
            break

    return subset
