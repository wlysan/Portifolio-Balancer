# Algoritmo Genético para Otimização de Portfólio de Ativos Financeiros

Este projeto implementa um algoritmo genético para otimizar a seleção de um portfólio de ativos financeiros com base em variáveis como variação, beta e risco. O objetivo é encontrar uma combinação de ativos que maximize a variação esperada do portfólio, respeitando restrições de beta e risco.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `random` (incluída na biblioteca padrão do Python)
  - `matplotlib` (para visualização, embora não utilizada diretamente no código atual)

## Como Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/wlysan/Portifolio-Balancer.git
    cd Portifolio-Balancer
    ```

2. Instale as dependências necessárias:
    ```bash
    pip install matplotlib
    ```

3. Execute o script:
    ```bash
    python main.py
    ```

## Estrutura do Código

### Classes

#### `Asset`
Representa um ativo financeiro.
- **Parâmetros:**
  - `name` (str): Nome do ativo.
  - `variation` (float): Variação esperada do ativo.
  - `beta` (float): Beta do ativo.
  - `risk` (float): Risco do ativo.

#### `Individual`
Representa um indivíduo na população do algoritmo genético.
- **Parâmetros:**
  - `variations` (list): Lista de variações dos ativos.
  - `betas` (list): Lista de betas dos ativos.
  - `risks` (list): Lista de riscos dos ativos.
  - `limit_condition` (list): Condição de limite para os ativos.
  - `portfolio_size` (int): Tamanho máximo do portfólio.
  - `max_risk` (float): Risco máximo permitido para o portfólio.
  - `generation` (int): Geração do indivíduo (padrão é 0).

- **Métodos:**
  - `__init__()`: Inicializa o indivíduo com um cromossomo aleatório.
  - `evaluate()`: Avalia o indivíduo calculando métricas como média de beta, risco e variação, além de aplicar as condições de limite.
  - `crossover(other_individual)`: Realiza o cruzamento entre dois indivíduos, retornando dois filhos.
  - `mutate(mutation_rate)`: Realiza a mutação do indivíduo com base em uma taxa de mutação.

#### `GeneticAlgorithm`
Implementa o algoritmo genético.
- **Parâmetros:**
  - `population_size` (int): Tamanho da população.

- **Métodos:**
  - `__init__()`: Inicializa a população e define a melhor solução.
  - `initialize_population()`: Inicializa a população de indivíduos.
  - `sort_population()`: Ordena a população com base na avaliação dos indivíduos.
  - `sort_population2()`: Ordena a população em ordem decrescente com base na avaliação.
  - `best_individual(individual)`: Atualiza a melhor solução encontrada.
  - `evaluate_sum()`: Calcula a soma das avaliações de toda a população.
  - `select_parent(evaluation_sum)`: Seleciona um pai da população com base na roleta ponderada pela aptidão.
  - `visualize_generation()`: Visualiza a melhor solução encontrada em uma determinada geração.
  - `solve()`: Executa o algoritmo genético para resolver o problema de otimização do portfólio.

## Parâmetros do Algoritmo

- **Ativos Financeiros**: Definidos na lista `asset_list`.
- **População Inicial**: 250 indivíduos.
- **Taxa de Mutação**: 10% (0.10).
- **Número de Gerações**: 250.
- **Risco Máximo Permitido**: 25.
- **Tamanho Máximo do Portfólio**: 7 ativos.

## Exemplo de Uso

O código define uma lista de ativos financeiros com suas respectivas variações, betas e riscos. Em seguida, o algoritmo genético é configurado e executado para encontrar a melhor combinação de ativos que maximize a variação esperada do portfólio, respeitando as restrições de beta e risco.

O resultado final imprime a melhor solução encontrada, incluindo a geração, pontuação, variação média, beta médio, risco médio e o cromossomo correspondente. Além disso, os nomes dos ativos selecionados no melhor portfólio também são impressos.

## Resultados

O script imprime a melhor solução encontrada após executar o algoritmo genético, exibindo informações detalhadas sobre o portfólio otimizado.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou novos recursos. Faça um fork do projeto, crie uma branch para suas alterações e envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Genetic Algorithm for Financial Asset Portfolio Optimization

This project implements a genetic algorithm to optimize the selection of a financial asset portfolio based on variables such as variation, beta, and risk. The goal is to find a combination of assets that maximizes the expected variation of the portfolio while respecting constraints on beta and risk.

## Requirements

- Python 3.x
- Libraries:
  - `random` (included in Python's standard library)
  - `matplotlib` (for visualization, although not directly used in the current code)

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/wlysan/Portifolio-Balancer.git
    cd Portifolio-Balancer
    ```

2. Install the required dependencies:
    ```bash
    pip install matplotlib
    ```

3. Run the script:
    ```bash
    python main.py
    ```

## Code Structure

### Classes

#### `Asset`
Represents a financial asset.
- **Parameters:**
  - `name` (str): Name of the asset.
  - `variation` (float): Expected variation of the asset.
  - `beta` (float): Beta of the asset.
  - `risk` (float): Risk of the asset.

#### `Individual`
Represents an individual in the genetic algorithm's population.
- **Parameters:**
  - `variations` (list): List of asset variations.
  - `betas` (list): List of asset betas.
  - `risks` (list): List of asset risks.
  - `limit_condition` (list): Constraint for the assets.
  - `portfolio_size` (int): Maximum portfolio size.
  - `max_risk` (float): Maximum allowed risk for the portfolio.
  - `generation` (int): Individual's generation (default is 0).

- **Methods:**
  - `__init__()`: Initializes the individual with a random chromosome.
  - `evaluate()`: Evaluates the individual by calculating metrics such as average beta, risk, and variation, and applying constraint conditions.
  - `crossover(other_individual)`: Performs crossover between two individuals, returning two offspring.
  - `mutate(mutation_rate)`: Mutates the individual based on a mutation rate.

#### `GeneticAlgorithm`
Implements the genetic algorithm.
- **Parameters:**
  - `population_size` (int): Population size.

- **Methods:**
  - `__init__()`: Initializes the population and sets the best solution.
  - `initialize_population()`: Initializes the population of individuals.
  - `sort_population()`: Sorts the population based on individuals' evaluation.
  - `sort_population2()`: Sorts the population in descending order based on evaluation.
  - `best_individual(individual)`: Updates the best solution found.
  - `evaluate_sum()`: Calculates the sum of evaluations for the entire population.
  - `select_parent(evaluation_sum)`: Selects a parent from the population using a fitness-weighted roulette wheel.
  - `visualize_generation()`: Visualizes the best solution found in a given generation.
  - `solve()`: Executes the genetic algorithm to solve the portfolio optimization problem.

## Algorithm Parameters

- **Financial Assets**: Defined in the `asset_list`.
- **Initial Population**: 250 individuals.
- **Mutation Rate**: 10% (0.10).
- **Number of Generations**: 250.
- **Maximum Allowed Risk**: 25.
- **Maximum Portfolio Size**: 7 assets.

## Usage Example

The code defines a list of financial assets with their respective variations, betas, and risks. Then, the genetic algorithm is configured and executed to find the best combination of assets that maximizes the expected portfolio variation while respecting beta and risk constraints.

The final result prints the best solution found, including the generation, score, average variation, average beta, average risk, and the corresponding chromosome. Additionally, the names of the selected assets in the best portfolio are also printed.

## Results

The script prints the best solution found after executing the genetic algorithm, displaying detailed information about the optimized portfolio.

## Contribution

Feel free to contribute with improvements or new features. Fork the project, create a branch for your changes, and submit a pull request.

## License

This project is licensed under the MIT License.
