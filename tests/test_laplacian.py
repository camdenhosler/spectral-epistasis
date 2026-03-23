import xgi
import numpy as np
from spectral_epistasis.laplacian import spectral_gap

def test_spectral_gap_path_hypergraph():
    H = xgi.Hypergraph()
    H.add_nodes_from([0, 1, 2])
    H.add_edge([0, 1])
    H.add_edge([1, 2])
    
    gap = spectral_gap(H)
    assert np.isclose(gap, 0.5, atol=1e-6)

