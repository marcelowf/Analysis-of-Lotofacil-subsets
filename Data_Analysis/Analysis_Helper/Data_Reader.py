def read_combinations_from_file(filename):
    combinations = []
    with open(filename, 'r') as file:
        for line in file:
            comb = tuple(map(int, line.strip().split()))
            combinations.append(comb)
    return combinations
