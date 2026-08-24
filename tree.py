class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if key < current_node.val:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)

    def print_in_order(self, node):
        if node:
            self.print_in_order(node.left)
            print(node.val, end=" ")
            self.print_in_order(node.right)

    def print_pre_order(self, node):
            if node:
                print(node.val, end=" ")
                self.print_pre_order(node.left)
                self.print_pre_order(node.right)

    def print_post_order(self, node):
            if node:
                self.print_post_order(node.left)
                self.print_post_order(node.right)
                print(node.val, end=" ")

if __name__ == "__main__":
    tree = BinarySearchTree()
    elements_to_insert = [50, 30,10,25,35,64, 70, 20, 40, 60, 80]

    for item in elements_to_insert:
        tree.insert(item)

    print("--- Tree Traversal Outputs ---")

    print("\n1. In-Order Traversal (Sorted Order):")
    tree.print_in_order(tree.root)

    print("\n2. Pre-Order Traversal:")
    tree.print_pre_order(tree.root)

    print("\n3. Post-Order Traversal:")
    tree.print_post_order(tree.root)

    