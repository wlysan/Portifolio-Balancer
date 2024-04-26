from random import random
import matplotlib.pyplot as plt

# Class representing a financial asset
class Asset():
    def __init__(self, name, variation, beta, risk):
        self.name = name
        self.variation = variation
        self.beta = beta
        self.risk = risk

# Class representing an individual in the genetic algorithm population
class Individual():
    def __init__ (self, variations, betas, risks, limit_condition, portfolio_size, max_risk, generation = 0):
        self.variations = variations
        self.betas = betas
        self.risks = risks
        self.limit_condition = limit_condition
        self.generation = generation
        self.chromosome = []
        self.portfolio_size = portfolio_size
        self.max_risk = max_risk
        
        self.avg_risks = 0
        self.avg_betas = 0
        self.avg_variations = 0
        self.risk_sum = 0
        self.fitness_score = 0
        
        # Initialization of the individual's chromosome with random values
        for i in range(len(self.variations)):
            if random() < 0.5:
                self.chromosome.append("0")
            else:
                self.chromosome.append("1")

    # Function to evaluate the individual
    def evaluate(self):
        score = 0
        beta_sum = 0
        count = 0
        risk_sum = 0
        
        # Evaluation of the chromosome and calculation of metrics
        for i in range(len(self.chromosome)):
            if self.chromosome[i] == '1':
                score += self.variations[i]
                beta_sum += self.betas[i]
                risk_sum += self.risks[i]
                count += 1
                
        if count > 0:
            avg_beta = beta_sum / count
            avg_risk = risk_sum / count
            avg_variation = score / count
        else:
            avg_beta = 0
            avg_risk = 0
            avg_variation = 0
        
        # Application of limit conditions
        if avg_beta > 1.9:
            score = 1            
        if count > portfolio_size:
            score = 1
        if avg_risk > max_risk:
            score = 1 
            
        self.fitness_score = score
        self.risk_sum = risk_sum
        self.avg_betas = avg_beta
        self.avg_risks = avg_risk
        self.avg_variations = avg_variation
    
    # Crossover operator between two individuals
    def crossover(self, other_individual):
        cutting_point = round(random() * len(self.chromosome))
        
        child1 = other_individual.chromosome[0:cutting_point] + self.chromosome[cutting_point::]
        child2 = self.chromosome[0:cutting_point] + other_individual.chromosome[cutting_point::]
        
        children = [Individual(self.variations, self.betas, self.risks, self.limit_condition,
                            self.portfolio_size, self.max_risk, self.generation + 1),
                  Individual(self.variations, self.betas, self.risks, self.limit_condition, 
                            self.portfolio_size, self.max_risk, self.generation + 1)]
        
        children[0].chromosome = child1
        children[1].chromosome = child2
        
        return children

    # Mutation operator of the individual
    def mutate(self, mutation_rate):
        for i in range(len(self.chromosome)):
            if random() < mutation_rate:
                if self.chromosome[i] == '1':
                    self.chromosome[i] = '0'
                else:
                    self.chromosome[i] = '1'
        return self

