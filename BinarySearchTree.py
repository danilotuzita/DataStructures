from random import randint

class Node:
    data = None
    left = None
    right = None
    debug = False

    def __init__(self, value, data_type):
        self.data = data_type(value)
        if self.debug: print(f"Creating Node: {self.data}")

    def count(self):
        return 1 if self.left else 0 + 1 if self.right else 0

    def is_leaf(self) -> bool:
        return self.count() == 0

    def clear_child(self, child):
        if child == self.left:
            self.left = None
        elif child == self.right:
            self.right = None

    def __del__(self):
        if self.debug:
            print(f"Deleting Node: {self.data}")


class BinarySearchTree:
    tree_type: type
    root: Node = None
    
    def __init__(self, tree_type: type):
        self.tree_type = tree_type

    def __new_node(self, value) -> Node:
        return Node(value, self.tree_type)

    def __print(self, node: Node):
        if node is None: return
        self.__print(node.left)
        print(node.data, end=', ')
        self.__print(node.right)

    def print(self):
        self.__print(self.root)
        print()

    def __draw_tree(self, node: Node, level: int = 0):
        if node is None: return
        self.__draw_tree(node.right, level + 1)
        print(' ' * 6 * level + ' -> ' + str(node.data))
        self.__draw_tree(node.left, level + 1)
    
    def draw_tree(self):
        self.__draw_tree(self.root)
        print()

    def __find(self, node: Node, value) -> Node:
        if node is None:       # not found
            return None
        if value == node.data: # found
            return node
        if value > node.data:  # go to right
            return self.__find(node.right, value)
        else:                  # go to left
            return self.__find(node.left, value)

    def find(self, value) -> Node:
        node = self.__find(self.root, value)
        return node.data if node else None

    def __min(self, node: Node):
        while node.left:
            node = node.left
        return node

    def __max(self, node: Node):
        while node.right:
            node = node.right
        return node

    def min(self):
        if self.root is None: return None
        return self.__min(self.root).data
        
    def max(self):
        if self.root is None: return None
        return self.__max(self.root).data

    def __height(self, node: Node) -> int:
        if node is None: return -1
        return 1 + max(
            self.__height(node.left),
            self.__height(node.right)
        )

    def height(self) -> int:
        return self.__height(self.root)

    def __is_bst(self, node: Node, min_value, max_value):
        if node is None:
            return True
        return (
            node.data >= min_value and
            node.data <= max_value and
            self.__is_bst(node.left, min_value, node.data) and
            self.__is_bst(node.right, node.data, max_value)
        )

    def is_bst(self):
        return self.__is_bst(self.root, -9999999, 9999999)

    def __remove(self, node: Node, value) -> Node:
        if node is None:
            return None  # Not found, do nothing
        
        if value < node.data:
            node.left = self.__remove(node.left, value) # update left tree
        elif value > node.data:
            node.right = self.__remove(node.right, value) # update right tree
        else:  # node found
            # NO CHILD
            if node.left is None and node.right is None:  # node has no child, return None
                return None
            # HAS RIGHT CHILD
            if node.left is None:  # node has only right child, return the right child
                return self.__balance(node.right)
            # HAS LEFT CHILD
            if node.right is None: # node has only left child, return the left child
                return self.__balance(node.left)
            # HAS BOTH CHILDREN
            node.data = self.__max(node.left).data  # find the max of left subrtree (could've been min of right subtree)
            node.left = self.__remove(node.left, node.data) # remove the max of left subtree
        
        return self.__balance(node)  # Returning the updated node

    def remove(self, value):
        self.root = self.__remove(self.root, value)        

    def __sucessor(self, node: Node, value) -> Node:
        if node is None: return None
        
        if value == node.data:  # Node found
            if node.right:  # If has right, get min from right subtree
                return self.__min(node.right)
            return node # If doesn't have right subtree, let previous node handle

        sucessor: Node = None  # Find the target node
        if value > node.data:
            sucessor = self.__sucessor(node.right, value)
        else:
            sucessor = self.__sucessor(node.left, value)

        if sucessor is None: return None

        if sucessor.data > node.data:  # If the sucessor found is still greater than it's parent
            return sucessor  # let previous node handle
        if sucessor.data > value:  # If the sucessor found is greater than the target value 
            return sucessor  # found the real sucessor
        return node  # keep returning the real sucessor

    def sucessor(self, value):
        node = self.__sucessor(self.root, value)
        return node.data if node else None

    def __predecessor(self, node: Node, value):
        if node is None: return None
        
        if value == node.data:  # Node found
            if node.left:  # If has left, get max from left subtree
                return self.__max(node.left)
            return node  # If doesn't have left subtree, let previous node handle
        
        predecessor: Node = None
        if value > node.data:  # Find the target node
            predecessor = self.__predecessor(node.right, value)
        else:
            predecessor = self.__predecessor(node.left, value)

        if predecessor.data < node.data:  # If the predecessor found is still lesser than it's parent
            return predecessor  # let previous node handle
        if predecessor.data < value: # If the precessor found is lesser than the target value
            return predecessor # found the real predecessor
        return node # keep returning the real predecessor

    def predecessor(self, value):
        node = self.__predecessor(self.root, value)
        return node.data if node else None

    def __balance_factor(self, node: Node) -> int:
        if node is None: return -1
        return self.__height(node.right) - self.__height(node.left)

    def __rotate_right(self, node: Node) -> Node:
        other_node: Node = node.left
        node.left = other_node.right
        other_node.right = node
        return other_node
    
    def __rotate_left(self, node: Node) -> Node:
        other_node: Node = node.right
        node.right = other_node.left
        other_node.left = node
        return other_node

    def __balance(self, node: Node) -> Node:
        bf = self.__balance_factor(node)
        if bf == -2:  # left heavy subtree
            bf2 = self.__balance_factor(node.left)
            if bf2 <= 0:  # left left heavy subtree
                # print(f"Node {node.data} is left left Heavy")
                return self.__rotate_right(node)
            else:         # left right heavy subtree
                # print(f"Node {node.data} is left right Heavy")
                node.left = self.__rotate_left(node.left)
                return self.__rotate_right(node)
        elif bf == 2:  # right heavy subtree
            bf2 = self.__balance_factor(node.right)
            if bf2 >= 0:  # right right heavy subtree
                # print(f"Node {node.data} is right right heavy")
                return self.__rotate_left(node)
            else:         # right left heavy
                # print(f"Node {node.data} is right left Heavy")
                node.right = self.__rotate_right(node.right)
                return self.__rotate_left(node)
        return node

    def __insert(self, node: Node, value) -> Node:
        if node is None:
            return self.__new_node(value)
        if value > node.data:
            node.right = self.__insert(node.right, value)
        else:
            node.left = self.__insert(node.left, value)
        return self.__balance(node)

    def insert(self, value):
        self.root = self.__insert(self.root, value)
    
    
    



