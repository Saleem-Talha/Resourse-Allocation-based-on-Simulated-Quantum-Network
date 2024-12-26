import networkx as nx

def find_paths(graph, source, target, k):
    """
    Find up to 'k' paths between source and target nodes in the residual graph.
    """
    return list(nx.shortest_simple_paths(graph, source, target))[:k]

def find_shortest_path(paths):
    """
    Select the shortest path from the available paths.
    """
    return min(paths, key=len) if paths else None

def resource_allocation(graph, apps):
    """
    Allocate resources for distributed quantum computing applications.
    
    Parameters:
    graph: NetworkX graph representing the residual graph G0
    apps: List of applications, each as a tuple (hi, Wi, F_min, ρ)
    
    Returns:
    F: Set of allocated flows
    """
    residual_graph = graph.copy()
    F = set()
    L = set(range(len(apps)))  # Indices of apps to be provisioned
    paths = {i: [] for i in range(len(apps))}

    # Populate paths for all apps
    for i, (hi, Wi, _, _) in enumerate(apps):
        for w in Wi:
            paths[i].extend(find_paths(residual_graph, hi, w, 3))  # Find up to 3 paths

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
            F.add((app_idx, tuple(p), R))  # Convert path list to tuple

            for u, v in zip(p[:-1], p[1:]):
                residual_graph[u][v]['capacity'] -= R
                if residual_graph[u][v]['capacity'] <= 0:
                    residual_graph.remove_edge(u, v)

    return F

# Example usage
if __name__ == "__main__":
    # Create a sample graph
    G = nx.DiGraph()
    G.add_edge('A', 'B', capacity=10)
    G.add_edge('B', 'C', capacity=5)
    G.add_edge('A', 'C', capacity=15)

    # Define applications (hi, Wi, F_min, ρ)
    apps = [
        ('A', ['C'], 3, 0.5),  # App 1
        ('A', ['B'], 2, 0.3),  # App 2
    ]

    allocated_flows = resource_allocation(G, apps)
    print("Allocated Flows:", allocated_flows)

    # Another example usage
    G2 = nx.DiGraph()
    G2.add_edge('X', 'Y', capacity=20)
    G2.add_edge('Y', 'Z', capacity=10)
    G2.add_edge('X', 'Z', capacity=25)
    G2.add_edge('Y', 'W', capacity=15)
    G2.add_edge('Z', 'W', capacity=10)

    apps2 = [
        ('X', ['W'], 5, 0.6),  # App 1: From 'X' to 'W'
        ('X', ['Z'], 4, 0.4),  # App 2: From 'X' to 'Z'
        ('Y', ['W'], 3, 0.5),  # App 3: From 'Y' to 'W'
    ]

    allocated_flows2 = resource_allocation(G2, apps2)
    print("Allocated Flows:", allocated_flows2)
