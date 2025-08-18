from typing import List
from collections import defaultdict, deque

'''
    Link: https://leetcode.com/problems/course-schedule
    Purpose: Find if you can finish all courses given prerequisites where prerequisites[i] = [course, prerequisite]
    Parameter: int numCourses - a number of courses
             : List[List[int]] prerequisites - a list of prerequisites[i]
    Returns: bool - true if you can finish all courses. Otherwise, return false.
    Pre-Condition: 1 <= numCourses <= 2000
                 : 0 <= prerequisites.length <= 5000
                 : prerequisites[i].length == 2
                 : 0 <= ai, bi < numCourses
                 : All the pairs prerequisites[i] are unique.
    Post-Condition: none
'''
# runtime: O(nlogn), space: O(n)
def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # [a, b] == b -> a == b: [a]
    graph = defaultdict(list)
    incomingCount = {}
    for outgoing, node in prerequisites:
        graph[node].append(outgoing)
        incomingCount[outgoing] = incomingCount.get(outgoing, 0) + 1

    order = []
    visited = set()

    def bfs(sources: List[int]):
        queue = deque(sources)
        while queue:
            node = queue.popleft()
            if node in visited:
                return

            visited.add(node)
            order.append(node)

            neighbors = graph[node]
            for neighbor in neighbors:
                incomingCount[neighbor] -= 1
                if neighbor not in visited and incomingCount[neighbor] == 0:
                    queue.append(neighbor)

    sources = []
    for node in range(numCourses):
        count = incomingCount.get(node, 0)
        if count == 0:
            sources.append(node)
    bfs(sources)

    return order if len(order) == numCourses else []

if __name__ == '__main__':
    edges1 = [[1, 0]]  # Graph with no Cycle
    edges2 = [[0, 1], [0, 2], [1, 2]]  # Graph with no Cycle
    edges3 = [[1, 0], [0, 1]]  # Graph with a directed Cycle
    edges4 = [[1, 4], [4, 5], [5, 2], [1, 4], [3, 4], [3, 1], [3, 7]]  # Graph with a undirected Cycle
    edges5 = [[0, 1], [1, 4], [2, 3], [4, 0]]  # Disconnected Graph with cycle
    edges6 = [[0, 1], [1, 4], [2, 3]]  # Disconnected Graph

    print(findOrder(2, edges1))  # [0, 1]
    print(findOrder(3, edges2))  # [2, 1, 0]
    print(findOrder(2, edges3))  # []
    print(findOrder(6, edges4))  # []
    print(findOrder(5, edges5))  # []
    print(findOrder(5, edges6))  # [3, 4, 2, 1, 0]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
