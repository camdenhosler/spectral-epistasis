import xgi
import numpy as np
from scipy.linalg import sqrtm, inv

# Build a simple hypergraph with one hyperedge containing 3 nodes
H = xgi.Hypergraph()
H.add_nodes_from([0, 1, 2])
H.add_edge([0, 1])
H.add_edge([1, 2])

#Zhou et al. 2006 lapacian
L = xgi.normalized_hypergraph_laplacian(H, weighted=False, sparse=False)

A = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
D = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 1]])

D_nhalf = np.diag(1.0 / np.sqrt(np.diag(D)))
L_graph = 0.5 * (np.eye(3) - D_nhalf @ A @ D_nhalf)

eigenvalues = np.linalg.eigvalsh(L_graph)
eigenvalues = np.sort(eigenvalues)

print(L)
print(L_graph)
print(eigenvalues[1])