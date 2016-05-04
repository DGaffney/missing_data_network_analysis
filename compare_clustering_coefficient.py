import networkx as nx
import numpy as np
#!/usr/bin/python
#only works with python 2.6+
#usage python compare_clustering_coefficient.py [infile_name] [cut_count] [directed(true|false)]
import sys
import igraph
import csv
directed = sys.argv[3] == "true"
cut_count = int(sys.argv[2])
G = nx.read_edgelist("data/soc-Epinions1.txt", delimiter='\t', nodetype=str)

def run(G, cut_count, iterations=10):
  print nx.average_clustering(G)
  nodes = G.nodes()
  edges = G.edges()
  for i in range(iterations):
    np.random.shuffle(nodes)
    selected_nodes = nodes[0:-cut_count]
    not_selected_nodes = set(nodes)-set(selected_nodes)
    not_selected_edges = G.subgraph(not_selected_nodes).edges()
    H = G.subgraph(nodes)
    H.remove_edges_from(not_selected_edges)
    H.remove_nodes_from(list(set(not_selected_nodes)&set(nx.isolates(H))))
    print nx.average_clustering(H)

run(G, cut_count, iterations=10)
