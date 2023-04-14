import random

nodes=[i for i in range(15)]
colors=['B','R','G','Y']
edges=[(1,2),(1,3),(1,4),(1,15)]
starting_population={}
fitness_goal=len(edges) #if the fitness is equal to the fitness goal, then the solution is found
N=10 #size of the population


#fitness function to evaluate each candidate solutions
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

#print(starting_population)

def parent_select(population):
    






