'''
Hard: (10 points)

  2. Write a Python function that takes a NetworkX graph as input and 
  returns the number of nodes in the graph that have a degree greater than 5
'''

import networkx as nx   # good graph library 
from networkx.classes.function import path_weight
import os

def count_nodes_5(g):
    numNodes5 = 0 
    for u, v in g.edges:
        weight = g[u][v]['weight']
        # print(weight)
        if weight > 5:
            # print(u, v)
            numNodes5 += 1 
    return numNodes5 


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

print("Number of nodes w/ degrees over 5:", count_nodes_5(g))


'''
ChatGPT prompts:
- how do i loop through a graph? 

- for i in g.edges:. this is showing me the edge by giving me the two nodes it's between. 
    How do i get the weight of this edge?

'''