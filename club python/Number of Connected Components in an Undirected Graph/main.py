from collections import defaultdict
from typing import List

'''
    Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
    Purpose: Find the number of components in an undirected graph
    parameter: int n - a number of nodes in the graph
             : List[List[int]] edges - a list of edges in [node1, node2]
    return: int ans - a number of components in an undirected graph
    Pre-Condition: 1 <= n <= 2000
                 : 1 <= edges.length <= 5000
                 : edges[i].length == 2
                 : 0 <= ai <= bi < n
                 : ai != bi
                 : There are no repeated edges.
    Post-Condition: none
'''
# dfs - runtime: O(V + E), space: O(V + E)
def countComponents(edges: List[List[int]], n: int) -> int:
    visited = set()
    ans = 0
    graph = defaultdict(list)
    for node1, node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1)

    def dfs(source):
        if source in visited:
            return
        visited.add(source)

        neighbors = graph[source]
        for neighbor in neighbors:
            if neighbor not in visited:
                dfs(neighbor)

    for i in range(n):
        if i not in visited:
            ans += 1
            dfs(i)
    return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(countComponents([[0,1],[1,2],[3,4]], n = 5))
    print(countComponents([[0,1],[1,2],[2,3],[3,4]], n=5))
    print(countComponents([[0, 1], [1, 2], [2, 3], [3, 4]], n=10))
