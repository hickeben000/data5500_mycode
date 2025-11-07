'''
Easy: (5 points)

Write a Python function that takes a NetworkX graph as input 
and returns the number of nodes in the graph.
'''

import networkx as nx   # good graph library 
from networkx.classes.function import path_weight
import os

def count_nodes(g):
    return g.number_of_nodes()

curr_dir = os.path.dirname(__file__) # get the current directory of this file; useful trick 
edges_fil = curr_dir + "/" + "hwEdges.txt" # dirname and __file__ (this file) returns the current folder

file = open(edges_fil) 

g = nx.DiGraph() # created empty directed graph: g is the object; DiGraph is the class; nx is python module/library

# You never explicitly tell NetworkX what the nodes are.
# Instead — NetworkX figures it out automatically from the edges you add.

edges = []
for line in file.readlines():
    node1, node2, weight = line.split(",")
    weight = float(weight)
    edges.append((node1, node2, weight)) # edges = [("A", "B", 4.0), ("A", "C", 2.0)...

g.add_weighted_edges_from(edges) # This function does two things automatically:
                                    # 1. Adds each edge with its weight, and
                                    # 2. Creates any nodes that appear in those edges.

print("Number of nodes:", count_nodes(g))


'''
ChatGPT prompts: 
- don't give me the code because i want to try it on my on first but
    still give me a NetworkX graph to use as i practice code to make graphs. 

- print("these are nodes", g.nodes) this there a function to count the nodes in this list? 
    or do i need to create a for loop? 

- Write a Python function that takes a NetworkX graph as input 
    and returns the number of nodes in the graph.
    how would you solve this question

- where should i put this function in my code? what's best practice?
'''