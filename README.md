# Analysis-of-Lotofacil-subsets

Este projeto executa análises em conjuntos de dados de combinações numéricas.

## Configuração do Projeto

Certifique-se de ter o Python instalado em sua máquina.

1. **Clone este repositório:**

   ```
   git clone https://github.com/marcelowf/Analysis-of-Lotofacil-subsets.git
   ```

2. **Instale as dependências:**

   ```
   pip install -r requirements.txt
   ```

3. **Certifique-se de ter a estrutura de diretórios:**

   ```
   Data_Analysis/
       __init__.py
       Analysis_Helper/
           __init__.py
           Data_Reader.py
           Cost_Calculator.py
           Time_Counter.py
       SB15_14.py
       SB15_13.py
       SB15_12.py
       SB15_11.py
   
   Data_Generator/
       Data_Generator.py
   
   Data_Logs/
         ...
   
   Main.py
   ```

4. **Certifique-se de gerar os seguintes arquivos de dados:**

   ```
   Data_Logs/
       combinations_15.txt
       combinations_14.txt
       combinations_13.txt
       combinations_12.txt
       combinations_11.txt
   ```

## Utilização

Para executar o programa, abra um terminal e navegue até o diretório raiz do projeto.

Para chamar uma função específica, utilize o seguinte comando:

```
python main.py <função>
```

Substitua `<função>` pelo nome da função que você deseja chamar. Por exemplo:

```
python main.py sb15_14
```

Isso executará a função `sb15_14`, mostrando o custo e o tempo de execução.

## Autores

Marcelo Wzorek Filho