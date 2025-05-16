import plotly.graph_objects as go
import igraph
from igraph import Graph, EdgeSeq
nr_vertices = 25
v_label = list(map(str, range(nr_vertices)))
G = Graph.Tree(nr_vertices, 2) # 2 é o número de filhos por nó
lay = G.layout('rt')
position = {k: lay[k] for k in range(nr_vertices)}
Y = [lay[k][1] for k in range(nr_vertices)]
M = max(Y)
es = EdgeSeq(G) # sequence of edges
E = [e.tuple for e in G.es] # list of edges
L = len(position)
Xn = [position[k][0] for k in range(L)]
Yn = [2*M-position[k][1] for k in range(L)]
Xe = []
Ye = []
for edge in E:
 Xe+=[position[edge[0]][0],position[edge[1]][0], None]
 Ye+=[2*M-position[edge[0]][1],2*M-position[edge[1]][1], None]
 labels = v_label
fig = go.Figure()
fig.add_trace(go.Scatter(x=Xe,
                         y=Ye,
                         mode='lines',
                         name='galho',
                         line=dict(color='rgb(0,0,0)', width=1),
                         hoverinfo='none'))
fig.add_trace(go.Scatter(x=Xn,
                        y=Yn,
                        mode='markers',
                        name='nó',
                        marker=dict( symbol='circle-dot',
                                    size=18,
                                    color='#FF0000',
                                    line=dict(color='rgb(255,127,127)',
                                    width=1)
                                    ),
                        text=labels,
                        hoverinfo='text',
                        opacity=1))
fig.show()
