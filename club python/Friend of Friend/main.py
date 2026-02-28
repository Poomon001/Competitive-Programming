from collections import defaultdict, deque
'''
    Purpose: Determine a friend of friend that a target person not yet connected with - 1-level relationship only
           : e.g B has friends of A, B, C, D.
           :     A has friends of B, C
           :     C has friends of A, B, K
           : if target is A it return [D, K] where D, K is a friend of B, C who A doesnt yet connect with.
    parameter: str target - a person
            : list[list] friendList - a pair of relation where [person, person's friend]
    return: list[str] - non-duplicate a friend of friend that a person doesnt yet connected with
    Pre-Condition: none
    Post-Condition: none
'''
# hashmap - runtime: O(f * fof), memory: O(n) where n = all nodes, f = friends of targets, and fof friends of friends of targets
def recommend_M1(target, friendList):
    ans = set()
    friendToFriends = defaultdict(set)

    for person, friend in friendList:
        friendToFriends[person].add(friend)
        friendToFriends[friend].add(person)

    targetFriends = friendToFriends[target]

    for friend in targetFriends:
        for friendOfFriend in friendToFriends[friend]:
            if friendOfFriend != target and friendOfFriend not in targetFriends:
                ans.add(friendOfFriend)

    return list(ans)

'''
    Purpose: Determine a friend of friend that a target person not yet connected with - 1-level relationship only
           : e.g B has friends of A, B, C, D.
           :     A has friends of B, C
           :     C has friends of A, B, K
           : if target is A it return [D, K] where D, K is a friend of B, C who A doesnt yet connect with.
    parameter: str target - a person
            : list[list] friendList - a pair of relation where [person, person's friend]
    return: list[str] - non-duplicate a friend of friend that a person doesnt yet connected with
    Pre-Condition: none
    Post-Condition: none
'''
# bfs - runtime: O(f * fof), memory: O(n) where n = all nodes, f = friends of targets, and fof friends of friends of targets
# note can be scaled to N-level
def recommend_M2(target, friendList):
    friendOfFriends = set()
    personToFriends = defaultdict(set)

    for person, friend in friendList:
        personToFriends[person].add(friend)
        personToFriends[friend].add(person)

    visited = set()
    level = 0

    def bfs(target, level):
        queue = deque(target)
        while queue and level <= 1:
            temp = deque()
            while queue and level <= 1:
                person = queue.popleft()
                if person not in visited:
                    visited.add(person)

                    neighbors = personToFriends[person]
                    for neighbor in neighbors:
                        temp.append(neighbor)
                        if neighbor != target:
                            friendOfFriends.add(neighbor)

            queue = temp
            level += 1

    bfs(target, level)

    return list(friendOfFriends - personToFriends[target])

'''
    Purpose: Determine a friend of friend that a target person not yet connected with - 1-level relationship only
           : e.g B has friends of A, B, C, D.
           :     A has friends of B, C
           :     C has friends of A, B, K
           : if target is A it return [D, K] where D, K is a friend of B, C who A doesnt yet connect with.
    parameter: str target - a person
            : list[list] friendList - a pair of relation where [person, person's friend]
    return: list[str] - non-duplicate a friend of friend that a person doesnt yet connected with
    Pre-Condition: none
    Post-Condition: none
'''
# dfs - runtime: O(f * fof), memory: O(n) where n = all nodes, f = friends of targets, and fof friends of friends of targets
# note can be scaled to N-level
def recommend_M3(target, friendList):
    graph = defaultdict(list)
    visited = set()
    for p1, p2 in friendList:
        graph[p1].append(p2)
        graph[p2].append(p1)

    ans = set()

    def dfs(person: str, level: int):
        if person != target and level == 2:
            ans.add(person)

        friends = graph[person]
        for friend in friends:
            # 0-level is target, 1-level is target's friend, and 2-level is target's friends of friend
            if friend != target and level + 1 <= 2:
                dfs(friend, level + 1)

    dfs(target, 0)
    return list(ans - set(graph[target]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    relation1 = [["A", "B"], ["A", "C"], ["A", "D"]] # a friend of friends has no other friends
    relation2 = [["A", "B"], ["A", "C"], ["A", "D"], ["B", "F"]] # a friend of friends has all exclusive friends
    relation3 = [["A", "B"], ["A", "C"], ["A", "D"], ["B", "F"], ["C", "F"], ["F", "D"], ["F", "A"]]  # a friend of friends has all exclusive friends
    relation4 = [["A", "B"], ["A", "C"], ["A", "D"], ["B", "F"], ["F", "A"], ["F", "E"], ["E", "K"], ["E", "A"]] # a friend of friends has a mix of mutual and exclusive friends

    print("\n === Solution 1 === \n")
    print(recommend_M1("A", relation1)) # set()
    print(recommend_M1("B", relation2)) # "C", "D"
    print(recommend_M1("F", relation3)) # set()
    print(recommend_M1("F", relation4)) # "K", "D", "C"

    print("\n === Solution 2 === \n")
    print(recommend_M2("A", relation1))  # set()
    print(recommend_M2("B", relation2))  # "C", "D"
    print(recommend_M2("F", relation3))  # set()
    print(recommend_M2("F", relation4))  # "K", "D", "C"

    print("\n === Solution 2 === \n")
    print(recommend_M3("A", relation1))  # set()
    print(recommend_M3("B", relation2))  # "C", "D"
    print(recommend_M3("F", relation3))  # set()
    print(recommend_M3("F", relation4))  # "K", "D", "C"
