import igraph
flights = [["ORD", "SEA"], ["ORD", "LAX"], ['ORD', 'DFW'], ['ORD', 'PIT'], ['SEA', 'LAX'], ['LAX', 'DFW'], ['ATL', 'PIT'], ['ATL', 'RDU'], ['RDU', 'PHL'], ['PIT', 'PHL'], ['PHL', 'PVD']]
gg = igraph.Graph(directed=False)
gg.add_vertices(list(set([item for sublist in flights for item in sublist])))
gg.add_edges(flights)

def clustering_observed(graph, ovs):
    results = []
    for v in graph.vs:
        neighbor_ids = set(graph.neighbors(v))
        intra_neighbor_ties = sum([len(set.intersection(set(graph.neighbors(neighbor)), neighbor_ids)) for neighbor in neighbor_ids])/2
        n_count = len(neighbor_ids)
        o_count = len(set.intersection(neighbor_ids, set([x.index for x in ovs])))
        if v in ovs:
            o_triads = o_count*(o_count-1)+(n_count-o_count)*o_count
        else:
            o_triads = o_count*(o_count-1)
        if o_triads == 0:
            result = None
        else:
            result = float(intra_neighbor_ties)/o_triads
        results.append(result)
    return results
  
  
