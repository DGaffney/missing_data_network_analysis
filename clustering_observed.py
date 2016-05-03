import igraph
flights = [["ORD", "SEA"], ["ORD", "LAX"], ['ORD', 'DFW'], ['ORD', 'PIT'], ['SEA', 'LAX'], ['LAX', 'DFW'], ['ATL', 'PIT'], ['ATL', 'RDU'], ['RDU', 'PHL'], ['PIT', 'PHL'], ['PHL', 'PVD']]
gg = igraph.Graph(directed=False)
gg.add_vertices(list(set([item for sublist in flights for item in sublist])))
gg.add_edges(flights)

def clustering(graph, vs, os):
  results = []
  for v in vs:
    neighbor_ids = gg.neighbors(v)
    neighbor_ids.append(v)
    intra_neighbor_ties = [list(set.intersection(set(gg.neighbors(neighbor)), set(neighbor_ids))) for neighbor in neighbor_ids[0:-1]]
    o_count = len(list(set.intersection(set(gg.neighbors(v)), os)))
    if o_count == 0:
      
    (sum([len(el) for el in intra_neighbor_ties])-len(intra_neighbor_ties))/

  
  