# import networkx as nx
# import matplotlib.pyplot as plt
#
# G = nx.DiGraph()
# G.add_node(0), G.add_node(1), G.add_node(2), G.add_node(3), G.add_node(4)
# G.add_edge(0, 1), G.add_edge(1, 2), G.add_edge(0, 2), G.add_edge(1, 4), G.add_edge(1, 3), G.add_edge(3, 2), G.add_edge(
#     3, 1), G.add_edge(4, 3), G.add_edge(0, 0, name="x")
#
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()

import graphviz

f = graphviz.Digraph('finite_state_machine', filename='fsm.gv')
f.attr(rankdir='LR', size='8,5')

f.attr('node', shape='doublecircle')
f.node('LR_0')
f.node('LR_3')
f.node('LR_4')
f.node('LR_8')

f.attr('node', shape='circle')
f.edge('LR_0', 'LR_2', label='SS(B)')
f.edge('LR_0', 'LR_1', label='SS(S)')
f.edge('LR_1', 'LR_3', label='S($end)')
f.edge('LR_2', 'LR_6', label='SS(b)')
f.edge('LR_2', 'LR_5', label='SS(a)')
f.edge('LR_2', 'LR_4', label='S(A)')
f.edge('LR_5', 'LR_7', label='S(b)')
f.edge('LR_5', 'LR_5', label='S(a)')
f.edge('LR_6', 'LR_6', label='S(b)')
f.edge('LR_6', 'LR_5', label='S(a)')
f.edge('LR_7', 'LR_8', label='S(b)')
f.edge('LR_7', 'LR_5', label='S(a)')
f.edge('LR_8', 'LR_6', label='S(b)')
f.edge('LR_8', 'LR_5', label='S(a)')

f.view()