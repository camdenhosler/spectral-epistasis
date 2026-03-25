#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pylab as plt
import seaborn as sns

def generate_heatmap(eps_matrix, nodes, title=None):
    """
    Parameters
    ----------
    eps_matrix : nxn ndarray
        A symmetric matrix where each i j entry corresponds to the 
        epistatic coeffecient of node i and j.  Where a np.nan
        entry is left for undefined values (when the graph is 
        disconnected).
    nodes : List of integers
        A list of node "numbers" used to index nodes in the case that
        they don't form a continous sequence of integers.
    title : String
        A title of the heatmap.

    Returns
    -------
    None
    """

    ax = sns.heatmap(eps_matrix, 
                     cmap="RdBu_r", 
                     linewidth=0.5, 
                     center=0, 
                     xticklabels=nodes,
                     yticklabels=nodes)
    ax.set_facecolor('gray')

    if title:
        plt.title(title)
    
    plt.xlabel("Node")
    plt.ylabel("Node")
    plt.show()