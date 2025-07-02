from collections import defaultdict, deque

def _directed_adjacency_graph(edges) -> dict:
    graph = defaultdict(list)
    for node, outgoing in edges:
        graph[node].append(outgoing)
    return graph

def _undirected_adjacency_graph(edges) -> dict:
    graph = defaultdict(list)
    for node, outgoing in edges:
        graph[node].append(outgoing)
        graph[outgoing].append(node)
    return graph

def direct_bfs_iterative(edges, sources):
    graph = _directed_adjacency_graph(edges)

    queue = deque(sources)
    visited = set()

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end=" -> ")

            neighbors = graph[node]
            for neighbor in neighbors:
                queue.append(neighbor)
    print("END", end="\n")

def undirect_bfs_iterative(edges, sources):
    graph = _undirected_adjacency_graph(edges)

    queue = deque(sources)
    visited = set()

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end=" -> ")

            neighbors = graph[node]
            for neighbor in neighbors:
                queue.append(neighbor)
    print("END", end="\n")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # [from, to]
    edges1 = [[0, 1], [1, 2], [2, 3], [3, 4]]  # Linear Graph
    edges2 = [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5]]  # Branching Graph
    edges3 = [[0, 1], [1, 2], [2, 0], [2, 3]]  # Graph with a Cycle
    edges4 = [[0, 1], [1, 4], [2, 3]]  # Disconnected Graph
    edges5 = [[0, 0], [1, 2], [2, 0]]  # No outgoing edges from start

    print("\n === direct_bfs_iterative === \n")
    direct_bfs_iterative(edges1, [0])  # [0 -> 1 -> 2 -> 3 -> 4 -> END]
    direct_bfs_iterative(edges1, [2])  # [2 -> 3 -> 4 -> END]
    direct_bfs_iterative(edges2, [0])  # [0 -> 2 -> 5 -> 4 -> 1 -> 3 -> END]
    direct_bfs_iterative(edges2, [0, 2])  # [0 -> 2 -> 1 -> 4 -> 5 -> 3 -> END]
    direct_bfs_iterative(edges3, [0])  # [0 -> 1 -> 2 -> 3 -> END]
    direct_bfs_iterative(edges4, [0])  # [0 -> 1 -> 4 -> END]
    direct_bfs_iterative(edges4, [2])  # [2 -> 3 -> END]
    direct_bfs_iterative(edges4, [2, 0])  # [2 -> 0 -> 3 -> 1 -> 4 -> END]
    direct_bfs_iterative(edges5, [0])  # [0 -> END]

    print("\n === undirect_bfs_iterative === \n")
    undirect_bfs_iterative(edges1, [0])  # [0 -> 1 -> 2 -> 3 -> 4 -> END]
    undirect_bfs_iterative(edges1, [2])  # [2 -> 1 -> 3 -> 0 -> 4 -> END]
    undirect_bfs_iterative(edges2, [0])  # [0 -> 1 -> 2 -> 3 -> 4 -> 5 -> END]
    undirect_bfs_iterative(edges2, [0, 2])  # [0 -> 2 -> 1 -> 4 -> 5 -> 3 -> END]
    undirect_bfs_iterative(edges3, [0])  # [0 -> 1 -> 2 -> 3 -> END]
    undirect_bfs_iterative(edges4, [0])  # [0 -> 1 -> 4 -> END]
    undirect_bfs_iterative(edges4, [2])  # [2 -> 3 -> END]
    undirect_bfs_iterative(edges4, [2, 0])  # [2 -> 0 -> 3 -> 1 -> 4 -> END]
    undirect_bfs_iterative(edges5, [0])  # [0 -> 2 -> 1 -> END]