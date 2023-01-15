# Binary Class
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Create data for binary tree
    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    # In Order Traversal
    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    # Post Order Traversal
    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    # Pre Order Traversal
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    # Search Option
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # val might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            # val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False
    # Find Max
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    # Find Min
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    # Delete Function
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

# Build Binary Tree
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

# Binary Tree Creation
if __name__ == '__main__':
    full_name = ["C", "A", "R", "W", "Y", "N", "K", "U", "R", "T", "S", "A", "R", "I", "M", "A", "D", "O"]
    full_name_tree = build_tree(full_name)

    print("Does C appear in the binary tree? ", full_name_tree.search("C"))
    print(full_name_tree.in_order_traversal())
    print(full_name_tree.post_order_traversal())
    print(full_name_tree.pre_order_traversal())
    print(full_name_tree.find_max())
    print(full_name_tree.find_min())

    full_name_tree.delete("W")
    print("After deleting W ", full_name_tree.in_order_traversal())

    full_name = ["C", "A", "R", "W", "Y", "N", "K", "U", "R", "T", "S", "A", "R", "I", "M", "A", "D", "O"]
    full_name_tree.delete("C")
    print("After deleting C ", full_name_tree.in_order_traversal())

    full_name = ["C", "A", "R", "W", "Y", "N", "K", "U", "R", "T", "S", "A", "R", "I", "M", "A", "D", "O"]
    full_name_tree.delete("R")
    print("After deleting R ", full_name_tree.in_order_traversal())

