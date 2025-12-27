from collections import defaultdict
import heapq
from math import inf
from typing import List

'''
    Link: https://leetcode.com/problems/network-delay-time/
    Purpose: Given a network of n nodes, labeled from 1 to n. And times, a list of travel times as directed edges 
           : times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, 
           : and wi is the time it takes for a signal to travel from source to target.
           : FIND the minimum time it takes for all the n nodes to receive the signal from source k.
    parameter: List[List[int]] times - a list of times where times[i] = (ui, vi, wi)
             : int n - a number of nodes
             : int k - a source node
    return: bool - True if s can be segmented. otherwise, False
    Pre-Condition: 1 <= k <= n <= 100
                 : 1 <= times.length <= 6000
                 : times[i].length == 3
                 : 1 <= ui, vi <= n
                 : ui != vi
                 : 0 <= wi <= 100
                 : All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
    Post-Condition: none
'''
# graph dijkstra algo - runtime: O(V*V), space: O(V*E)
def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    # build an adjacency graph
    graph = defaultdict(list)
    for time in times:
        graph[time[0]].append((time[1], time[2]))

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

    ans = max(node_to_distances.values())
    return -1 if ans == inf else ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1], [1, 4, 5]], n=4, k=2)) # 2
    print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)) # 2
    print(networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=3)) # -1
    print(networkDelayTime([[1,2,1]], n=2, k=1)) # 1
    print(networkDelayTime([[1,2,1]], n=2, k=2)) # -1
