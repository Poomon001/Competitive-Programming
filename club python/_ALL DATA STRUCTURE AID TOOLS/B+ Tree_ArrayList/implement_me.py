# Implementation of B+-tree functionality.

from index import *

# You should implement all of the static functions declared
# in the ImplementMe class and submit this (and only this!) file.
class ImplementMe:
    # Returns a B+-tree obtained by inserting a key into a pre-existing
    # B+-tree index if the key is not already there. If it already exists,
    # the return value is equivalent to the original, input tree.
    #
    # Complexity: Guaranteed to be asymptotically linear in the height of the tree
    # Because the tree is balanced, it is also asymptotically logarithmic in the
    # number of keys that already exist in the index.
    @staticmethod
    def InsertIntoIndex( index, key ):
        currNode = index.root
        currKey = currNode.keys
        path = []
        splitKey = []

        # insert into empty B+ tree
        if currKey == KeySet([None, None]):
            keySets = KeySet([key, index.root.keys.keys[1]])
            pointerSets = index.root.pointers
            index = Index(Node(keySets, pointerSets))


        while currKey != KeySet([None, None]):
            # save current path
            path.append(currNode)

            # set currKey to the left-most key
            currKeyVal = currKey.keys[0] # int | None

            ''' Traverse to a leaf node '''

            # find a duplicate, return original B+ tree
            if key == currKeyVal:
                return index

            # case 1: key is less than left-most key
            if key < currKeyVal:
                # None represent the none Node
                if currNode.pointers.pointers[0] is not None:
                    # currNode is not a leaf, go left-side pointer
                    currNode = currNode.pointers.pointers[0]
                    currKey = currNode.keys
                    continue

            # set currKey to the right-most key
            currKeyVal = currKey.keys[1]  # int | None

            # find a duplicate, return original B+ tree
            if key == currKeyVal:
                return index

            # case 2: key is between left-most and right-most keys
            if currKeyVal is None or key < currKeyVal:
                # None represent the none Node
                if currNode.pointers.pointers[0] is not None:
                    # currNode is not a leaf, go middle pointer
                    currNode = currNode.pointers.pointers[1]
                    currKey = currNode.keys
                    continue

            # case 3: key is greater than right-most key
            if currKeyVal and key > currKeyVal:
                # None represent the none Node
                if currNode.pointers.pointers[0] is not None:
                    # currNode is not a leaf, go right pointer
                    currNode = currNode.pointers.pointers[2]
                    currKey = currNode.keys
                    continue

            ''' insertion at a leaf '''
            # space is available to insert
            if path:
                path.pop()

            if None in currKey.keys:
                 currKey.keys = [min(key, currKey.keys[0]), max(key, currKey.keys[0])]
                 return index
            else:
                # split to the next level
                nums = sorted([currKey.keys[0], currKey.keys[1], key])
                splitKey.append(nums[1])
                rightNode = Node(KeySet([nums[1], nums[2]]), PointerSet(currNode.pointers.pointers))
                currNode.keys = KeySet([nums[0], None])
                currNode.pointers = PointerSet([None] * Index.FAN_OUT)
                currNode.pointers.pointers[Index.NUM_KEYS] = rightNode

                # add to the next level
                while splitKey:
                    key = splitKey.pop()

                    if path:
                        # still parent left
                        parent = path.pop()
                    else:
                        # no parent left
                        parent = Node(KeySet([key, None]), PointerSet([currNode, rightNode, None]))
                        if currNode.pointers.pointers[0] is None:
                            currNode.pointers.pointers[Index.NUM_KEYS] = rightNode
                        break

                    # find a location in leaf and insert right node
                    if currNode.pointers.pointers[0] is None:
                        for i in range(len(parent.pointers.pointers)):
                            if parent.pointers.pointers[i] == currNode:
                                if i + 1 < len(parent.pointers.pointers) and parent.pointers.pointers[i+1] is not None:
                                    rightNode.pointers.pointers[Index.NUM_KEYS] = parent.pointers.pointers[i+1]
                                parent.pointers.pointers.insert(i+1, rightNode)
                                break
                        rightNode = []
                        if len(parent.pointers.pointers) == 4 and parent.pointers.pointers[3] is None:
                            parent.pointers.pointers.pop()

                    # insert right parent if it exist
                    if rightNode:
                        for i in range(len(parent.pointers.pointers)):
                            if parent.pointers.pointers[i] == currNode:
                                parent.pointers.pointers.insert(i + 1, rightNode)
                                break
                        rightNode = []
                        if len(parent.pointers.pointers) == 4 and parent.pointers.pointers[3] is None:
                            parent.pointers.pointers.pop()

                    # add split key to parent
                    if None in parent.keys.keys:
                        # space is available
                        parent.keys.keys = [min(parent.keys.keys[0], key), max(parent.keys.keys[0], key)]
                    else:
                        # no space, split to the next level
                        nums = sorted([parent.keys.keys[0], parent.keys.keys[1], key])
                        rightNode = Node(KeySet([nums[2], None]), PointerSet([parent.pointers.pointers[2], parent.pointers.pointers[3], None]))
                        parent.keys = KeySet([nums[0], None])
                        parent.pointers = PointerSet([parent.pointers.pointers[0], parent.pointers.pointers[1], None])
                        currNode = parent
                        splitKey.append(nums[1])

                if path:
                    parent = path.pop()
                return Index(parent)

        return index

    # Returns a boolean that indicates whether a given key
    # is found among the leaves of a B+-tree index.
    #
    # Complexity: Guaranteed not to touch more nodes than the
    # height of the tree
    @staticmethod
    def LookupKeyInIndex( index, key ):
        currNode = index.root
        currKey = currNode.keys

        if currKey == KeySet([None, None]):
            return False

        while currNode.pointers.pointers[0] is not None:
            # set currKey to the left-most key
            currKeyVal = currKey.keys[0]  # int | None

            ''' Traverse to a leaf node '''

            # case 1: key is less than left-most key
            if key < currKeyVal:
                # None represent the none Node
                if currNode.pointers.pointers[0] is not None:
                    # currNode is not a leaf, go left-side pointer
                    currNode = currNode.pointers.pointers[0]
                    currKey = currNode.keys
                    continue

            # set currKey to the right-most key
            currKeyVal = currKey.keys[1]  # int | None

            # case 2: key is between left-most and right-most keys
            if currKeyVal is None or key < currKeyVal:
                # None represent the none Node
                if currNode.pointers.pointers[0] is not None:
                    # currNode is not a leaf, go middle pointer
                    currNode = currNode.pointers.pointers[1]
                    currKey = currNode.keys
                    continue

            # case 3: key is greater than right-most key
            if currKeyVal and key >= currKeyVal:
                # None represent the none Node
                if currNode.pointers.pointers[0] is not None:
                    # currNode is not a leaf, go right pointer
                    currNode = currNode.pointers.pointers[2]
                    currKey = currNode.keys
                    continue

        ''' check if the leaf nodes contains the key '''
        # check if the keysets contains the key
        if currNode.keys.keys[0] == key:
            return True

        if currNode.keys.keys[1] and currNode.keys.keys[1] == key:
            return True

        return False

    # Returns a list of keys in a B+-tree index within the half-open
    # interval [lower_bound, upper_bound)
    #
    # Complexity: Guaranteed not to touch more nodes than the height
    # of the tree and the number of leaves overlapping the interval.
    @staticmethod
    def RangeSearchInIndex( index, lower_bound, upper_bound ):
        answer = []
        key = lower_bound
        currNode = index.root
        currKey = currNode.keys

        if currKey == KeySet([None, None]):
            return answer

        while currNode.pointers.pointers[0] is not None:
            # set currKey to the left-most key
            currKeyVal = currKey.keys[0]  # int | None

            ''' Traverse to a leaf node '''

            # case 1: key is less than left-most key
            if key < currKeyVal:
                # None represent the none Node
                if currNode.pointers.pointers[0] is not None:
                    # currNode is not a leaf, go left-side pointer
                    currNode = currNode.pointers.pointers[0]
                    currKey = currNode.keys
                    continue

            # set currKey to the right-most key
            currKeyVal = currKey.keys[1]  # int | None

            # case 2: key is between left-most and right-most keys
            if currKeyVal is None or key < currKeyVal:
                # None represent the none Node
                if currNode.pointers.pointers[0] is not None:
                    # currNode is not a leaf, go middle pointer
                    currNode = currNode.pointers.pointers[1]
                    currKey = currNode.keys
                    continue

            # case 3: key is greater than right-most key
            if currKeyVal and key >= currKeyVal:
                # None represent the none Node
                if currNode.pointers.pointers[0] is not None:
                    # currNode is not a leaf, go right pointer
                    currNode = currNode.pointers.pointers[2]
                    currKey = currNode.keys
                    continue

        ''' get a range '''
        while currNode:
            # check if the keysets in the range
            if lower_bound <= currNode.keys.keys[0] < upper_bound:
                answer.append(currNode.keys.keys[0])

            if currNode.keys.keys[0] >= upper_bound:
                break

            if currNode.keys.keys[1]:
                if lower_bound <= currNode.keys.keys[1] < upper_bound:
                    answer.append(currNode.keys.keys[1])

                if currNode.keys.keys[1] >= upper_bound:
                    break

            currNode = currNode.pointers.pointers[2]

        return answer