import networkx as nx
import itertools as it

G = nx.Graph()
# We now start creating the graph of all configurations.
# Below, we iterate through all possible strings of length 8
# with two W's and two B's. For this, we iterate through all 
# possible four indices of W's and B's (out of eight possible positions).
for wb_indices in it.permutations(range(8), 4):
    configuration = ['*'] * 8
    configuration[wb_indices[0]] = 'W'
    configuration[wb_indices[1]] = 'W'
    configuration[wb_indices[2]] = 'B'
    configuration[wb_indices[3]] = 'B'

    G.add_node("".join(configuration))
