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

def direct_graph_cycle_detection(edges):
    graph = _directed_adjacency_graph(edges)

    visited = set()
    path = set() # Check if there is a cycle within the current path

    def dfs(node):
        if node in path:
            # There is a cycle
            return True

        if node in visited:
            # Okay but not continue processing
            return False

        visited.add(node)
        path.add(node)

        neighbors = graph[node]
        for neighbor in neighbors:
            if dfs(neighbor):
                return True

        path.remove(node) # remove node from path for backtracking
        return False

    all_nodes = set([node for node, _ in edges]) | set([outgoing for _, outgoing in edges])
    # this for loop to handle forests
    for node in all_nodes:
        if node not in visited:
            if dfs(node):
                return True

    return False

def undirect_graph_cycle_detection(edges):
    graph = _undirected_adjacency_graph(edges)

    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor == parent:
                # we travel from neighbor to current node, so it is not cycle
                continue
            if neighbor in visited:
                # we will visit a node twice
                return True
            if dfs(neighbor, node):
                return True
        return False

    for node in graph:
        # this for loop to handle forests
        if node not in visited:
            if dfs(node, -1):
                return True

    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # [from, to]
    edges1 = [[0, 1], [1, 2], [2, 3], [3, 4]]  # Linear Graph
    edges2 = [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5]]  # Branching Graph
    edges3 = [[0, 1], [1, 2], [2, 0], [2, 3]]  # Graph with a Cycle 1
    edges4 = [[0, 1], [1, 4], [2, 3]]  # Disconnected Graph
    edges5 = [[0, 1], [1, 4], [2, 3], [4, 0]]  # Disconnected Graph with cycle
    edges6 = [[0, 0], [1, 2], [2, 0]]  # No outgoing edges from start - cycle
    edges7 = [[1, 4], [4, 5], [5, 2], [1, 3], [3, 6], [6, 1]]  # Graph with a Cycle 2
    edges8 = [[1, 4], [4, 5], [5, 2], [1, 4], [4, 3], [3, 1], [3, 7]]  # Graph with a Cycle 3
    edges9 = [[1, 4], [4, 5], [5, 2], [1, 4], [3, 4], [3, 1], [3, 7]]  # Graph with a undirected Cycle 3

    print("\n === direct graph cycle detection === \n")
    print(direct_graph_cycle_detection(edges1)) # False
    print(direct_graph_cycle_detection(edges2)) # False
    print(direct_graph_cycle_detection(edges3)) # True
    print(direct_graph_cycle_detection(edges4)) # False
    print(direct_graph_cycle_detection(edges5)) # True
    print(direct_graph_cycle_detection(edges6)) # True
    print(direct_graph_cycle_detection(edges7)) # True
    print(direct_graph_cycle_detection(edges8)) # True
    print(direct_graph_cycle_detection(edges9)) # False

    print("\n === undirect graph cycle detection === \n")
    print(undirect_graph_cycle_detection(edges1))  # False
    print(undirect_graph_cycle_detection(edges2))  # False
    print(undirect_graph_cycle_detection(edges3))  # True
    print(undirect_graph_cycle_detection(edges4))  # False
    print(undirect_graph_cycle_detection(edges5))  # True
    print(undirect_graph_cycle_detection(edges6))  # True
    print(undirect_graph_cycle_detection(edges7))  # True
    print(undirect_graph_cycle_detection(edges8))  # True
    print(undirect_graph_cycle_detection(edges9))  # True

