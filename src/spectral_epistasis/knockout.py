#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import xgi

def knockout_nodes(H, nodes):
    """
    Parameters
    ----------
    H : Hypergraph
        A hypergraph is a collection of subsets of a set of nodes
        or vertices.
    nodes: List of integers
        A list of integers denoting which nodes will be knocked out.
        
    Returns
    -------
    H_sub : Hypergraph
        A hypergraph without the specified node.
    """

    nodes_without = [n for n in H.nodes if n not in set(nodes)]
    H_sub = xgi.subhypergraph(H, nodes_without) 

    return H_sub
