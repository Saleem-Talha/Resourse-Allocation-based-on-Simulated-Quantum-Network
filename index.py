import networkx as nx
import matplotlib.pyplot as plt

def find_paths(graph, source, target, k):
    return list(nx.shortest_simple_paths(graph, source, target))[:k]

def find_shortest_path(paths):
    return min(paths, key=len) if paths else None

def resource_allocation(graph, apps):
    residual_graph = graph.copy()
    F = set()
    L = set(range(len(apps)))
    paths = {i: [] for i in range(len(apps))}

    for i, (hi, Wi, _, _) in enumerate(apps):
        for w in Wi:
            paths[i].extend(find_paths(residual_graph, hi, w, 3))

    delta = 0
    while L:
        app_idx = next(iter(L))
        delta = apps[app_idx][3] / sum(app[3] for app in apps)

        p = None
        while not p and paths[app_idx]:
            p = find_shortest_path(paths[app_idx])
            if p and not all(residual_graph.has_edge(u, v) for u, v in zip(p[:-1], p[1:])):
                paths[app_idx].remove(p)
                p = None

        if not p:
            L.remove(app_idx)
        else:
            R = min(delta, min(residual_graph[u][v]['capacity'] for u, v in zip(p[:-1], p[1:])))
            F.add((app_idx, tuple(p), R))

            for u, v in zip(p[:-1], p[1:]):
                residual_graph[u][v]['capacity'] -= R
                if residual_graph[u][v]['capacity'] <= 0:
                    residual_graph.remove_edge(u, v)

    return F

def visualize_network(G, apps, allocated_flows, title):
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)
    
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_labels(G, pos)
    
    edge_labels = nx.get_edge_attributes(G, 'capacity')
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    nx.draw_networkx_edges(G, pos)
    
    for app_idx, path, flow in allocated_flows:
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, 
                             edge_color='r', width=2, alpha=0.5)
    
    plt.title(title)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":

    G = nx.DiGraph()
    G.add_edge('A', 'B', capacity=10)
    G.add_edge('B', 'C', capacity=5)
    G.add_edge('A', 'C', capacity=15)
    
    apps = [
        ('A', ['C'], 3, 0.5),
        ('A', ['B'], 2, 0.3),
    ]
    
    allocated_flows = resource_allocation(G, apps)
    print("Simple Network Allocated Flows:", allocated_flows)
    visualize_network(G, apps, allocated_flows, "Simple Network Resource Allocation")
    
    G2 = nx.DiGraph()
    G2.add_edge('X', 'Y', capacity=20)
    G2.add_edge('Y', 'Z', capacity=10)
    G2.add_edge('X', 'Z', capacity=25)
    G2.add_edge('Y', 'W', capacity=15)
    G2.add_edge('Z', 'W', capacity=10)
    
    apps2 = [
        ('X', ['W'], 5, 0.6),
        ('X', ['Z'], 4, 0.4),
        ('Y', ['W'], 3, 0.5),
    ]
    
    allocated_flows2 = resource_allocation(G2, apps2)
    print("Complex Network Allocated Flows:", allocated_flows2)
    visualize_network(G2, apps2, allocated_flows2, "Complex Network Resource Allocation")