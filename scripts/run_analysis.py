import xgi

H = xgi.Hypergraph()
H.add_nodes_from([0, 1, 2])

print(0 in H.nodes)
print(3 in H.nodes)