# Class implementing the genetic algorithm
class GeneticAlgorithm():
    def __init__(self, population_size):
        self.population_size = population_size
        self.population = []
        self.generation = 0
        self.best_solution = 0
     
    # Initialization of the initial population
    def initialize_population(self, variations, betas, risks, limit_condition, portfolio_size, max_risk):
        for i in range(self.population_size):
            self.population.append(Individual(variations, betas, risks, limit_condition, portfolio_size, max_risk))
        self.best_solution = self.population[0]
        
    # Sorts the population based on the individuals' evaluation
    def sort_population(self):
        best_distance = self.best_solution.fitness_score / self.best_solution.avg_risks
        distance = 0
        for i in range(len(self.population)):
            if self.population[i].avg_risks > 0:
                distance = self.population[i].fitness_score / self.population[i].avg_risks
                if distance > best_distance:
                    self.population[0] = self.population[i]       
        
    # Sorts the population in descending order according to the individuals' evaluation
    def sort_population2(self):
        self.population = sorted(self.population, key = lambda individual: individual.fitness_score, reverse = True)
    
    # Updates the best solution found
    def best_individual(self, individual):
        if individual.fitness_score > self.best_solution.fitness_score:
            self.best_solution = individual
    
    # Calculates the sum of evaluations of the entire population
    def evaluate_sum(self):
        total_sum = 0
        for individual in self.population:
            total_sum += individual.fitness_score
        return total_sum
    
    # Selects a parent from the population based on fitness-weighted roulette wheel
    def select_parent(self, evaluation_sum):
        parent_index = -1
        draw_value = random() * evaluation_sum
        sum_so_far = 0
        i = 0
        while i < len(self.population) and sum_so_far < draw_value:
            sum_so_far += self.population[i].fitness_score
            parent_index += 1
            i += 1
        return parent_index
    
    # Visualizes the best solution found in a given generation
    def visualize_generation(self):
        best_individual = self.population[0]
        print("Generation = %s Score = %s Chromosome = %s" % (self.population[0].generation, best_individual.fitness_score,
                                                      best_individual.chromosome))
    
    # Executes the genetic algorithm to solve the problem
    def solve(self, mutation_rate, num_generations, variations, betas, risks, limit_condition,
                 portfolio_size, max_risk):
        self.initialize_population(variations, betas, risks, limit_condition, portfolio_size, max_risk)
        
        for individual in self.population:
            individual.evaluate()
        
        self.sort_population()
        
        for generation in range(num_generations):
            evaluation_sum = self.evaluate_sum()
            new_population = []
            
            for generated_individuals in range(0, self.population_size, 2):
                parent1 = self.select_parent(evaluation_sum)
                parent2 = self.select_parent(evaluation_sum)
                
                children = self.population[parent1].crossover(self.population[parent2])
                
                new_population.append(children[0].mutate(mutation_rate))
                new_population.append(children[1].mutate(mutation_rate))
                
            self.population = list(new_population)
            
            for individual in self.population:
                individual.evaluate()
            
            self.sort_population()
            
            best_individual = self.population[0]
            
            self.best_individual(best_individual)
            
        if self.best_solution.fitness_score == 1:
            print("A valid solution was not found")
        else:            
            print("\n Best Solution: \nGeneration = %s,\nScore = %s, \nVariation = %s, \nBeta = %s, \nRisk = %s, \nChromosome = %s" % 
                  (self.best_solution.generation,
                   self.best_solution.fitness_score,
                   self.best_solution.avg_variations,
                   self.best_solution.avg_betas,
                   self.best_solution.avg_risks,
                   self.best_solution.chromosome))
    
        return self.best_solution.chromosome

# Main function
if __name__ == '__main__':
    # Definition of financial assets
    asset_list = []
    
    asset_list.append(Asset("ITUB", 2.8, 1.06, 1.4))
    asset_list.append(Asset("ITSA", 2.019, 1.09, 1.009))
    asset_list.append(Asset("CSAN", 39.28, 0.94, 19.14))
    asset_list.append(Asset("CSNA", 58.33, 1.3, 29.165))
    asset_list.append(Asset("GGBR", 25.3, 1.6, 12.65))
    asset_list.append(Asset("EMBR", 288.04, 0.73, 144.02))
    asset_list.append(Asset("WEGE", 1.5, 0.52, 0.75))
    asset_list.append(Asset("TAEE", 31.84, 0.51, 15.92))
    asset_list.append(Asset("VALE", 32.5, 0.51, 16.25))
    asset_list.append(Asset("LAME", -8.146, 1.19, 4.073))
    asset_list.append(Asset("MGLU", -41.33, 0.99, 20.665))
    asset_list.append(Asset("PRIO", 290.64, 1.64, 145.32))
    asset_list.append(Asset("PETR", 48.08, 1.56, 17))
    # Add other assets here...
    
    # Extraction of asset characteristics
    variations = []
    betas = []
    names = []
    risks = []
    
    for asset in asset_list:
        variations.append(asset.variation)
        betas.append(asset.beta)
        risks.append(asset.risk)
        names.append(asset.name)
    
    # Limit condition for assets
    condition = [">=", "beta", 1.1]    
    
    # Parameters of the genetic algorithm
    population_size = 250
    mutation_rate = 0.10
    num_generations = 250
    max_risk = 25
    portfolio_size = 7
    
    # Creation and execution of the genetic algorithm
    ga = GeneticAlgorithm(population_size)
    
    result = ga.solve(mutation_rate, num_generations, variations, betas, risks, condition, 
                            portfolio_size, max_risk)
    
    for i in range(len(result)):
        if result[i] == '1':
            print("Asset Name = %s" % asset_list[i].name)
