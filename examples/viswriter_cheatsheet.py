from dgl.vis import VisWriter

# Specify the path to save files
writer = VisWriter(logdir='data')

# Add a graph.
# node labels, number of node classes and edge weights are optional.
# A graph can be associated with multiple types of edge weights.
writer.add_graph(name='Cora', graph=..., 
                 nlabels=..., eweights={'confidence':..., 'strength':...})

# Add a model.
# L0_Hi stands for the edge weights from the i-th attention head in the first layer.
writer.add_model(graph_name='Cora', model_name='GAT_L2', 
                 nlabels=..., eweights={'L0_H0':..., 'L0_H1':...})

# Add weighted subgraphs associated with two particular nodes.
# The weighted subgraphs are generated by a same explanation method.
# subgraph edge weights is optional.
writer.add_subgraph(graph_name='Cora', subgraph_name='GNNExplainer', 
                    node_id=0, subgraph=..., subgraph_eweights=...)
writer.add_subgraph(graph_name='Cora', subgraph_name='GNNExplainer', 
                    node_id=16, subgraph=..., subgraph_eweights=...)

# Finish data preparation.
writer.close()
