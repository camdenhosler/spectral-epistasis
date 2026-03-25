#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import xgi
from spectral_epistasis.epistasis import epistasis_matrix
from spectral_epistasis.visualization import generate_heatmap

H = xgi.Hypergraph()
H.add_nodes_from([0, 1, 2, 3, 4, 5])
H.add_edges_from([[0,1],[1,2],[2,3],[3,4],[4,5],[5,0]])

eps_matrix, nodes = epistasis_matrix(H)

generate_heatmap(eps_matrix, nodes)