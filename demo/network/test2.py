import os
import json
import networkx as nx
import matplotlib.pyplot as plt


dir_root = os.getcwd()
sep = os.sep
path = sep.join([dir_root, 'test.json'])
print(path)
dependents = {}
nodes = []
edges = []
with open(path, 'r', encoding='utf8') as data:
    dependents_config = json.load(data)
    a = 0
    for db in dependents_config['databases']:
        a = a + len(db['tables'])
        for table in db['tables']:
            dependents["{}.{}".format(db['name'], table['name'])] = table['dependents']
            nodes.append("{}.{}".format(db['name'], table['name']))
            # d = len(table['dependents'])
            # if d == 0 or (d == 1 and table['dependents'][0] == table['name']):
            for dependent in table['dependents']:
                if dependent != table['name']:
                    tup = ("{}.{}".format(db['name'], table['name']), dependent)
                    edges.append(tup)


# print(dependents)
# print(nodes)
print("============={}============".format(a))
# print(edges)

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# nx.draw_networkx(G, with_labels=True)

print("")
print("不连通子图数：{}".format(nx.number_connected_components(G)))
print("==========不连通的子图==========")
n = 0
for c in nx.connected_components(G):
    # nodeSet = G.subgraph(c).nodes()
    # plot = plot + 1
    n = n + len(c)
    print("子图节点个数：{}".format(len(c)))
    print(c)
print("表的总量：{}".format(n))
