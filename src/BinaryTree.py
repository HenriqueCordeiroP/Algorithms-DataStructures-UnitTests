class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def add_node(self, new):
        if self.root is None:
            self.root = new
        else:
            self._add_node_recursion(self.root, new)

    def _add_node_recursion(self, node, new):
        if new.value <= node.value:
            if node.left:
                self._add_node_recursion(node.left, new)
            else:
                node.left = new
        else:
            if node.right:
                self._add_node_recursion(node.right, new)
            else:
                node.right = new

    # Left - Middle - Right
    def print_pre_order(self):
        self.pre_order_recursion(self.root)
    
    def pre_order_recursion(self, node):
        if node:
            self.pre_order_recursion(node.left)
            print(node.value, end = " ")
            self.pre_order_recursion(node.right)
bt = BinaryTree()
root = Node(5)
bt.add_node(root)
bt.add_node(Node(2))
bt.add_node(Node(7))
bt.add_node(Node(1))
bt.add_node(Node(6))
bt.add_node(Node(3))
bt.add_node(Node(8))

bt.print_pre_order()