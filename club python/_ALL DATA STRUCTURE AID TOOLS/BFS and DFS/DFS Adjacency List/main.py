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

def direct_dfs_recursive(edges, source):
    # build a directed adjacency graph
    graph = _directed_adjacency_graph(edges)

    # dfs traverse
    visited = set()
    def dfs(node):
        if node not in visited:
            visited.add(node)
            print(node, end=" -> ")

            neighbors = graph[node]
            for neighbor in neighbors:
                dfs(neighbor)

    dfs(source)
    print("END", end="\n")

def undirect_dfs_recursive(edges, source):
    # build a directed adjacency graph
    graph = _undirected_adjacency_graph(edges)

    # dfs traverse
    visited = set()
    def dfs(node):
        if node not in visited:
            visited.add(node)
            print(node, end=" -> ")

            neighbors = graph[node]
            for neighbor in neighbors:
                dfs(neighbor)

    dfs(source)
    print("END", end="\n")

def direct_dfs_iterative(edges, source):
    # build a directed adjacency graph
    graph = _directed_adjacency_graph(edges)

    # dfs traverse
    stack = deque([source])
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" -> ")

            neighbors = graph[node]
            for neighbor in neighbors:
                stack.append(neighbor)

    print("END", end="\n")


def undirect_dfs_iterative(edges, source):
    # build a directed adjacency graph
    graph = _undirected_adjacency_graph(edges)

    # dfs traverse
    stack = deque([source])
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" -> ")

            neighbors = graph[node]
            for neighbor in neighbors:
                stack.append(neighbor)

    print("END", end="\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # [from, to]
    edges1 = [[0, 1], [1, 2], [2, 3], [3, 4]] #  Linear Graph
    edges2 = [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5]] # Branching Graph
    edges3 = [[0, 1], [1, 2], [2, 0], [2, 3]] # Graph with a Cycle
    edges4 = [[0, 1], [1, 4], [2, 3]]  # Disconnected Graph
    edges5 = [[0, 0], [1, 2], [2, 0]] # No outgoing edges from start

    print("\n === direct_dfs_recursive === \n")
    direct_dfs_recursive(edges1, 0) # [0 -> 1 -> 2 -> 3 -> 4 -> END]
    direct_dfs_recursive(edges1, 2)  # [2 -> 3 -> 4 -> END]
    direct_dfs_recursive(edges2, 0)  # [0 -> 1 -> 4 -> 2 -> 3 -> END]
    direct_dfs_recursive(edges3, 0)  # [0 -> 1 -> 2 -> 3 -> END]
    direct_dfs_recursive(edges4, 0)  # [0 -> 1 -> 4 -> END]
    direct_dfs_recursive(edges4, 2)  # [2 -> 3 -> END]
    direct_dfs_recursive(edges5, 0)  # [0 -> END]

    print("\n === undirect_dfs_recursive === \n")
    undirect_dfs_recursive(edges1, 0) # [0 -> 1 -> 2 -> 3 -> 4 -> END]
    undirect_dfs_recursive(edges1, 2)  # [2 -> 1 -> 0 -> 3 -> 4 -> END]
    undirect_dfs_recursive(edges2, 0)  # [0 -> 1 -> 3 -> 2 -> 4 -> 5 -> END]
    undirect_dfs_recursive(edges3, 0)  # [0 -> 1 -> 2 -> 3 -> END]
    undirect_dfs_recursive(edges4, 0)  # [0 -> 1 -> 4 -> END]
    undirect_dfs_recursive(edges4, 2)  # [2 -> 3 -> END]
    undirect_dfs_recursive(edges5, 0)  # [0 -> 2 -> 1 -> END]

    print("\n === direct_dfs_iterative === \n")
    direct_dfs_iterative(edges1, 0)  # [0 -> 1 -> 2 -> 3 -> 4 -> END]
    direct_dfs_iterative(edges1, 2)  # [2 -> 3 -> 4 -> END]
    direct_dfs_iterative(edges2, 0)  # [0 -> 2 -> 5 -> 4 -> 1 -> 3 -> END]
    direct_dfs_iterative(edges3, 0)  # [0 -> 1 -> 2 -> 3 -> END]
    direct_dfs_iterative(edges4, 0)  # [0 -> 1 -> 4 -> END]
    direct_dfs_iterative(edges4, 2)  # [2 -> 3 -> END]
    direct_dfs_iterative(edges5, 0)  # [0 -> END]

    print("\n === undirect_dfs_iterative === \n")
    undirect_dfs_iterative(edges1, 0)  # [0 -> 1 -> 2 -> 3 -> 4 -> END]
    undirect_dfs_iterative(edges1, 2)  # [2 -> 3 -> 4 -> 1 -> 0 -> END]
    undirect_dfs_iterative(edges2, 0)  # [0 -> 2 -> 5 -> 4 -> 1 -> 3 -> END]
    undirect_dfs_iterative(edges3, 0)  # [0 -> 2 -> 3 -> 1 -> END]
    undirect_dfs_iterative(edges4, 0)  # [0 -> 1 -> 4 -> END]
    undirect_dfs_iterative(edges4, 2)  # [2 -> 3 -> END]
    undirect_dfs_iterative(edges5, 0)  # [0 -> 2 -> 1 -> END]
