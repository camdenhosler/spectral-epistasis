import xgi
import numpy as np
from spectral_epistasis.laplacian import spectral_gap
from spectral_epistasis.knockout import knockout_nodes
from spectral_epistasis.epistasis import epistasis_coef

def test_spectral_gap_on_simple_hypergraph():
    H = xgi.Hypergraph()
    H.add_nodes_from([0, 1, 2])
    H.add_edge([0, 1])
    H.add_edge([1, 2])
    
    gap = spectral_gap(H)

    #0.5 determined analytically
    assert np.isclose(gap, 0.5, atol=1e-6)

def test_knockout_removes_correct_nodes():
    H = xgi.Hypergraph()
    H.add_nodes_from([0, 1, 2])
    H.add_edges_from([[0,1], [1,2]])

    H_single = knockout_nodes(H, [0])
    H_double = knockout_nodes(H, [0,1])

    assert H.num_nodes == 3
    assert H.num_edges == 2

    assert H_single.num_nodes == 2
    assert H_single.num_edges == 1

    assert H_double.num_nodes == 1
    assert H_double.num_edges == 0

    assert 0 not in H_single.nodes
    assert 0 not in H_double.nodes
    assert 1 not in H_double.nodes

def test_epistasis_coef_complete_graph():
    H = xgi.Hypergraph()
    H.add_nodes_from([0, 1, 2, 3])
    H.add_edges_from([[0,1], [1,2], [2,3], [3,4]])

    eps = epistasis_coef(H,0,4)

    print(eps)

    assert np.isclose(eps, 0.15, atol=1e-2)