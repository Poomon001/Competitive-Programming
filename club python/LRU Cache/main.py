class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

'''
    Link: https://leetcode.com/problems/lru-cache/
    Purpose: Implement LRU Cache algorithm with constraint runtime and limited cache capacity.
           : Need O(1) push to cache and update the recent use to 1st.
           : Need O(1) get to get cache and update the recent use to 1st. If no key, return -1.
    parameter: int key - an integer
             : int val - an integer
    return: None
    Pre-Condition: 1 <= capacity <= 3000
                 : 0 <= key <= 10^4
                 : 0 <= value <= 10^5
                 : At most 2 * 10^5 calls will be made to get and put.
    Post-Condition: none
'''
# Array - runtime: O(1), memory: O(n)
class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.key_to_node = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self._move_to_back(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self._move_to_back(node)
        else:
            node = Node(key, value)
            self.key_to_node[key] = node
            self._add_to_back(node)

            if len(self.key_to_node) > self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.key_to_node[lru.key]

    def _add_to_back(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_back(self, node: Node):
        self._remove(node)
        self._add_to_back(node)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1)) # 1
    cache.put(3, 3)
    print(cache.get(2)) # -1
    cache.put(4, 4)
    print(cache.get(1)) # -1
    print(cache.get(3)) # 3
    print(cache.get(4)) # 4
