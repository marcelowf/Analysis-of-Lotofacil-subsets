def find_subsets_of_15_that_contain_13(combinations_15, combinations_13):
    subset = []
    set_13 = set(map(tuple, combinations_13))

    for comb15 in combinations_15:
        comb15_set = set(comb15)
        matching_subsets = {subset_13 for subset_13 in set_13 if set(subset_13).issubset(comb15_set)}
        if matching_subsets:
            subset.append(comb15)
            set_13 -= matching_subsets
        if not set_13:
            break

    return subset
