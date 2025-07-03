from typing import List
from collections import defaultdict

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
def courseSchedule(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    # make adjacency list
    for node, outgoing in prerequisites:
        graph[node].append(outgoing)

    # iterate through a graph
    visited = set()
    path = set()
    def dfs(node):
        if node in path:
            return True # there is a cycle
        if node in visited:
            return False # there is no a cycle

        path.add(node)
        visited.add(node)

        neighbors = graph[node]
        for neighbor in neighbors:
            if dfs(neighbor):
                return True

        path.remove(node)
        return False


    nodes = set(node for node, _ in prerequisites) | set(outgoing for _, outgoing in prerequisites)
    for node in nodes:
        if node not in visited:
            if dfs(node):
                return False

    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    edges1 = [[1, 0]] # Graph with no Cycle
    edges2 = [[0,1],[0,2],[1,2]] # Graph with no Cycle
    edges3 = [[1,0],[0,1]] # Graph with a directed Cycle
    edges4 = [[1, 4], [4, 5], [5, 2], [1, 4], [3, 4], [3, 1], [3, 7]]  # Graph with a undirected Cycle
    edges5 = [[0, 1], [1, 4], [2, 3], [4, 0]]  # Disconnected Graph with cycle
    edges6 = [[0, 1], [1, 4], [2, 3]]  # Disconnected Graph

    print(courseSchedule(2 , edges1)) # True
    print(courseSchedule(3, edges2)) # True
    print(courseSchedule(2, edges3)) # False
    print(courseSchedule(6, edges4))  # True
    print(courseSchedule(5, edges5))  # False
    print(courseSchedule(5, edges6))  # True
