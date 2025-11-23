import json 
import os
import pandas as pd 
import requests
import networkx as nx
from itertools import permutations
import matplotlib.pyplot as plt


url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum,bitcoin,litecoin,ripple,bitcoin-cash,eos&vs_currencies=eth,btc,ltc,xrp,bch,eos"
req = requests.get(url)
df = json.loads(req.text)
g =  nx.DiGraph() # make empty graph named g
edges = [] # empty list to put edges in

coin_to_ticker = {  # to convert coins to tickers to meet assignment examples
    "bitcoin": "btc",
    "bitcoin-cash": "bch",
    "cardano": "ada",
    "eos": "eos",
    "ethereum": "eth",
    "litecoin": "ltc",
    "ripple": "xrp",
} 

for coin, symbol in df.items(): # loop through df json and gets keys (full crypto names) and values (dictionaries within the names)
    target_ticker = coin_to_ticker[coin]    # converts full crypto names to tickers 
    for ticker, weight in symbol.items():   # loops through each value / dictionary (full crypto names) and pulls out ticker and weight
        weight = float(weight)  
        edges.append((target_ticker, ticker, weight))   # adds nodes and weight between nodes to edges list
        # g.add_weighted_edges_from([(coin, ticker, weight)]) 

g.add_weighted_edges_from(edges)    # calls function to for graph from edges list 

min_factor = 5  # initializing min and max factor to print at end
max_factor = 0

for n1, n2 in permutations(g.nodes,2): # order does matter - btc to eth is different weight than from eth to btc; ,2 take two nodes at a time
    print("paths from",n1,"to", n2,"-"*50)

    for path in nx.all_simple_paths(g, source=n1, target=n2):   # loops and finds all paths from n1 and n2
        path_weight = 1 # not =0; anything multiplied by 1 will be itself
        for i in range(len(path) - 1):  # len(path)-1 because there are 4 edges in 5 nodes
            path_weight *= g[path[i]][path[i+1]]['weight']  # multipying edges to find the path weight

    for rev_path in nx.all_simple_paths(g, source=n2, target=n1):   # same logic as previous nest for loops, just changing source and target nodes
        rev_path_weight = 1
        for j in range(len(rev_path)-1):
            rev_path_weight *= g[rev_path[j]][rev_path[j+1]]['weight'] 

        print(path, path_weight)
        print(rev_path, rev_path_weight)

        weights_factor = (path_weight) * (rev_path_weight)  # multiplying weights to get factor
        print(weights_factor)

        if weights_factor < min_factor:     # keeps track of smallest factor by setting min_factor to the weight
            min_factor = weights_factor 
            min_path = path                 # min_path variable to keep track of path
            min_rev_path = rev_path
        
        if weights_factor > max_factor:
            max_factor = weights_factor
            max_path = path
            max_rev_path = rev_path

print("Smallest Paths weight factor:", min_factor)      # print out smallest and greatest paths
print("Paths:", min_path, min_rev_path) 

print("Greatest Paths weight factor:", max_factor)
print("Paths:", max_path, max_rev_path) 
