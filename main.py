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

# We then add edges to the graph. For this, we first fill in a list moves: 
#   moves[i] are the numbers of cells where a knight can move from the i-th cell.
moves = [[] for _ in range(8)]
moves[0] = [4, 6]
moves[1] = [5, 7]
moves[2] = [3, 6]
moves[3] = [2, 7]
moves[4] = [0, 5]
moves[5] = [1, 4]
moves[6] = [0, 2]
moves[7] = [1, 3]

# Adding edges to the graph:
for node in G.nodes():
    configuration = [c for c in node]

    # loop over all configuration's items 
    for i in range(8):
        if configuration[i] == '*':
            continue
        for new_pos in moves[i]:
            if configuration[new_pos] != '*':
                continue
            new_configuration = configuration.copy()
            new_configuration[i] = '*'
            new_configuration[new_pos] = configuration[i]
            if not G.has_edge(node, "".join(new_configuration)):
                G.add_edge(node, "".join(new_configuration))
