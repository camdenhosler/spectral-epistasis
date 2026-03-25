#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from spectral_epistasis.laplacian import spectral_gap
from spectral_epistasis.knockout import knockout_nodes

def epistasis_coef(H, node_A, node_B, normalize=False):
    """
    Parameters
    ----------
    H : Hypergraph
        A hypergraph is a collection of subsets of a set of nodes
        or vertices.
    node_A: Integer
        Integer denoting which node will be knocked out.
    node_B: Integer
        Integer denoting which node will be knocked out.
    normalize : Boolean
        A boolean indicating whether or not the epistatic coeffiecent will 
        be normalized by the size of the graph.
    Returns
    -------
    eps : Float
        The epistatic coeffiecent.
    """
    HA = knockout_nodes(H, [node_A])
    HB = knockout_nodes(H, [node_B])
    HAB = knockout_nodes(H, [node_A,node_B])

    s_H = spectral_gap(H,normalize)
    s_HA = spectral_gap(HA,normalize)
    s_HB = spectral_gap(HB,normalize)
    s_HAB = spectral_gap(HAB,normalize)

    eps = s_HAB  - s_HA - s_HB + s_H
    return eps

def epistasis_matrix(H, normalize=False):
    """
    Parameters
    ----------
    H : Hypergraph
        A hypergraph is a collection of subsets of a set of nodes
        or vertices.
    normalize : Boolean
        A boolean indicating whether or not the epistatis matrix will 
        be normalized by the size of the graph.
    Returns
    -------
    matrix : n x n ndarray
        A symmetric matrix where each i j entry corresponds to the 
        epistatic coeffecient of node i and j.  Where a np.nan
        entry is left for undefined values (when the graph is 
        disconnected).
    """

    nodes = list(H.nodes)
    n = len(nodes)
    matrix = np.full((n, n), np.nan)

    for i in range(n):
        for j in range(i, n):
            try:
                if i != j:
                    eps = epistasis_coef(H, nodes[i], nodes[j], normalize)
                else:
                    eps = 0
                matrix[i, j] = eps
                matrix[j, i] = eps

            except AssertionError:
                pass

    return matrix, nodes