bst = BinarySearchTree(int)

insert_values = [10]
insert_values.extend(i for i in range(10))
insert_values.extend(i for i in range(11, 21))
insert_values.extend(randint(-100, 100) for i in range(24))
for value in insert_values:
    bst.insert(value)
print(bst.is_bst())
bst.print()

for i in range(0, len(insert_values), 5):
    bst.remove(i)
bst.draw_tree()
print(bst.is_bst())
bst.print()

exit()
bst.insert(12)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(13)
bst.insert(14)
bst.insert(17)
bst.insert(1)
bst.insert(9)
bst.insert(19)

# bst.draw_tree()
bst.remove(15)
bst.draw_tree()
bst.balance_factor()


exit()

# print(bst.min(), bst.max())
bst.insert(4)
bst.insert(6)
bst.insert(13)
bst.insert(15)
bst.insert(14)
# bst.draw_tree()
print(bst.sucessor(1))


bst2 = BinarySearchTree(int)
bst2.insert(16)
bst2.insert(15)
bst2.insert(10)
bst2.insert(12)
bst2.insert(13)
bst2.draw_tree()
print(bst2.sucessor(13))

bst3 = BinarySearchTree(int)
bst3.insert(10)
bst3.insert(11)
bst3.insert(16)
bst3.insert(14)
bst3.insert(13)
bst3.draw_tree()
print(bst3.predecessor(13))
