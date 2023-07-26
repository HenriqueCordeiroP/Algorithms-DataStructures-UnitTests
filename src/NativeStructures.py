class Node_LinkedList:
    def __init__(self, value: int):
        self.head = None
        self.value = value
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_node(self, new: Node_LinkedList):
        if self.head is None:
            self.head = new
            self.tail = new
        else:            
            self.tail.next = new
            self.tail = new
    
    def remove_node(self, removed_value: int):
        if removed_value == self.head.value:
            self.head = self.head.next
        else:
            aux = self.head
            while aux.next is not None:
                if aux.next.value == removed_value:
                    aux.next = aux.next.next
                    break
                aux = aux.next

    def get_list(self):
        aux = self.head
        out = ""
        while aux is not None:
            out += f"{aux.value} -> "
            aux = aux.next
        out += "None"
        return out

    def print_nodes(self):
        aux = self.head
        while aux is not None:
            print(f"{aux.value} -> ", end="")
            aux = aux.next
        print("None")
'''
print("-----LinkedList-----")
ll = LinkedList()
ll.add_node(Node_LinkedList(1))
ll.print_nodes()
ll.add_node(Node_LinkedList(2))
ll.add_node(Node_LinkedList(2))
ll.add_node(Node_LinkedList(3))
ll.add_node(Node_LinkedList(4))
ll.print_nodes()
ll.remove_node(2)
ll.print_nodes()
ll.add_node(Node_LinkedList(2))
ll.print_nodes()
ll.remove_node(1)
# ll.remove_node(5)
ll.print_nodes()
'''

class Node_DoublyLinked:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinked:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_node(self, new):
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
            self.tail.next = None
            
    def remove_node(self, removed_value):
        if self.head is not None:
            if removed_value == self.head.value:
               self.head = self.head.next
            #    if self.head is not None:
            #     self.head.prev = None
            else:
                aux = self.head
                while aux.next is not None and aux.next.value != removed_value:
                    aux = aux.next 
                if aux.next.next is not None:    
                    aux.next = aux.next.next
                    aux.next.prev = aux
                else:
                    if aux.next.value == removed_value:
                        aux.next = None
    def get_list_in_order(self):
        aux = self.head
        out = ""
        while aux is not None:
            out += f"{aux.value} <-> "
            aux = aux.next
        out += "None"
        return out

    def get_list_in_reverse(self):
        aux = self.tail
        out = "None"
        while aux is not None:
            out += f" <-> {aux.value}"
            aux = aux.prev
        return out

    def print_nodes_in_order(self):
        aux = self.head
        while aux is not None:
            print(f"{aux.value} <-> ", end="")
            aux = aux.next
        print("None")

    def print_nodes_in_reverse(self):
        aux = self.tail
        while aux is not None:
            print(f"{aux.value} <-> ", end="")
            aux = aux.prev
        print("None")

'''      
print("-----DoublyLinkedList-----")
dll = DoublyLinked()
dll.add_node(Node_DoublyLinked(1))
dll.print_nodes_in_order()
dll.add_node(Node_DoublyLinked(2))
dll.add_node(Node_DoublyLinked(3))
dll.add_node(Node_DoublyLinked(4))
dll.print_nodes_in_order() 
dll.print_nodes_in_reverse()
dll.remove_node(2)
dll.print_nodes_in_order()
dll.remove_node(1)
dll.remove_node(3)
dll.remove_node(5)
dll.remove_node(4)
dll.remove_node(5)
dll.print_nodes_in_order()
'''

class Node_BinaryTree:
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
            self._insert_recursive(self.root, new)

    def _insert_recursive(self, node, new):
        if new.value <= node.value:
            if node.left:
                self._insert_recursive(node.left, new)
            else:
                node.left = new
        else:
            if node.right:
                self._insert_recursive(node.right, new)
            else:
                node.right = new

    def print_nodes_in_order(self, node):
        if node:
            self.print_nodes_in_order(node.left)
            print(node.value, end=" - ")
            self.print_nodes_in_order(node.right)
    
    def print_nodes_pre_order(self, node):
        if node:
            print(node.value, end=" - ")
            self.print_nodes_pre_order(node.left)
            self.print_nodes_pre_order(node.right)
    
    def print_nodes_post_order(self, node):
        if node:
            self.print_nodes_post_order(node.left)
            self.print_nodes_post_order(node.right)
            print(node.value, end=" - ")
bt = BinaryTree()
root = Node_BinaryTree(5)
bt.add_node(root)
bt.add_node(Node_BinaryTree(2))
bt.add_node(Node_BinaryTree(7))
bt.add_node(Node_BinaryTree(1))
bt.add_node(Node_BinaryTree(6))
bt.add_node(Node_BinaryTree(3))
bt.add_node(Node_BinaryTree(8))
# root.left = Node_BinaryTree(2)
# root.right = Node_BinaryTree(3)
# root.left.left = Node_BinaryTree(4)
# root.left.right = Node_BinaryTree(5)
bt.print_nodes_pre_order(root)
print()
bt.print_nodes_in_order(root)
print()
bt.print_nodes_post_order(root)