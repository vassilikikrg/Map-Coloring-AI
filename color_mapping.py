import random

nodes = [i for i in range(16)]
colors = ['B', 'R', 'G', 'Y']
edges = [(0, 1), (0, 2), (0, 3), (0, 12), (0, 14), (0, 15), (1, 2), (1, 4), (1, 8), (1, 7), (1, 13), (1, 14), (1, 15), (2, 3), (2, 4), (2, 5), (3, 5), (4, 5), (4, 6), (4, 8), (4, 9),
         (5, 6), (5, 10), (5, 12), (6, 9), (6, 10), (7, 8), (7, 13), (8, 9), (8, 11), (8, 13), (9, 10), (9, 11), (10, 11), (10, 12), (11, 12), (11, 13), (11, 14), (12, 14), (13, 14), (14, 15)]
population = {}
# if the fitness is equal to the fitness goal, then the solution is found
fitness_goal = len(edges)
N = 10  # size of the population


#                                                       #
# Fitness function to evaluate each candidate solutions #
#                                                       #
def fitness_function(solution):
    fitness = 0
    for i in range(len(edges)):
        # if the colors of the connected nodes are different
        if solution[edges[i][0]] != solution[edges[i][1]]:
            fitness += 1
    return fitness


#                   #
# Parent selection  #
#                   #
def roulette_selection(population):
    # Compute the total fitness of the population
    total_fitness = sum(population.values())

    # Generate a random number between 0 and the total fitness
    spin = random.uniform(0, total_fitness)

    # Iterate over the solutions and accumulate their fitness scores until we reach the selected number
    accumulated_fitness = 0
    for solution, sol_fitness in population.items():
        accumulated_fitness += sol_fitness
        if accumulated_fitness >= spin:
            # Return the selected solution
            return solution

    # If no solution has been selected, return None
    return None

#
# Reproduction (using single-point crossover)
#


def crossover(parent1, parent2):
    n = len(parent1)
    child1 = parent1[:n//2]+parent2[n//2:]
    child2 = parent2[:n//2]+parent1[n//2:]
    return child1, child2

#
# Initialization of the population
#
def initialize(N, nodes, colors):
    population = {}
    for i in range(N):
        s = "".join(random.choice(colors) for i in range(len(nodes)))
        population[s] = fitness_function(s)
    return population

def algorithm(N, nodes, colors, fitness_goal):
    # random initial population (size=10)
    population = initialize(N, nodes, colors)

    counter = 0
    # while the fitness is not equal to the fitness goal
    while (max(population.values()) < fitness_goal and counter < 20000):
        counter += 1
        for j in range(N//2):
            # select two parents
            parent1 = roulette_selection(population)
            parent2 = roulette_selection(population)
            # crossover
            child1, child2 = crossover(parent1, parent2)
            # mutate
            # child1=mutate(child1)
            # child2=mutate(child2)
            # evaluate the fitness of the children
            population[child1] = fitness_function(child1)
            population[child2] = fitness_function(child2)
        # select the best 10 solutions
        population = dict(sorted(population.items(),
                          key=lambda item: item[1], reverse=True)[:10])
    max_value = max(population.values())
    print("The best solution/solutions with a fitness score of: "+str(max_value))
    print([k for k,v in population.items() if v == max_value])
    


algorithm(N, nodes, colors, fitness_goal)
