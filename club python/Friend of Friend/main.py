'''
    Purpose: Determine a friend of friend for a target person
    parameter: str target - a person
            : list[list] friendList - a pari of relation where [person, person's friend]
    return: list[str] - non-duplicate a friend of friend that a person doesnt yet connected with
    Pre-Condition: none
    Post-Condition: none
'''
# hashSet - runtime: O(n^2), memory: O(n)
def recommend(target, friendList):
    ans = set()

    # {"person", set(their friends)}
    friendToConnection = {}

    for relation in friendList:
        person = relation[0]
        friend = relation[1]
        if person not in friendToConnection:
            friendToConnection[person] = set(friend)
        else:
            friendToConnection[person].add(friend)

    # add friend of friend to ans
    for myFriend in friendToConnection[target]:
        if myFriend in friendToConnection:
            relatedFriendSet = friendToConnection[myFriend]
            for relatedFriend in relatedFriendSet:
                if relatedFriend not in friendToConnection[target] and relatedFriend != target:
                    ans.add(relatedFriend)

    return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(recommend("A", [["A", "B"], ["A", "C"], ["A", "D"], ["B", "A"], ["B", "F"]])) # F
    print(recommend("A", [["A", "C"], ["A", "D"], ["B", "A"], ["B", "F"]])) # {}
    print(recommend("B", [["A", "B"], ["A", "C"], ["A", "D"], ["B", "A"], ["B", "F"]])) # "C", "D"
    print(recommend("F", [["A", "B"], ["A", "C"], ["A", "D"], ["B", "A"], ["B", "F"], ["F", "A"], ["A", "F"]])) # "C","B","D"
    print(recommend("F", [["A", "B"], ["A", "C"], ["A", "D"], ["B", "A"], ["B", "F"],["B", "K"], ["F", "A"], ["A", "F"], ["F","B"]])) # "K","D","C"
