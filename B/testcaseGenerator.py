import random

def generate_edges(nodes, num_edges):
    edges = set()
    while len(edges) < num_edges:
        edge = (random.choice(nodes), random.choice(nodes))
        if edge[0] != edge[1]:
            edges.add(edge)
    return list(edges)

def generate_testcases(num_nodes, num_edges, num_sources, filename):
    nodes = list(range(1, num_nodes + 1))
    edges = generate_edges(nodes, num_edges)
    sources = []

    while len(sources) < num_sources:
        source = random.choice(nodes)
        if any(edge[0] == source or edge[1] == source for edge in edges):
            sources.append(source)

    with open(filename, 'w') as file:
        for edge in edges:
            file.write(f"edge({edge[0]}, {edge[1]}).\n")
        for source in sources:
            file.write(f"source({source}).\n")

