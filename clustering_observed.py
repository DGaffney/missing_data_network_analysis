import igraph
import networkx as nx
import numpy as np

## iGraph version
# Takes an iGraph graph object and an iGraph vertex sequence object
def clustering_observed_igraph(graph, ovs):
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
  
## NetworkX version
# Takes a networkx graph and a list of fully observed node ids
def clustering_observed_nx(graph, ovs):
    results = []
    for v in graph:
        neighbor_ids = set(graph.neighbors(v))
        intra_neighbor_ties = sum([len(set.intersection(set(graph.neighbors(neighbor)), neighbor_ids)) for neighbor in neighbor_ids])/2
        n_count = len(neighbor_ids)
        o_count = len(set.intersection(neighbor_ids, set(ovs)))
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

### Example runs 
## iGraph version
flights = [["ORD", "SEA"], ["ORD", "LAX"], ['ORD', 'DFW'], ['ORD', 'PIT'], ['SEA', 'LAX'], ['LAX', 'DFW'], ['ATL', 'PIT'], ['ATL', 'RDU'], ['RDU', 'PHL'], ['PIT', 'PHL'], ['PHL', 'PVD']]
gg = igraph.Graph(directed=False)
gg.add_vertices(list(set([item for sublist in flights for item in sublist])))
gg.add_edges(flights)
observed = [x for x in gg.vs][:-2]
example_igraph = clustering_observed_igraph(gg, observed)
print example_igraph
print np.mean([x for x in example_igraph if x!=None])

## NetworkX version
flights = [["ORD", "SEA"], ["ORD", "LAX"], ['ORD', 'DFW'], ['ORD', 'PIT'], ['SEA', 'LAX'], ['LAX', 'DFW'], ['ATL', 'PIT'], ['ATL', 'RDU'], ['RDU', 'PHL'], ['PIT', 'PHL'], ['PHL', 'PVD']]
gg = nx.Graph()
for flight in flights:
    gg.add_edge(flight[0],flight[1])
observed = gg.nodes()[:-2]
example_igraph = clustering_observed_nx(gg, observed)
print example_igraph
print np.mean([x for x in example_igraph if x!=None])



