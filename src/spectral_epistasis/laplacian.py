#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import xgi

def spectral_gap(H, normalize=False):
    """
    Parameters
    ----------
    H : Hypergraph
        A hypergraph is a collection of subsets of a set of nodes
        or vertices.
    normalize : Boolean
        A boolean indicating whether or not the spectral gap will be
        normalized by the size of the graph.

    Returns
    -------
    spectral_gap : Float
        Scalar representing the spectral gap of the hypergraph.


    Note
    ----
    The laplacian calculated by Zhou et al. (2006) is expected 
    to be exactly half the laplacian of a the traditional dyadic
    graph since the D_{e}^{-1} the diagonal matrix of hyperedge 
    degrees would act as an identity matrix scaled by a factor of 
    one half.

    Since lambda_0 is expected to be 0 for a connected graph the 
    spectral gap is just lambda_1 not lambda_1 - lambda_0
    """

    L = xgi.normalized_hypergraph_laplacian(H, weighted=False, sparse=False)
    eigenvalues = np.linalg.eigvalsh(L)
    eigenvalues = np.sort(eigenvalues)

    assert np.isclose(eigenvalues[0], 0, atol=1e-10), \
        f"Expected lambda_0 ≈ 0, got {eigenvalues[0]}"

    if normalize:
        spectral_gap = eigenvalues[1] / H.num_nodes
    else:
        spectral_gap = eigenvalues[1]
    
    return spectral_gap
