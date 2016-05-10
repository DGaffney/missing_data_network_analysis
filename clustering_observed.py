import igraph
import networkx as nx
import numpy as np
  
## NetworkX version
# Given only a graph these functions are same as standard networkx versions 
# Given a list of observed nodes these functions will count only observed triangles
# Given something different to do with nodes for which cc is undefined, clustering will oblige and 
# average_clustering will ignore non-numbers in its average. Setting undefined=None, for example, ignores leaves. 
def clustering(graph, observed='all', undefined=0.0):
    results = []
    full = True if observed == 'all' else False
    if type(undefined) is int: undefined = float(undefined)
    for v in graph:
        neighbor_ids = set(graph.neighbors(v))
        intra_neighbor_ties = sum([len(set.intersection(set(graph.neighbors(neighbor)), neighbor_ids)) for neighbor in neighbor_ids])/2
        n_count = len(neighbor_ids)
        o_count = n_count if full else len(set.intersection(neighbor_ids, set(observed)))
        if not full and v in observed:
            o_triads = 0.5*o_count*(o_count-1)+(n_count-o_count)*o_count
        else:
            o_triads = 0.5*o_count*(o_count-1)
        # the canonical clustering coefficient is undefined for leaves - default is zero
        result = undefined if o_triads == 0 else float(intra_neighbor_ties)/o_triads
        results.append(result)
    return results

def avg_clustering(graph, observed='all', undefined=0.0):
    results = []
    full = True if observed == 'all' else False
    if type(undefined) is int: undefined = float(undefined)
    for v in graph:
        neighbor_ids = set(graph.neighbors(v))
        intra_neighbor_ties = sum([len(set.intersection(set(graph.neighbors(neighbor)), neighbor_ids)) for neighbor in neighbor_ids])/2
        n_count = len(neighbor_ids)
        o_count = n_count if full else len(set.intersection(neighbor_ids, set(observed)))
        if not full and v in observed:
            o_triads = 0.5*o_count*(o_count-1)+(n_count-o_count)*o_count
        else:
            o_triads = 0.5*o_count*(o_count-1)
        # the canonical clustering coefficient is undefined for leaves - default is zero
        result = undefined if o_triads == 0 else float(intra_neighbor_ties)/o_triads
        results.append(result)
    results = [x for x in results if type(x) is float] # remove the undefined nodes if they are not integers
    return float(sum(results))/len(results)

## Example
flights = [["ORD", "SEA"], ["ORD", "LAX"], ['ORD', 'DFW'], ['ORD', 'PIT'], ['SEA', 'LAX'], ['LAX', 'DFW'], ['ATL', 'PIT'], ['ATL', 'RDU'], ['RDU', 'PHL'], ['PIT', 'PHL'], ['PHL', 'PVD']]
gg = nx.Graph()
for flight in flights:
    gg.add_edge(flight[0],flight[1])
observed = gg.nodes()[:-2]

avg_nx   = nx.average_clustering(gg)
avg_Zero = avg_clustering(gg)
avg_None = avg_clustering(gg, undefined=None)
avg_obs_Zero = avg_clustering(gg, observed=observed)
avg_obs_None = avg_clustering(gg, observed=observed, undefined=None)

### Example runs 
## NetworkX version
flights = [["ORD", "SEA"], ["ORD", "LAX"], ['ORD', 'DFW'], ['ORD', 'PIT'], ['SEA', 'LAX'], ['LAX', 'DFW'], ['ATL', 'PIT'], ['ATL', 'RDU'], ['RDU', 'PHL'], ['PIT', 'PHL'], ['PHL', 'PVD']]
gg = nx.Graph()
for flight in flights:
    gg.add_edge(flight[0],flight[1])
observed = gg.nodes()[:-2]
example_igraph = clustering_observed_nx(gg, observed)
print example_igraph
print np.mean([x for x in example_igraph if x!=None])

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

flights = [["ORD", "SEA"], ["ORD", "LAX"], ['ORD', 'DFW'], ['ORD', 'PIT'], ['SEA', 'LAX'], ['LAX', 'DFW'], ['ATL', 'PIT'], ['ATL', 'RDU'], ['RDU', 'PHL'], ['PIT', 'PHL'], ['PHL', 'PVD']]
gg = igraph.Graph(directed=False)
gg.add_vertices(list(set([item for sublist in flights for item in sublist])))
gg.add_edges(flights)
observed = [x for x in gg.vs][:-2]
example_igraph = clustering_observed_igraph(gg, observed)
print example_igraph
print np.mean([x for x in example_igraph if x!=None])
