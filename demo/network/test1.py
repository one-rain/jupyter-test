import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_node("tableA")
G.add_node("tableB")
G.add_node("tableC")
G.add_node("tableD")
G.add_node("tableE")
G.add_node("tableF")
G.add_node("tableG")

G.add_edge("tableA", "tableB")
G.add_edge("tableC", "tableB")
G.add_edge("tableB", "tableD")
G.add_edge("tableD", "tableE")
G.add_edge("tableD", "tableF")
G.add_edge("tableF", "tableG")

nx.draw_networkx(G)
# plt.title('有向无环图',fontproperties=myfont)
plt.show()
# print(list(reversed(list(nx.topological_sort(G)))))
