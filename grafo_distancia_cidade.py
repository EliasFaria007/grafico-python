import matplotlib.pyplot as plt
import networkx as nx
G=nx.read_gml("../grafico-pyton/grafo.gml")
pos=nx.shell_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='#00c0c0', node_size=500, alpha=0.8)
labels=nx.draw_networkx_labels(G,pos,font_size=10)
edge_labels=nx.draw_networkx_edge_labels(G,pos,font_size=10)
plt.axis('off')
plt.show() 