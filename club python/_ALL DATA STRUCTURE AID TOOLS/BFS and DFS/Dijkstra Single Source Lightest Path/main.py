from collections import defaultdict
import heapq
from math import inf
from typing import List

def _directed_adjacency_graph(edges) -> dict:
    graph = defaultdict(list)
    for node, outgoing, weight in edges:
        graph[node].append((outgoing, weight))
    return graph

def _undirected_adjacency_graph(edges) -> dict:
    graph = defaultdict(list)
    for node, outgoing, weight in edges:
        graph[node].append((outgoing, weight))
        graph[outgoing].append((node, weight))
    return graph

'''
An algorithm to find the a lightest path from a source node to each target node 
'''
# dijkstra algo - runtime: O(V*V), space: O(V*E)
def dijkstra_with_directed_graph(edges: List[List[int]], n: int, k: int) -> dict:
    # build an adjacency graph
    graph = _directed_adjacency_graph(edges)

    node_to_distances = defaultdict(int)
    pq = [(0, k)]  # (weight, node) to order by min weight

    # build a node_to_distances
    for i in range(1, n + 1):
        node_to_distances[i] = inf
    node_to_distances[k] = 0

    while pq:
        curr_lightest_weight, curr_lightest_node = heapq.heappop(pq)

        # If we already found a shorter path, skip
        if curr_lightest_weight > node_to_distances[curr_lightest_node]:
            continue

        neighbors = graph[curr_lightest_node]
        for neighbor in neighbors:
            node = neighbor[0]
            weight = neighbor[1]
            # Relaxation: if a shorter path is found
            if weight + curr_lightest_weight < node_to_distances[node]:
                node_to_distances[node] = weight + curr_lightest_weight
                heapq.heappush(pq, (weight + curr_lightest_weight, node))

    # {node, shortest path from source to node}
    return dict(node_to_distances)


'''
An algorithm to find the a lightest path from a source node to each target node 
'''
# dijkstra algo - runtime: O(V*V), space: O(V*E)
def dijkstra_with_undirected_graph(edges: List[List[int]], n: int, k: int) -> dict:
    # build an adjacency graph
    graph = _undirected_adjacency_graph(edges)

    node_to_distances = defaultdict(int)
    pq = [(0, k)]  # (weight, node) to order by min weight

    # build a node_to_distances
    for i in range(1, n + 1):
        node_to_distances[i] = inf
    node_to_distances[k] = 0

    while pq:
        curr_lightest_weight, curr_lightest_node = heapq.heappop(pq)

        # If we already found a shorter path, skip
        if curr_lightest_weight > node_to_distances[curr_lightest_node]:
            continue

        neighbors = graph[curr_lightest_node]
        for neighbor in neighbors:
            node = neighbor[0]
            weight = neighbor[1]
            # Relaxation: if a shorter path is found
            if weight + curr_lightest_weight < node_to_distances[node]:
                node_to_distances[node] = weight + curr_lightest_weight
                heapq.heappush(pq, (weight + curr_lightest_weight, node))

    # {node, shortest path from source to node}
    return dict(node_to_distances)

if __name__ == '__main__':
    print("\n === dijkstra with directed graph  === \n")

    # edges[i] = (source, target, weight)
    edges = [[1, 2, 1]]
    n = 2
    source = 1
    print(dijkstra_with_directed_graph(edges, n, source))

    # edges[i] = (source, target, weight)
    edges = [[2, 1, 1], [2, 3, 1], [3, 4, 1], [1, 4, 5]]
    n = 4
    source = 2
    print(dijkstra_with_directed_graph(edges, n, source))

    # edges[i] = (source, target, weight)
    edges = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    source = 3
    print(dijkstra_with_directed_graph(edges, n, source))

    # edges[i] = (source, target, weight)
    edges = [[2, 1, 1], [2, 3, 1], [3, 4, 1], [5, 6, 2]]
    n = 6
    source = 3
    print(dijkstra_with_directed_graph(edges, n, source))

    # edges[i] = (source, target, weight)
    edges = [[2, 1, 1], [2, 3, 1], [3, 4, 1], [5, 6, 2]]
    n = 6
    source = 5
    print(dijkstra_with_directed_graph(edges, n, source))

    # edges[i] = (source, target, weight)
    edges = [
        [1, 2, 2],
        [1, 3, 5],
        [2, 3, 1],
        [2, 4, 2],
        [3, 4, 2],
        [4, 5, 1],
        [5, 3, 1],  # cycle
    ]
    n = 5
    source = 1
    print(dijkstra_with_directed_graph(edges, n, source))


    print("\n === dijkstra with undirected graph  === \n")

    # edges[i] = (source, target, weight)
    edges = [[1, 2, 1]]
    n = 2
    source = 1
    print(dijkstra_with_undirected_graph(edges, n, source))

    # edges[i] = (source, target, weight)
    edges = [[2, 1, 1], [2, 3, 1], [3, 4, 1], [1, 4, 5]]
    n = 4
    source = 2
    print(dijkstra_with_undirected_graph(edges, n, source))

    # edges[i] = (source, target, weight)
    edges = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    source = 3
    print(dijkstra_with_undirected_graph(edges, n, source))

    # edges[i] = (source, target, weight)
    edges = [[2, 1, 1], [2, 3, 1], [3, 4, 1], [5, 6, 2]]
    n = 6
    source = 3
    print(dijkstra_with_undirected_graph(edges, n, source))

    # edges[i] = (source, target, weight)
    edges = [[2, 1, 1], [2, 3, 1], [3, 4, 1], [5, 6, 2]]
    n = 6
    source = 5
    print(dijkstra_with_undirected_graph(edges, n, source))

    # edges[i] = (source, target, weight)
    edges = [
        [1, 2, 2],
        [1, 3, 5],
        [2, 3, 1],
        [2, 4, 2],
        [3, 4, 2],
        [4, 5, 1],
        [5, 3, 1],  # cycle
    ]
    n = 5
    source = 1
    print(dijkstra_with_undirected_graph(edges, n, source))
