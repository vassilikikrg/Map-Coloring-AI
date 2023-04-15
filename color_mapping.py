import random

nodes=[i for i in range(15)]
colors=['B','R','G','Y']
edges=[(1,2),(1,3),(1,4),(1,15)]
starting_population={}
fitness_goal=len(edges) #if the fitness is equal to the fitness goal, then the solution is found
N=10 #size of the population

#                                                       #
# Fitness function to evaluate each candidate solutions #
#                                                       #
def fitness_function(solution):
    fitness=0
    for i in range(len(edges)):
        if solution[edges[i][0]]!=solution[edges[i][1]]:#if the colors of the connected nodes are different
            fitness+=1
    return fitness

#random initial population (size=10)
for i in range(N):
    s="".join(random.choice(colors) for i in range(len(nodes)))
    starting_population[s]=fitness_function(s)

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
    for sol_fitness in population.values():
        accumulated_fitness += sol_fitness
        if accumulated_fitness >= spin:
            # Return the selected solution
            return solution

    # If no solution has been selected, return None
    return None






