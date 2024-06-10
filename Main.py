# main.py
import sys
import os
from Data_Analysis.Analysis_Helper.Data_Reader import read_combinations_from_file
from Data_Analysis.Analysis_Helper.Cost_Calculator import calculate_cost
from Data_Analysis.Analysis_Helper.Time_Counter import measure_execution_time
from Data_Analysis.SB15_14 import find_subsets_of_15_that_contain_14
from Data_Analysis.SB15_13 import find_subsets_of_15_that_contain_13
from Data_Analysis.SB15_12 import find_subsets_of_15_that_contain_12
from Data_Analysis.SB15_11 import find_subsets_of_15_that_contain_11

FUNCTIONS = {
    "sb15_14": {
        "combinations": ("Data_Logs/combinations_15.txt", "Data_Logs/combinations_14.txt"),
        "function": find_subsets_of_15_that_contain_14
    },
    "sb15_13": {
        "combinations": ("Data_Logs/combinations_15.txt", "Data_Logs/combinations_13.txt"),
        "function": find_subsets_of_15_that_contain_13
    },
    "sb15_12": {
        "combinations": ("Data_Logs/combinations_15.txt", "Data_Logs/combinations_12.txt"),
        "function": find_subsets_of_15_that_contain_12
    },
    "sb15_11": {
        "combinations": ("Data_Logs/combinations_15.txt", "Data_Logs/combinations_11.txt"),
        "function": find_subsets_of_15_that_contain_11
    }
}

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <função>")
        return

    function_name = sys.argv[1]

    if function_name in FUNCTIONS:
        combinations = FUNCTIONS[function_name]["combinations"]
        function_to_execute = FUNCTIONS[function_name]["function"]
        # Executa a medição do tempo de execução
        timer = measure_execution_time(function_to_execute, *map(read_combinations_from_file, combinations))
        # Executa a função real para obter o resultado
        result = function_to_execute(*map(read_combinations_from_file, combinations))
        # Calcula o custo
        cost = calculate_cost(len(result))
        print(f"Custo {function_name.upper()}: {cost}")
        print(f"Tempo de execução do Programa {function_name.upper()}: {timer} segundos")
    else:
        print("Função desconhecida:", function_name)

if __name__ == "__main__":
    main()
