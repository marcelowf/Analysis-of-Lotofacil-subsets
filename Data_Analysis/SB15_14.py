def find_subsets_of_15_that_contain_14(combinations_15, combinations_14):
    subset = []
    set_14 = set(map(tuple, combinations_14))  # Convertendo para um conjunto de tuplas para facilitar a busca

    for comb15 in combinations_15:
        comb15_set = set(comb15)
        matching_subsets = {subset_14 for subset_14 in set_14 if set(subset_14).issubset(comb15_set)}
        if matching_subsets:
            subset.append(comb15)
            set_14 -= matching_subsets
        if not set_14:
            break

    return subset
