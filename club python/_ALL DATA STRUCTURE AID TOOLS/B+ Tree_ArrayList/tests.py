# Test cases for ImplementMe class.
# The mocked objects (and therefore expected output) may change
# at the point of evaluation, including into a more complex object,  
# and the functionality tested by each test case may increase in difficulty.
# Your implementation should anticipate ways in which these mocks
# or tests could be more complex, as well as design mocks
# for some disclosed but not written test cases.

import unittest
import time
import timeout_decorator
from node import *
from index import *
from implement_me import ImplementMe


# Insert into an empty tree
class TestCase01(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        root = Node()
        btree = Index( root )

        key = 99

        newRoot = Node(\
            KeySet([99,None]),\
            PointerSet([None]*Index.FAN_OUT))

        expected_output = Index( newRoot )

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )

# Insert existing key
class TestCase02(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        root = Node(\
            KeySet([99,None]),\
            PointerSet([None]*Index.FAN_OUT))
        btree = Index( root )

        key = 99

        newRoot = Node(\
            KeySet([99,None]),\
            PointerSet([None]*Index.FAN_OUT))
        expected_output = Index( newRoot )

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )

# Insert into existing node that is not full
class TestCase03(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        root = Node(\
            KeySet([87, None]),\
            PointerSet([None]*Index.FAN_OUT))
        btree = Index( root )

        key = 66

        newRoot = Node(\
            KeySet([66, 87]),\
            PointerSet([None]*Index.FAN_OUT))
        expected_output = Index( newRoot )

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )

