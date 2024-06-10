import itertools

def generate_combinations_and_save(n, p, filename):
    combinations = list(itertools.combinations(range(1, n + 1), p))
    with open(filename, 'w') as file:
        for comb in combinations:
            file.write(' '.join(map(str, comb)) + '\n')

generate_combinations_and_save(25, 15, 'Data_Logs/combinations_15.txt')
generate_combinations_and_save(25, 14, 'Data_Logs/combinations_14.txt')
generate_combinations_and_save(25, 13, 'Data_Logs/combinations_13.txt')
generate_combinations_and_save(25, 12, 'Data_Logs/combinations_12.txt')
generate_combinations_and_save(25, 11, 'Data_Logs/combinations_11.txt')
