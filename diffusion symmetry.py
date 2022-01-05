'''random_walk.py'''
'''
 the diffusion symmetry(physics) group of a graph
 C[k][n] denote the number of times an element of the graph is visited under all random walk of size k
Ci denote variables 
Di[k] denote nodes with distance k from s=0

'''
import math
import networkx as nx
from sympy import symbols, Eq
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import random

def diffusion(g, k):
    '''
    define the diffusion sequence
    '''
    s = 0
    res = defaultdict()
    res[0] = s,
    for i in np.arange(k):
        res[i+1] = []
    for i in np.arange(k):
        for s in res[i]:
            for n in g.neighbors(s):
                res[i+1].append(n)

    return res

def build_chain(res, n, k):
    '''
    Construct a chain that count the number of time a node s is visited after k diffusion
    '''
    C = defaultdict()
    for i in np.arange(k+1):
        C[i] = defaultdict()
        for j in np.arange(n):
            C[i][j] = res[i].count(j)
    return C

def random_walk(g, k):
    '''
    return a k-size random walk graph from a graph g
    '''
    h = nx.Graph()
    h.add_nodes_from(g)
    s = 0
    for i in np.arange(k):
        r = random.choice(g.edges(s))
        h.add_edge(s, r[1])
        s = r[1]
    plt.figure(f"random_walk")
    pos = nx.circular_layout(h)
    nx.draw(h, pos, with_labels = True, node_color = "red", edge_color = "blue")
    return h

def build_variables(g, C, k, n):
    '''
    build variables for the algebra of diffusion symmetry
    '''
    Ci = np.array()
    for i in np.arange(k+1):
        np.append(Ci, [symbols(f"C{i}")])
    Di = []
    Di.append([0])
    tmp = np.array()
    np.append(tmp, [0])
    for i in np.arange(k):
        Di.append([])
        for j in Di[-2]:
            for s in g.neighbors(j):
                if s not in tmp:
                    Di[i+1].append(s)
                    np.append(tmp, [s])
    result = defaultdict()
    for i in np.arange(k):
            result[i] = defaultdict()
    for i in C:   # number of times j appears
        for j in np.arange(n):
            for m in np.arange(k+1):
                if j in D[m]:
                    #result
                    pass
                
n = int(input(f"graph size: "))
k = int(input(f"diffusion size: "))
#l = int(input(f"The node: "))
g = nx.fast_gnp_random_graph(n, 0.7)
plt.figure(f"graph")
pos = nx.circular_layout(g)
nx.draw(g, pos, with_labels = True, node_color = "blue", edge_color = "red")
print(f"nodes : {g.nodes}\n")
print(f"edges : {g.edges}\n")
res = diffusion(g, k)
C = build_chain(res, n, k)
print(f"C chain : ")
for i in np.arange(k+1):
    print(C[i])

h = random_walk(g, k)
build_variables(g, C, k, n)