# Insert into full node.
class TestCase04(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        root = Node(\
            KeySet([66, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        btree = Index( root )

        key = 87

        leaf1 = Node( \
            KeySet([87, 99]), \
            PointerSet([None] * Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([66, None]), \
            PointerSet([None, None, leaf1]))
        newRoot = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))

        expected_output = Index( newRoot )

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )

# poomon002: split and parent is not full (from right)
class TestCaseV(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):
        # 66, 75, 80
        rootLeft = Node(KeySet([66, None]), PointerSet([None] * Index.FAN_OUT))
        rootMiddle = Node(KeySet([75, 80]), PointerSet([None] * Index.FAN_OUT))
        rootRight = None

        rootLeft.pointers.pointers[Index.NUM_KEYS] = rootMiddle

        root = Node(KeySet([75, None]), PointerSet([rootLeft, rootMiddle, rootRight]))

        btree = Index(root)

        key = 100

        rootLeft_E = Node(KeySet([66, None]), PointerSet([None] * Index.FAN_OUT))
        rootMiddle_E = Node(KeySet([75, None]), PointerSet([None] * Index.FAN_OUT))
        rootRight_E = Node(KeySet([80, 100]), PointerSet([None] * Index.FAN_OUT))

        rootLeft_E.pointers.pointers[Index.NUM_KEYS] = rootMiddle_E
        rootMiddle_E.pointers.pointers[Index.NUM_KEYS] = rootRight_E

        root_E = Node(KeySet([75, 80]), PointerSet([rootLeft_E, rootMiddle_E, rootRight_E]))

        expected_output = Index(root_E)

        self.assertEqual(expected_output, ImplementMe.InsertIntoIndex(btree, key))

# poomon003: split and parent is not full (from left)
class TestCaseVI(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):
        # 66, 75, 80, 70
        rootLeft = Node(KeySet([66, 70]), PointerSet([None] * Index.FAN_OUT))
        rootMiddle = Node(KeySet([75, 80]), PointerSet([None] * Index.FAN_OUT))
        rootRight = None

        rootLeft.pointers.pointers[Index.NUM_KEYS] = rootMiddle

        root = Node(KeySet([75, None]), PointerSet([rootLeft, rootMiddle, rootRight]))

        btree = Index(root)

        key = 10

        rootLeft_E = Node(KeySet([10, None]), PointerSet([None] * Index.FAN_OUT))
        rootMiddle_E = Node(KeySet([66, 70]), PointerSet([None] * Index.FAN_OUT))
        rootRight_E = Node(KeySet([75, 80]), PointerSet([None] * Index.FAN_OUT))

        rootLeft_E.pointers.pointers[Index.NUM_KEYS] = rootMiddle_E
        rootMiddle_E.pointers.pointers[Index.NUM_KEYS] = rootRight_E

        root_E = Node(KeySet([66, 75]), PointerSet([rootLeft_E, rootMiddle_E, rootRight_E]))

        expected_output = Index(root_E)

        self.assertEqual(expected_output, ImplementMe.InsertIntoIndex(btree, key))

# poomon004: add node from third level to second level after spliting
class TestCaseVII(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):
        # 66, 75, 80, 100, 95
        rootLeftLeft = Node(KeySet([66, None]), PointerSet([None] * Index.FAN_OUT))
        rootLeftRight = Node(KeySet([75, None]), PointerSet([None] * Index.FAN_OUT))
        rootRightLeft = Node(KeySet([80, None]), PointerSet([None] * Index.FAN_OUT))
        rootRightRight = Node(KeySet([95, 100]), PointerSet([None] * Index.FAN_OUT))

        rootLeftLeft.pointers.pointers[Index.NUM_KEYS] = rootLeftRight
        rootLeftRight.pointers.pointers[Index.NUM_KEYS] = rootRightLeft
        rootRightLeft.pointers.pointers[Index.NUM_KEYS] = rootRightRight

        rootLeft = Node(KeySet([75, None]), PointerSet([rootLeftLeft, rootLeftRight, None]))
        rootRight = Node(KeySet([95, None]), PointerSet([rootRightLeft, rootRightRight, None]))

        root = Node(KeySet([80, None]), PointerSet([rootLeft, rootRight, None]))

        btree = Index(root)

        key = 96

        rootLeftLeft_E = Node(KeySet([66, None]), PointerSet([None] * Index.FAN_OUT))
        rootLeftRight_E = Node(KeySet([75, None]), PointerSet([None] * Index.FAN_OUT))
        rootRightLeft_E = Node(KeySet([80, None]), PointerSet([None] * Index.FAN_OUT))
        rootRightMiddle_E = Node(KeySet([95, None]), PointerSet([None] * Index.FAN_OUT))
        rootRightRight_E = Node(KeySet([96, 100]), PointerSet([None] * Index.FAN_OUT))

        rootLeftLeft_E.pointers.pointers[Index.NUM_KEYS] = rootLeftRight_E
        rootLeftRight_E.pointers.pointers[Index.NUM_KEYS] = rootRightLeft_E
        rootRightLeft_E.pointers.pointers[Index.NUM_KEYS] = rootRightMiddle_E
        rootRightMiddle_E.pointers.pointers[Index.NUM_KEYS] = rootRightRight_E

        rootLeft_E = Node(KeySet([75, None]), PointerSet([rootLeftLeft_E, rootLeftRight_E, None]))
        rootRight_E = Node(KeySet([95, 96]), PointerSet([rootRightLeft_E, rootRightMiddle_E, rootRightRight_E]))

        root_E = Node(KeySet([80, None]), PointerSet([rootLeft_E, rootRight_E, None]))

        expected_output = Index(root_E)

        self.assertEqual(expected_output, ImplementMe.InsertIntoIndex(btree, key))

# poomon005: add node from third level to second level after spliting
class TestCaseIX(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):
        # 66, 75, 80, 100, 50, 77, 78, 10
        rootLeftLeft = Node(KeySet([50, 66]), PointerSet([None] * Index.FAN_OUT))
        rootLeftRight = Node(KeySet([75, None]), PointerSet([None] * Index.FAN_OUT))
        rootRightLeft = Node(KeySet([77, 78]), PointerSet([None] * Index.FAN_OUT))
        rootRightRight = Node(KeySet([80, 100]), PointerSet([None] * Index.FAN_OUT))

        rootLeftLeft.pointers.pointers[Index.NUM_KEYS] = rootLeftRight
        rootLeftRight.pointers.pointers[Index.NUM_KEYS] = rootRightLeft
        rootRightLeft.pointers.pointers[Index.NUM_KEYS] = rootRightRight

        rootLeft = Node(KeySet([75, None]), PointerSet([rootLeftLeft, rootLeftRight, None]))
        rootRight = Node(KeySet([80, None]), PointerSet([rootRightLeft, rootRightRight, None]))

        root = Node(KeySet([77, None]), PointerSet([rootLeft, rootRight, None]))

        btree = Index(root)

        key = 10

        rootLeftLeft_E = Node(KeySet([10, None]), PointerSet([None] * Index.FAN_OUT))
        rootLeftMiddle_E = Node(KeySet([50, 66]), PointerSet([None] * Index.FAN_OUT))
        rootLeftRight_E = Node(KeySet([75 ,None]), PointerSet([None] * Index.FAN_OUT))
        rootRightLeft_E = Node(KeySet([77, 78]), PointerSet([None] * Index.FAN_OUT))
        rootRightRight_E = Node(KeySet([80, 100]), PointerSet([None] * Index.FAN_OUT))

        rootLeftLeft_E.pointers.pointers[Index.NUM_KEYS] = rootLeftMiddle_E
        rootLeftMiddle_E.pointers.pointers[Index.NUM_KEYS] = rootLeftRight_E
        rootLeftRight_E.pointers.pointers[Index.NUM_KEYS] = rootRightLeft_E
        rootRightLeft_E.pointers.pointers[Index.NUM_KEYS] = rootRightRight_E

        rootLeft_E = Node(KeySet([50, 75]), PointerSet([rootLeftLeft_E, rootLeftMiddle_E, rootLeftRight_E]))
        rootRight_E = Node(KeySet([80, None]), PointerSet([rootRightLeft_E, rootRightRight_E, None]))

        root_E = Node(KeySet([77, None]), PointerSet([rootLeft_E, rootRight_E, None]))

        expected_output = Index(root_E)

        self.assertEqual(expected_output, ImplementMe.InsertIntoIndex(btree, key))

# poomon006: split in second and third level
class TestCaseVIII(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):
        # 66, 75, 80, 100, 50, 77, 78, 10
        rootLeftLeft = Node(KeySet([10, None]), PointerSet([None] * Index.FAN_OUT))
        rootLeftMiddle = Node(KeySet([50, 66]), PointerSet([None] * Index.FAN_OUT))
        rootLeftRight = Node(KeySet([75, None]), PointerSet([None] * Index.FAN_OUT))
        rootRightLeft = Node(KeySet([77, 78]), PointerSet([None] * Index.FAN_OUT))
        rootRightRight = Node(KeySet([80, 100]), PointerSet([None] * Index.FAN_OUT))

        rootLeftLeft.pointers.pointers[Index.NUM_KEYS] = rootLeftMiddle
        rootLeftMiddle.pointers.pointers[Index.NUM_KEYS] = rootLeftRight
        rootLeftRight.pointers.pointers[Index.NUM_KEYS] = rootRightLeft
        rootRightLeft.pointers.pointers[Index.NUM_KEYS] = rootRightRight

        rootLeft = Node(KeySet([50, 75]), PointerSet([rootLeftLeft, rootLeftMiddle, rootLeftRight]))
        rootRight = Node(KeySet([80, None]), PointerSet([rootRightLeft, rootRightRight, None]))

        root = Node(KeySet([77, None]), PointerSet([rootLeft, rootRight, None]))

        btree = Index(root)

        key = 67

        rootLeftLeft_E = Node(KeySet([10, None]), PointerSet([None] * Index.FAN_OUT))
        rootLeftRight_E = Node(KeySet([50, None]), PointerSet([None] * Index.FAN_OUT))

        rootMiddleLeft_E = Node(KeySet([66, 67]), PointerSet([None] * Index.FAN_OUT))
        rootMiddleRight_E = Node(KeySet([75, None]), PointerSet([None] * Index.FAN_OUT))

        rootRightLeft_E = Node(KeySet([77, 78]), PointerSet([None] * Index.FAN_OUT))
        rootRightRight_E = Node(KeySet([80, 100]), PointerSet([None] * Index.FAN_OUT))

        rootLeftLeft_E.pointers.pointers[Index.NUM_KEYS] = rootLeftRight_E
        rootLeftRight_E.pointers.pointers[Index.NUM_KEYS] = rootMiddleLeft_E
        rootMiddleLeft_E.pointers.pointers[Index.NUM_KEYS] = rootMiddleRight_E
        rootMiddleRight_E.pointers.pointers[Index.NUM_KEYS] = rootRightLeft_E
        rootRightLeft_E.pointers.pointers[Index.NUM_KEYS] = rootRightRight_E

        rootLeft_E = Node(KeySet([50, None]), PointerSet([rootLeftLeft_E, rootLeftRight_E, None]))
        rootMiddle_E = Node(KeySet([75, None]), PointerSet([rootMiddleLeft_E, rootMiddleRight_E, None]))
        rootRight_E = Node(KeySet([80, None]), PointerSet([rootRightLeft_E, rootRightRight_E, None]))

        root_E = Node(KeySet([66, 77]), PointerSet([rootLeft_E, rootMiddle_E, rootRight_E]))

        expected_output = Index(root_E)

        self.assertEqual(expected_output, ImplementMe.InsertIntoIndex(btree, key))

# poomon007: split to forth level
class TestCaseX(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):
        # 66, 75, 80, 100, 50, 77, 78, 10, 67, 70
        rootLeftLeft = Node(KeySet([10, None]), PointerSet([None] * Index.FAN_OUT))
        rootLeftRight = Node(KeySet([50, None]), PointerSet([None] * Index.FAN_OUT))

        rootMiddleLeft = Node(KeySet([66, None]), PointerSet([None] * Index.FAN_OUT))
        rootMiddleMiddle = Node(KeySet([67, 70]), PointerSet([None] * Index.FAN_OUT))
        rootMiddleRight = Node(KeySet([75, None]), PointerSet([None] * Index.FAN_OUT))

        rootRightLeft = Node(KeySet([77, 78]), PointerSet([None] * Index.FAN_OUT))
        rootRightRight = Node(KeySet([80, 100]), PointerSet([None] * Index.FAN_OUT))

        rootLeftLeft.pointers.pointers[Index.NUM_KEYS] = rootLeftRight
        rootLeftRight.pointers.pointers[Index.NUM_KEYS] = rootMiddleLeft
        rootMiddleLeft.pointers.pointers[Index.NUM_KEYS] = rootMiddleMiddle
        rootMiddleMiddle.pointers.pointers[Index.NUM_KEYS] = rootMiddleRight
        rootMiddleRight.pointers.pointers[Index.NUM_KEYS] = rootRightLeft
        rootRightLeft.pointers.pointers[Index.NUM_KEYS] = rootRightRight

        rootLeft = Node(KeySet([50, None]), PointerSet([rootLeftLeft, rootLeftRight, None]))
        rootMiddle = Node(KeySet([67, 75]), PointerSet([rootMiddleLeft, rootMiddleMiddle, rootMiddleRight]))
        rootRight = Node(KeySet([80, None]), PointerSet([rootRightLeft, rootRightRight, None]))

        root = Node(KeySet([66, 77]), PointerSet([rootLeft, rootMiddle, rootRight]))

        btree = Index(root)

        key = 69

        rootLeftLeftLeft_E = Node(KeySet([10, None]), PointerSet([None] * Index.FAN_OUT))
        rootLeftLeftRight_E = Node(KeySet([50, None]), PointerSet([None] * Index.FAN_OUT))

        rootLeftRightLeft_E = Node(KeySet([66, None]), PointerSet([None] * Index.FAN_OUT))
        rootLeftRightRight_E = Node(KeySet([67, None]), PointerSet([None] * Index.FAN_OUT))

        rootRightLeftLeft_E = Node(KeySet([69, 70]), PointerSet([None] * Index.FAN_OUT))
        rootRightLeftRight_E = Node(KeySet([75, None]), PointerSet([None] * Index.FAN_OUT))

        rootRightRightLeft_E = Node(KeySet([77, 78]), PointerSet([None] * Index.FAN_OUT))
        rootRightRightRight_E = Node(KeySet([80, 100]), PointerSet([None] * Index.FAN_OUT))

        rootLeftLeftLeft_E.pointers.pointers[Index.NUM_KEYS] = rootLeftLeftRight_E
        rootLeftLeftRight_E.pointers.pointers[Index.NUM_KEYS] = rootLeftRightLeft_E
        rootLeftRightLeft_E.pointers.pointers[Index.NUM_KEYS] = rootLeftRightRight_E
        rootLeftRightRight_E.pointers.pointers[Index.NUM_KEYS] = rootRightLeftLeft_E
        rootRightLeftLeft_E.pointers.pointers[Index.NUM_KEYS] = rootRightLeftRight_E
        rootRightLeftRight_E.pointers.pointers[Index.NUM_KEYS] = rootRightRightLeft_E
        rootRightRightLeft_E.pointers.pointers[Index.NUM_KEYS] = rootRightRightRight_E

        rootLeftLeft_E = Node(KeySet([50, None]), PointerSet([rootLeftLeftLeft_E, rootLeftLeftRight_E, None]))
        rootLeftRight_E = Node(KeySet([67, None]), PointerSet([rootLeftRightLeft_E, rootLeftRightRight_E, None]))

        rootRightLeft_E = Node(KeySet([75, None]), PointerSet([rootRightLeftLeft_E, rootRightLeftRight_E, None]))
        rootRightRight_E = Node(KeySet([80, None]), PointerSet([rootRightRightLeft_E, rootRightRightRight_E, None]))

        rootLeft_E = Node(KeySet([50, None]), PointerSet([rootLeftLeft_E, rootLeftRight_E, None]))
        rootRight_E = Node(KeySet([80, None]), PointerSet([rootRightLeft_E, rootRightRight_E, None]))

        root_E = Node(KeySet([69, None]), PointerSet([rootLeft_E, rootRight_E, None]))

        expected_output = Index(root_E)

        self.assertEqual(expected_output, ImplementMe.InsertIntoIndex(btree, key))

class TestCaseXVIIII(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):
        # 66, 75, 80, 100, 50, 77, 78, 10, 67, 70
        rootLeftLeft = Node(KeySet([10, None]), PointerSet([None] * Index.FAN_OUT))
        rootLeftRight = Node(KeySet([50, None]), PointerSet([None] * Index.FAN_OUT))

        rootMiddleLeft = Node(KeySet([66, None]), PointerSet([None] * Index.FAN_OUT))
        rootMiddleMiddle = Node(KeySet([67, 70]), PointerSet([None] * Index.FAN_OUT))
        rootMiddleRight = Node(KeySet([75, None]), PointerSet([None] * Index.FAN_OUT))

        rootRightLeft = Node(KeySet([77, 78]), PointerSet([None] * Index.FAN_OUT))
        rootRightRight = Node(KeySet([80, 100]), PointerSet([None] * Index.FAN_OUT))

        rootLeftLeft.pointers.pointers[Index.NUM_KEYS] = rootLeftRight
        rootLeftRight.pointers.pointers[Index.NUM_KEYS] = rootMiddleLeft
        rootMiddleLeft.pointers.pointers[Index.NUM_KEYS] = rootMiddleMiddle
        rootMiddleMiddle.pointers.pointers[Index.NUM_KEYS] = rootMiddleRight
        rootMiddleRight.pointers.pointers[Index.NUM_KEYS] = rootRightLeft
        rootRightLeft.pointers.pointers[Index.NUM_KEYS] = rootRightRight

        rootLeft = Node(KeySet([50, None]), PointerSet([rootLeftLeft, rootLeftRight, None]))
        rootMiddle = Node(KeySet([67, 75]), PointerSet([rootMiddleLeft, rootMiddleMiddle, rootMiddleRight]))
        rootRight = Node(KeySet([80, None]), PointerSet([rootRightLeft, rootRightRight, None]))

        root = Node(KeySet([66, 77]), PointerSet([rootLeft, rootMiddle, rootRight]))

        btree = Index(root)
        keys = [66, 75, 80, 100, 50, 77, 78, 10, 67, 70]
        for key in keys:
            expected_output = True
            self.assertEqual(expected_output, ImplementMe.LookupKeyInIndex(btree, key))


# Insert into full node with full parent, causing root split.
# Not shown. To be designed by student.
class TestCase05(unittest.TestCase):
    @timeout_decorator.timeout(25)
    def test_insertion(self):
        leaf3 = Node(KeySet([8, 9]), PointerSet([None] * 3))
        leaf2 = Node(KeySet([6, None]), PointerSet([None, None, leaf3]))
        leaf1 = Node(KeySet([1, None]), PointerSet([None, None, leaf2]))

        root = Node(KeySet([6, 8]), PointerSet([leaf1, leaf2, leaf3]))

        btree = Index(root)

        key = 10

        leaf3 = Node(KeySet([9, 10]), PointerSet([None] * 3))
        leaf2 = Node(KeySet([8, None]), PointerSet([None, None, leaf3]))
        leaf1 = Node(KeySet([6, None]), PointerSet([None, None, leaf2]))
        leaf = Node(KeySet([1, None]), PointerSet([None, None, leaf1]))

        mid2 = Node(KeySet([6, None]), PointerSet([leaf, leaf1, None]))
        mid3 = Node(KeySet([9, None]), PointerSet([leaf2, leaf3, None]))

        root = Node(KeySet([8, None]), PointerSet([mid2, mid3, None]))

        expected_output = Index(root)

        self.assertEqual(expected_output, ImplementMe.InsertIntoIndex(btree, key))


# Insert into full node with full parent, but does not cause a root split.
class TestCase06(unittest.TestCase):
    @timeout_decorator.timeout(25)
    def test_insertion(self):

        leaf4 = Node(\
            KeySet([97,99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf3 = Node(\
            KeySet([87, None]),\
            PointerSet([None,None,leaf4]))
        leaf2 = Node(\
            KeySet([66,None]),\
            PointerSet([None,None,leaf3]))
        leaf1 = Node(\
            KeySet([27,None]),\
            PointerSet([None,None,leaf2]))
        leaf0 = Node(\
            KeySet([7,9]),\
            PointerSet([None,None,leaf1]))
        parent1 = Node(\
            KeySet([97,None]),\
            PointerSet([leaf3,leaf4,None]))
        parent0 = Node(\
            KeySet([27,66]),\
            PointerSet([leaf0,leaf1,leaf2]))
        root = Node(\
            KeySet([87,None]),\
            PointerSet([parent0,parent1,None]))
        btree = Index(root)

        key = 5

        newLeaf5 = Node(\
            KeySet([97,99]),\
            PointerSet([None]*Index.FAN_OUT))
        newLeaf4 = Node(\
            KeySet([87, None]),\
            PointerSet([None,None,newLeaf5]))
        newLeaf3 = Node(\
            KeySet([66,None]),\
            PointerSet([None,None,newLeaf4]))
        newLeaf2 = Node(\
            KeySet([27,None]),\
            PointerSet([None,None,newLeaf3]))
        newLeaf1 = Node(\
            KeySet([7,9]),\
            PointerSet([None,None,newLeaf2]))
        newLeaf0 = Node(\
            KeySet([5,None]),\
            PointerSet([None,None,newLeaf1]))
        newParent2 = Node(\
            KeySet([97,None]),\
            PointerSet([newLeaf4,newLeaf5,None]))
        newParent1 = Node(\
            KeySet([66,None]),\
            PointerSet([newLeaf2,newLeaf3,None]))
        newParent0 = Node(\
            KeySet([7,None]),\
            PointerSet([newLeaf0,newLeaf1,None]))
        newRoot = Node(\
            KeySet([27,87]),\
            PointerSet([newParent0,newParent1,newParent2]))
        expected_output = Index(newRoot)

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )

# Insertion causes splits that propagates at least three times: : split at the right-most leaf
class TestCase07(unittest.TestCase):
    @timeout_decorator.timeout(25)
    def test_insertion(self):
        leaf7 = Node(KeySet([7, 8]), PointerSet([None] * 3))
        leaf6 = Node(KeySet([6, None]), PointerSet([None, None, leaf7]))
        leaf5 = Node(KeySet([5, None]), PointerSet([None, None, leaf6]))
        leaf4 = Node(KeySet([4, None]), PointerSet([None, None, leaf5]))
        leaf3 = Node(KeySet([3, None]), PointerSet([None, None, leaf4]))
        leaf2 = Node(KeySet([2, None]), PointerSet([None, None, leaf3]))
        leaf1 = Node(KeySet([1, None]), PointerSet([None, None, leaf2]))

        mid3 = Node(KeySet([6, 7]), PointerSet([leaf5, leaf6, leaf7]))
        mid2 = Node(KeySet([4, None]), PointerSet([leaf3, leaf4, None]))
        mid1 = Node(KeySet([2, None]), PointerSet([leaf1, leaf2, None]))

        root = Node(KeySet([3, 5]), PointerSet([mid1, mid2, mid3]))
        btree = Index(root)

        key = 9

        leaf8 = Node(KeySet([8, 9]), PointerSet([None] * 3))
        leaf7 = Node(KeySet([7, None]), PointerSet([None, None, leaf8]))
        leaf6 = Node(KeySet([6, None]), PointerSet([None, None, leaf7]))
        leaf5 = Node(KeySet([5, None]), PointerSet([None, None, leaf6]))
        leaf4 = Node(KeySet([4, None]), PointerSet([None, None, leaf5]))
        leaf3 = Node(KeySet([3, None]), PointerSet([None, None, leaf4]))
        leaf2 = Node(KeySet([2, None]), PointerSet([None, None, leaf3]))
        leaf1 = Node(KeySet([1, None]), PointerSet([None, None, leaf2]))

        mid8 = Node(KeySet([8, None]), PointerSet([leaf7, leaf8, None]))
        mid6 = Node(KeySet([6, None]), PointerSet([leaf5, leaf6, None]))
        mid4 = Node(KeySet([4, None]), PointerSet([leaf3, leaf4, None]))
        mid2 = Node(KeySet([2, None]), PointerSet([leaf1, leaf2, None]))

        upper7 = Node(KeySet([7, None]), PointerSet([mid6, mid8, None]))
        upper3 = Node(KeySet([3, None]), PointerSet([mid2, mid4, None]))

        root = Node(KeySet([5, None]), PointerSet([upper3, upper7, None]))

        expected_output = Index(root)

        self.assertEqual(expected_output, ImplementMe.InsertIntoIndex(btree, key))

# Insertion causes splits that propagates at least three times: split at the left-most leaf
class TestCaseXIV(unittest.TestCase):
    @timeout_decorator.timeout(25)
    def test_insertion(self):
        # 1, 5, 10, 15, 20, 25,30,35, 7, 12, 17, 3, 4, 0
        leaf7 = Node(KeySet([30, 35]), PointerSet([None] * 3))
        leaf6 = Node(KeySet([25, None]), PointerSet([None, None, leaf7]))
        leaf5 = Node(KeySet([20, None]), PointerSet([None, None, leaf6]))
        leaf4 = Node(KeySet([15, 17]), PointerSet([None, None, leaf5]))
        leaf3 = Node(KeySet([10, 12]), PointerSet([None, None, leaf4]))
        leaf2 = Node(KeySet([5, 7]), PointerSet([None, None, leaf3]))
        leaf1 = Node(KeySet([3, 4]), PointerSet([None, None, leaf2]))
        leaf0 = Node(KeySet([0, 1]), PointerSet([None, None, leaf1]))

        mid3 = Node(KeySet([25, 30]), PointerSet([leaf5, leaf6, leaf7]))
        mid2 = Node(KeySet([15, None]), PointerSet([leaf3, leaf4, None]))
        mid1 = Node(KeySet([3, 5]), PointerSet([leaf0, leaf1, leaf2]))

        root = Node(KeySet([10, 20]), PointerSet([mid1, mid2, mid3]))
        btree = Index(root)

        key = 2

        leaf8 = Node(KeySet([30, 35]), PointerSet([None] * 3))
        leaf7 = Node(KeySet([25, None]), PointerSet([None, None, leaf8]))
        leaf6 = Node(KeySet([20, None]), PointerSet([None, None, leaf7]))
        leaf5 = Node(KeySet([15, 17]), PointerSet([None, None, leaf6]))
        leaf4 = Node(KeySet([10, 12]), PointerSet([None, None, leaf5]))
        leaf3 = Node(KeySet([5, 7]), PointerSet([None, None, leaf4]))
        leaf2 = Node(KeySet([3, 4]), PointerSet([None, None, leaf3]))
        leaf1 = Node(KeySet([1, 2]), PointerSet([None, None, leaf2]))
        leaf0 = Node(KeySet([0, None]), PointerSet([None, None, leaf1]))

        mid8 = Node(KeySet([25, 30]), PointerSet([leaf6, leaf7, leaf8]))
        mid6 = Node(KeySet([15, None]), PointerSet([leaf4, leaf5, None]))
        mid4 = Node(KeySet([5, None]), PointerSet([leaf2, leaf3, None]))
        mid2 = Node(KeySet([1, None]), PointerSet([leaf0, leaf1, None]))

        upper7 = Node(KeySet([20, None]), PointerSet([mid6, mid8, None]))
        upper3 = Node(KeySet([3, None]), PointerSet([mid2, mid4, None]))

        root = Node(KeySet([10, None]), PointerSet([upper3, upper7, None]))

        expected_output = Index(root)

        self.assertEqual(expected_output, ImplementMe.InsertIntoIndex(btree, key))

# Insertion causes splits that propagates at least three times: split at the right right leaf connecting with another parent leaf
class TestCaseXV(unittest.TestCase):
    @timeout_decorator.timeout(25)
    def test_insertion(self):
        # 1, 5, 10, 15, 20, 25,30,35, 7, 0, 12, 17, 3
        leaf7 = Node(KeySet([30, 35]), PointerSet([None] * 3))
        leaf6 = Node(KeySet([25, None]), PointerSet([None, None, leaf7]))
        leaf5 = Node(KeySet([20, None]), PointerSet([None, None, leaf6]))
        leaf4 = Node(KeySet([15, 17]), PointerSet([None, None, leaf5]))
        leaf3 = Node(KeySet([10, 12]), PointerSet([None, None, leaf4]))
        leaf2 = Node(KeySet([5, 7]), PointerSet([None, None, leaf3]))
        leaf1 = Node(KeySet([1, 3]), PointerSet([None, None, leaf2]))
        leaf0 = Node(KeySet([0, None]), PointerSet([None, None, leaf1]))

        mid3 = Node(KeySet([25, 30]), PointerSet([leaf5, leaf6, leaf7]))
        mid2 = Node(KeySet([15, None]), PointerSet([leaf3, leaf4, None]))
        mid1 = Node(KeySet([1, 5]), PointerSet([leaf0, leaf1, leaf2]))

        root = Node(KeySet([10, 20]), PointerSet([mid1, mid2, mid3]))
        btree = Index(root)

        key = 6

        leaf8 = Node(KeySet([30, 35]), PointerSet([None] * 3))
        leaf7 = Node(KeySet([25, None]), PointerSet([None, None, leaf8]))
        leaf6 = Node(KeySet([20, None]), PointerSet([None, None, leaf7]))
        leaf5 = Node(KeySet([15, 17]), PointerSet([None, None, leaf6]))
        leaf4 = Node(KeySet([10, 12]), PointerSet([None, None, leaf5]))
        leaf3 = Node(KeySet([6, 7]), PointerSet([None, None, leaf4]))
        leaf2 = Node(KeySet([5, None]), PointerSet([None, None, leaf3]))
        leaf1 = Node(KeySet([1, 3]), PointerSet([None, None, leaf2]))
        leaf0 = Node(KeySet([0, None]), PointerSet([None, None, leaf1]))

        mid8 = Node(KeySet([25, 30]), PointerSet([leaf6, leaf7, leaf8]))
        mid6 = Node(KeySet([15, None]), PointerSet([leaf4, leaf5, None]))
        mid4 = Node(KeySet([6, None]), PointerSet([leaf2, leaf3, None]))
        mid2 = Node(KeySet([1, None]), PointerSet([leaf0, leaf1, None]))

        upper7 = Node(KeySet([20, None]), PointerSet([mid6, mid8, None]))
        upper3 = Node(KeySet([5, None]), PointerSet([mid2, mid4, None]))

        root = Node(KeySet([10, None]), PointerSet([upper3, upper7, None]))

        expected_output = Index(root)

        self.assertEqual(expected_output, ImplementMe.InsertIntoIndex(btree, key))


# Boundary case: lookup smallest key in tree
class TestCase08(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):

        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([66, None]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        key = 66

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )


# Boundary case: lookup largest key in tree
# Fake data in first node to test complexity
class TestCase09(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):

        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([66, None]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        key = 99

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )


# Lookup key outside range of tree's keys
# Fake data in middle leaf to test complexity
class TestCase10(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):

        root = Node(\
            KeySet([87, None]),\
            PointerSet([None]*Index.FAN_OUT))
        btree = Index( root )

        key = 99

        expected_output = False

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )

class TestCaseXVI(unittest.TestCase):
    @timeout_decorator.timeout(25)
    def test_insertion(self):
        # 1, 5, 10, 15, 20, 25, 30, 35, 7, 0, 12, 17, 3, 6
        leaf8 = Node(KeySet([30, 35]), PointerSet([None] * 3))
        leaf7 = Node(KeySet([25, None]), PointerSet([None, None, leaf8]))
        leaf6 = Node(KeySet([20, None]), PointerSet([None, None, leaf7]))
        leaf5 = Node(KeySet([15, 17]), PointerSet([None, None, leaf6]))
        leaf4 = Node(KeySet([10, 12]), PointerSet([None, None, leaf5]))
        leaf3 = Node(KeySet([6, 7]), PointerSet([None, None, leaf4]))
        leaf2 = Node(KeySet([5, None]), PointerSet([None, None, leaf3]))
        leaf1 = Node(KeySet([1, 3]), PointerSet([None, None, leaf2]))
        leaf0 = Node(KeySet([0, None]), PointerSet([None, None, leaf1]))

        mid8 = Node(KeySet([25, 30]), PointerSet([leaf6, leaf7, leaf8]))
        mid6 = Node(KeySet([15, None]), PointerSet([leaf4, leaf5, None]))
        mid4 = Node(KeySet([6, None]), PointerSet([leaf2, leaf3, None]))
        mid2 = Node(KeySet([1, None]), PointerSet([leaf0, leaf1, None]))

        upper7 = Node(KeySet([20, None]), PointerSet([mid6, mid8, None]))
        upper3 = Node(KeySet([5, None]), PointerSet([mid2, mid4, None]))

        root = Node(KeySet([10, None]), PointerSet([upper3, upper7, None]))

        btree = Index(root)
        # found but return False
        key = 36
        expected_output = False

        self.assertEqual(expected_output, ImplementMe.LookupKeyInIndex(btree, key))


# Lookup key within tree's range but not in tree
# Fake data in one leaf to test complexity
class TestCase11(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):

        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([41, None]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        key = 66

        expected_output = False

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )

# Lookup key strictly within the tree's range
class TestCase12(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):

        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([41, 66]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        key = 66

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )

# Lookup key strictly within the tree's range
class TestCaseX(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):
        # 66, 75, 80, 100, 95
        rootLeftLeft_E = Node(KeySet([66, None]), PointerSet([None] * Index.FAN_OUT))
        rootLeftRight_E = Node(KeySet([75, None]), PointerSet([None] * Index.FAN_OUT))
        rootRightLeft_E = Node(KeySet([80, None]), PointerSet([None] * Index.FAN_OUT))
        rootRightRight_E = Node(KeySet([95, 100]), PointerSet([None] * Index.FAN_OUT))

        rootLeftLeft_E.pointers.pointers[Index.NUM_KEYS] = rootLeftRight_E
        rootLeftRight_E.pointers.pointers[Index.NUM_KEYS] = rootRightLeft_E
        rootRightLeft_E.pointers.pointers[Index.NUM_KEYS] = rootRightRight_E

        rootLeft_E = Node(KeySet([75, None]), PointerSet([rootLeftLeft_E, rootLeftRight_E, None]))
        rootRight_E = Node(KeySet([95, None]), PointerSet([rootRightLeft_E, rootRightRight_E, None]))

        root_E = Node(KeySet([80, None]), PointerSet([rootLeft_E, rootRight_E, None]))

        btree = Index(root_E)
        key = 0

        expected_output = False

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )

class TestCaseXI(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):
        # 87, 41, 99, 66, 120
        rootLeft = Node(KeySet([41, 66]), PointerSet([None] * Index.FAN_OUT))
        rootMiddle = Node(KeySet([87, None]), PointerSet([None] * Index.FAN_OUT))
        rootRight = Node(KeySet([99, 120]), PointerSet([None] * Index.FAN_OUT))

        rootLeft.pointers.pointers[Index.NUM_KEYS] = rootMiddle
        rootMiddle.pointers.pointers[Index.NUM_KEYS] = rootRight

        root = Node(KeySet([87, 99]), PointerSet([rootLeft, rootMiddle, rootRight]))

        btree = Index(root)
        key = 90

        expected_output = False

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )

class TestCaseXIII(unittest.TestCase):
    @timeout_decorator.timeout(25)
    def test_insertion(self):
        # 1, 5, 10, 15, 20, 25,30,35, 7, 0, 12, 17, 3
        leaf7 = Node(KeySet([30, 35]), PointerSet([None] * 3))
        leaf6 = Node(KeySet([25, None]), PointerSet([None, None, leaf7]))
        leaf5 = Node(KeySet([20, None]), PointerSet([None, None, leaf6]))
        leaf4 = Node(KeySet([15, 17]), PointerSet([None, None, leaf5]))
        leaf3 = Node(KeySet([10, 12]), PointerSet([None, None, leaf4]))
        leaf2 = Node(KeySet([5, 7]), PointerSet([None, None, leaf3]))
        leaf1 = Node(KeySet([1, 3]), PointerSet([None, None, leaf2]))
        leaf0 = Node(KeySet([0, None]), PointerSet([None, None, leaf1]))

        mid3 = Node(KeySet([25, 30]), PointerSet([leaf5, leaf6, leaf7]))
        mid2 = Node(KeySet([15, None]), PointerSet([leaf3, leaf4, None]))
        mid1 = Node(KeySet([1, 5]), PointerSet([leaf0, leaf1, leaf2]))

        root = Node(KeySet([10, 20]), PointerSet([mid1, mid2, mid3]))
        btree = Index(root)

        key = 20

        expected_output = True

        self.assertEqual(expected_output, ImplementMe.LookupKeyInIndex(btree, key))


# Range query fully contained in one leaf node
class TestCase13(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):
        leaf1 = Node( \
            KeySet([3, 4]), \
            PointerSet([None] * Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([0, 1]), \
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([2, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        key = 2

        expected_output = False

        self.assertEqual(expected_output, ImplementMe.LookupKeyInIndex(btree, key))

# Range query fully contained in one leaf node
class TestCaseXI(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):
        leaf1 = Node(\
            KeySet([25, 40]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([21, 33]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([25, 40]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        key = 33

        expected_output = False

        self.assertEqual(expected_output, ImplementMe.LookupKeyInIndex(btree, key))

        lower_bound = 20
        upper_bound = 30

        expected_output = [21]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )

class TestCaseXII(unittest.TestCase):
    @timeout_decorator.timeout(25)
    def test_insertion(self):
        # 1, 5, 10, 15, 20, 25,30,35, 7, 0, 12, 17, 3
        leaf7 = Node(KeySet([30, 35]), PointerSet([None] * 3))
        leaf6 = Node(KeySet([25, None]), PointerSet([None, None, leaf7]))
        leaf5 = Node(KeySet([20, None]), PointerSet([None, None, leaf6]))
        leaf4 = Node(KeySet([15, 17]), PointerSet([None, None, leaf5]))
        leaf3 = Node(KeySet([10, 12]), PointerSet([None, None, leaf4]))
        leaf2 = Node(KeySet([5, 7]), PointerSet([None, None, leaf3]))
        leaf1 = Node(KeySet([1, 3]), PointerSet([None, None, leaf2]))
        leaf0 = Node(KeySet([0, None]), PointerSet([None, None, leaf1]))

        mid3 = Node(KeySet([25, 30]), PointerSet([leaf5, leaf6, leaf7]))
        mid2 = Node(KeySet([15, None]), PointerSet([leaf3, leaf4, None]))
        mid1 = Node(KeySet([1, 5]), PointerSet([leaf0, leaf1, leaf2]))

        root = Node(KeySet([10, 20]), PointerSet([mid1, mid2, mid3]))
        btree = Index(root)

        lower_bound = -1
        upper_bound = 8

        expected_output = [0,1,3,5,7]

        self.assertEqual(expected_output, ImplementMe.RangeSearchInIndex(btree, lower_bound, upper_bound))


# Range query half-open to the left
class TestCase14(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):
        # 87, 99, 68, 41
        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([41, 68]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        lower_bound = 0
        upper_bound = 42

        expected_output = [41]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Range query half-open to the right
class TestCase15(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):
        # 87, 99, 68, 41
        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([41, 68]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        lower_bound = 42
        upper_bound = 1024

        expected_output = [68,87,99]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Range query with matching upper and lower bound
class TestCase16(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):

        btree = Index(Node(\
            KeySet([7,None]),\
            PointerSet([None]*Index.FAN_OUT)))

        lower_bound = 7
        upper_bound = 7

        expected_output = []

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Multi-leaf range query in middle of tree
class TestCase17(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):
        # 66, 75, 80, 100, 50, 77, 78, 10, 67, 70
        rootLeftLeft = Node(KeySet([10, None]), PointerSet([None] * Index.FAN_OUT))
        rootLeftRight = Node(KeySet([50, None]), PointerSet([None] * Index.FAN_OUT))

        rootMiddleLeft = Node(KeySet([66, None]), PointerSet([None] * Index.FAN_OUT))
        rootMiddleMiddle = Node(KeySet([67, 70]), PointerSet([None] * Index.FAN_OUT))
        rootMiddleRight = Node(KeySet([75, None]), PointerSet([None] * Index.FAN_OUT))

        rootRightLeft = Node(KeySet([77, 78]), PointerSet([None] * Index.FAN_OUT))
        rootRightRight = Node(KeySet([80, 100]), PointerSet([None] * Index.FAN_OUT))

        rootLeftLeft.pointers.pointers[Index.NUM_KEYS] = rootLeftRight
        rootLeftRight.pointers.pointers[Index.NUM_KEYS] = rootMiddleLeft
        rootMiddleLeft.pointers.pointers[Index.NUM_KEYS] = rootMiddleMiddle
        rootMiddleMiddle.pointers.pointers[Index.NUM_KEYS] = rootMiddleRight
        rootMiddleRight.pointers.pointers[Index.NUM_KEYS] = rootRightLeft
        rootRightLeft.pointers.pointers[Index.NUM_KEYS] = rootRightRight

        rootLeft = Node(KeySet([50, None]), PointerSet([rootLeftLeft, rootLeftRight, None]))
        rootMiddle = Node(KeySet([67, 75]), PointerSet([rootMiddleLeft, rootMiddleMiddle, rootMiddleRight]))
        rootRight = Node(KeySet([80, None]), PointerSet([rootRightLeft, rootRightRight, None]))

        root = Node(KeySet([66, 77]), PointerSet([rootLeft, rootMiddle, rootRight]))

        btree = Index(root)

        lower_bound = 77
        upper_bound = 100

        expected_output = [77, 78, 80]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Lookup recently added key
class TestCase18(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_unknown(self):

        btree = Index(Node(\
            KeySet([99,None]),\
            PointerSet([None]*Index.FAN_OUT)))

        key = 12

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex(\
        ImplementMe.InsertIntoIndex( btree, key ), key ) )



# Lookup range that includes recently added key
class TestCase19(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_unknown(self):

        leaf4 = Node(\
            KeySet([97,99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf3 = Node(\
            KeySet([87, None]),\
            PointerSet([None,None,leaf4]))
        leaf2 = Node(\
            KeySet([66,None]),\
            PointerSet([None,None,leaf3]))
        leaf1 = Node(\
            KeySet([27,None]),\
            PointerSet([None,None,leaf2]))
        leaf0 = Node(\
            KeySet([7,9]),\
            PointerSet([None,None,leaf1]))
        parent1 = Node(\
            KeySet([97,None]),\
            PointerSet([leaf3,leaf4,None]))
        parent0 = Node(\
            KeySet([27,66]),\
            PointerSet([leaf0,leaf1,leaf2]))
        root = Node(\
            KeySet([87,None]),\
            PointerSet([parent0,parent1,None]))
        btree = Index(root)

        key = 5
        lower_bound = 1
        upper_bound = 68

        expected_output = [5,7,9,27,66]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex(\
        ImplementMe.InsertIntoIndex( btree, key ), lower_bound, upper_bound ) )


# Lookup range with nearly matching lower and upper bound equal to recently added key
class TestCase20(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_unknown(self):
        # 87, 99, 68, 41
        leaf1 = Node( \
            KeySet([87, 99]), \
            PointerSet([None] * Index.FAN_OUT))
        leaf0 = Node( \
            KeySet([41, 68]), \
            PointerSet([None, None, leaf1]))
        root = Node( \
            KeySet([87, None]), \
            PointerSet([leaf0, leaf1, None]))
        btree = Index(root)

        key = 12
        lower_bound = 12
        upper_bound = 13

        expected_output = [12]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex(\
        ImplementMe.InsertIntoIndex( btree, key ), lower_bound, upper_bound ) )

class TestCaseIC(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        root =  Node(\
            KeySet([99,None]),\
            PointerSet([None]*Index.FAN_OUT))

        btree = Index( root )

        lower_bound = 0
        upper_bound = 99

        expected_output = []

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )

# Insert into full node with full parent, but does not cause a root split.
class TestCaseC(unittest.TestCase):
    @timeout_decorator.timeout(25)
    def test_insertion(self):
        leaf5 = Node(KeySet([5, 6]), PointerSet([None] * Index.FAN_OUT))
        leaf4 = Node(KeySet([4, None]), PointerSet([None, None, leaf5]))
        leaf3 = Node(KeySet([3, None]), PointerSet([None, None, leaf4]))
        leaf2 = Node(KeySet([2, None]), PointerSet([None, None, leaf3]))
        leaf1 = Node(KeySet([1, None]), PointerSet([None, None, leaf2]))

        mid2 = Node(KeySet([4, 5]), PointerSet([leaf3, leaf4, leaf5]))
        mid1 = Node(KeySet([2, None]), PointerSet([leaf1, leaf2, None]))

        root = Node(KeySet([3, None]), PointerSet([mid1, mid2, None]))

        btree = Index(root)

        key = 7

        leaf6 = Node(KeySet([6, 7]), PointerSet([None] * Index.FAN_OUT))
        leaf5 = Node(KeySet([5, None]), PointerSet([None, None, leaf6]))
        leaf4 = Node(KeySet([4, None]), PointerSet([None, None, leaf5]))
        leaf3 = Node(KeySet([3, None]), PointerSet([None, None, leaf4]))
        leaf2 = Node(KeySet([2, None]), PointerSet([None, None, leaf3]))
        leaf1 = Node(KeySet([1, None]), PointerSet([None, None, leaf2]))

        mid3 = Node(KeySet([6, None]), PointerSet([leaf5, leaf6, None]))
        mid2 = Node(KeySet([4, None]), PointerSet([leaf3, leaf4, None]))
        mid1 = Node(KeySet([2, None]), PointerSet([leaf1, leaf2, None]))

        root = Node(KeySet([3, 5]), PointerSet([mid1, mid2, mid3]))

        expected_output = Index(root)

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )

class TestCaseCI(unittest.TestCase):
    @timeout_decorator.timeout(25)
    def test_insertion(self):
        rightLeaf = Node(KeySet([6, 7]), PointerSet([None] * Index.FAN_OUT))
        middleLeaf = Node(KeySet([4, 5]), PointerSet([None, None, rightLeaf]))
        leftLeaf = Node(KeySet([2, 3]), PointerSet([None, None, middleLeaf]))
        root = Node(KeySet([4, 6]), PointerSet([leftLeaf, middleLeaf, rightLeaf]))
        btree = Index(root)

        key = 1

        leaf4 = Node(KeySet([6, 7]), PointerSet([None]*3))
        leaf3 = Node(KeySet([4, 5]), PointerSet([None, None, leaf4]))
        leaf2 = Node(KeySet([2, 3]), PointerSet([None, None, leaf3]))
        leaf1 = Node(KeySet([1, None]), PointerSet([None, None, leaf2]))
        rightMid = Node(KeySet([6, None]), PointerSet([leaf3,  leaf4, None]))
        leftMid = Node(KeySet([2, None]), PointerSet([leaf1,  leaf2, None]))
        root = Node(KeySet([4, None]), PointerSet([leftMid,  rightMid, None]))

        expected_output = Index(root)

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )

# Range query with matching upper and lower bound
class TestCaseCII(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):
        # 1, 5, 10, 15, 20, 25, 30, 35, 7, 0, 12, 17, 3, 6
        leaf8 = Node(KeySet([30, 35]), PointerSet([None] * 3))
        leaf7 = Node(KeySet([25, None]), PointerSet([None, None, leaf8]))
        leaf6 = Node(KeySet([20, None]), PointerSet([None, None, leaf7]))
        leaf5 = Node(KeySet([15, 17]), PointerSet([None, None, leaf6]))
        leaf4 = Node(KeySet([10, 12]), PointerSet([None, None, leaf5]))
        leaf3 = Node(KeySet([6, 7]), PointerSet([None, None, leaf4]))
        leaf2 = Node(KeySet([5, None]), PointerSet([None, None, leaf3]))
        leaf1 = Node(KeySet([1, 3]), PointerSet([None, None, leaf2]))
        leaf0 = Node(KeySet([0, None]), PointerSet([None, None, leaf1]))

        mid8 = Node(KeySet([25, 30]), PointerSet([leaf6, leaf7, leaf8]))
        mid6 = Node(KeySet([15, None]), PointerSet([leaf4, leaf5, None]))
        mid4 = Node(KeySet([6, None]), PointerSet([leaf2, leaf3, None]))
        mid2 = Node(KeySet([1, None]), PointerSet([leaf0, leaf1, None]))

        upper7 = Node(KeySet([20, None]), PointerSet([mid6, mid8, None]))
        upper3 = Node(KeySet([5, None]), PointerSet([mid2, mid4, None]))

        root = Node(KeySet([10, None]), PointerSet([upper3, upper7, None]))

        btree = Index(root)

        lower_bound = 15
        upper_bound = 16

        expected_output = [15]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )

# Run all unit tests above.
unittest.main(argv=[''],verbosity=2, exit=False)