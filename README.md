# Map Coloring Problem
A solution written in Python for the Map Coloring problem using genetic algorithms. The aim is to select a color for each region of the graph from a given color palette (here is : blue, red, green, yellow)
so that all adjacent regions have different color.

In the program, a random starting population is used.
A fitness score is assigned to each candidate solution in order to be used as a quality measurement.
The fitness function calculates the number of adjacent nodes that have different color for each possible solution. Parents are selected using the 
[Roulette Wheel selection](https://en.wikipedia.org/wiki/Fitness_proportionate_selection) 
in which there is a higher probability for candidate solutions with a higher fitness to be selected as parent.
Then a [one-point crossover](https://en.wikipedia.org/wiki/Crossover_(genetic_algorithm)) is used to combine the pair of parents and produce the new population.
This process is repeated until a solution is found or the limit of repeats is exceeded.

## Installation

Simply clone the project to your local device and then open a terminal and run the script using the following command:

```
python color_mapping.py
```
## Prerequisites
[Python](https://www.python.org/) 3.9 or newer is needed.
### pip
 To install the needed dependencies if you are using pip, run:
 ```bash
pip install networkx matplotlib
```

This command will install the following modules:
* `networkx` (for creating and manipulating graphs and networks)
* `matplotlib` (for plotting)

## Example
For this graph:

![image](https://github.com/vassilikikrg/Map-Coloring-AI/assets/78561945/1bf137f8-c327-4883-a284-6f47c83073b8)

the colored output of the program is 

![image](https://github.com/vassilikikrg/Map-Coloring-AI/assets/78561945/0dc4fb2a-6e59-46b1-affa-eabdbd259b7c)
