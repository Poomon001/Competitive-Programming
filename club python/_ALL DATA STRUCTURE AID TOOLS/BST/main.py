class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # case 1: data is already exist then done need to add
        if data == self.data:
            return

        # case 2: data is less than curr data then go to left child
        if data < self.data:
            if self.left:
                # left is not empty, move to the next level of left sub tree to find next leaf node
                self.left.add_child(data)
            else:
                # left is null, simply add new node
                self.left = BSTNode(data)

        # case 3: data is greater than curr data then go to right child
        if data > self.data:
            if self.right:
                # right data is not empty, move to the next level of right sub tree to find next leaf node
                self.right.add_child(data)
            else:
                # right is null, simly add new node
                self.right = BSTNode(data)

    def in_order_traversal(self):
        elem = []

        # left -> root -> right
        if self.left:
            # bebugView = self.left.data;
            elem += self.left.in_order_traversal()

        # base case
        # bebugView = self.data
        elem.append(self.data)

        if self.right:
            # bebugView = self.right.data;
            elem += self.right.in_order_traversal()

        return elem

    def inOrder_traversal_M2(self):
        elem = []
        root = self
        # visit left -> node -> right
        def inOrder(root):
            if root:
                if root.left:
                    inOrder(root.left)

                elem.append(root.data)

                if root.right:
                    inOrder(root.right)

        inOrder(root)

        return elem

    def post_order_traversal(self):
        elem = []

        # left -> right -> root
        if self.left:
            # bebugView = self.left.data;
            elem += self.left.post_order_traversal()

        if self.right:
            # bebugView = self.right.data;
            elem += self.right.post_order_traversal()

        # base case
        # bebugView = self.data
        elem.append(self.data)

        return elem

    def postOrder_traversal_M2(self):
        elem = []
        root = self
        # visit left -> node -> right
        def postOrder(root):
            if root:
                if root.left:
                    postOrder(root.left)

                if root.right:
                    postOrder(root.right)

                elem.append(root.data)

        postOrder(root)

        return elem

    def pre_order_traversal(self):
        elem = []

        # root -> left -> right
        # base case
        # bebugView = self.data
        elem.append(self.data)

        if self.left:
            # bebugView = self.left.data;
            elem += self.left.post_order_traversal()

        if self.right:
            # bebugView = self.right.data;
            elem += self.right.post_order_traversal()

        return elem

    def preOrder_traversal_M2(self):
        elem = []
        root = self
        # visit left -> node -> right
        def preOrder(root):
            if root:
                if root.left:
                    preOrder(root.left)

                if root.right:
                    preOrder(root.right)

                elem.append(root.data)

        preOrder(root)


    def search(self, target):
        # case 1: the root is the target
        if self.data == target:
            return True

        # case 2: if the root is less then the target, might be in the right subtree
        if self.data < target:
            if self.right:
                return self.right.search(target)
            else:
                return False

        # case 3: if the root is more then the target, might be in the left subtree
        if self.data > target:
            if self.left:
                return self.left.search(target)
            else:
                return False

    def find_min(self):
        # left is lower than root so it will be min
        if self.left:
            return self.left.find_min()
        else:
            # base case
            return self.data

    def find_max(self):
        # right is higher than root so it will be min
        if self.right:
            return self.right.find_max()
        else:
            # base case
            return self.data

    def calculate_sum(self, sum=0):
        # x is a virtual aid
        # let use post-order transversal (left -> right -> root)
        if self.left:
            # x = self.data
            sum += self.left.calculate_sum()

        if self.right:
            # x = self.data
            sum += self.right.calculate_sum()

        # x = self.data
        sum += self.data
        return sum

    ''' review this again '''
    def delete(self, val):
        # search on the left
        if self.left and val < self.data:
            self.left = self.left.delete(val)

        # search on the right
        elif self.right and val > self.data:
            self.right = self.right.delete(val)

        # found
        else:
            # case 1: the target has no child
            if self.left is None and self.right is None:
                return None

            # case 2: the target has 1 child
            if self.left is None:
                self = self.right
                return self
            if self.right is None:
                return self.left

            # case 3: the target has 2 children
            # (successor)
            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)

            # (predecessor)
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self


def build_tree(numbers):
    # create a root
    root = BSTNode(numbers[0])

    # find a place to insert: left,/right/left etc
    for i in range(1, len(numbers)):
        root.add_child(numbers[i])

    return root


if __name__ == "__main__":
    # root = build_tree([1, 4, 9, 17, 18, 23, 34])
    # root.add_child(21)
    # root = root.delete(1)
    # root = root.delete(4)
    # root = root.delete(17)
    # root = root.delete(9)
    # root = root.delete(18)
    # root.add_child(32)
    root = build_tree([15])
    root.add_child(10)
    root.add_child(14)
    root.add_child(20)
    print("After deleting 20 ", root.inOrder_traversal_M2())  # this should print [1, 4, 9, 17, 18, 23, 34]
    print("After deleting 20 ", root.in_order_traversal())  # this should print [1, 4, 9, 17, 18, 23, 34]
    print(root.search(34))
    print(root.find_min())
    print(root.find_max())
    print(root.calculate_sum())  # 167