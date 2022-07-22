import sys

class Node:
    value = None
    next_node = None

    def __init__(self, value):
        self.value = value



class LinkedList:
    head: Node = None

    def insert(self, value, pos: int = -1):
        new_node: Node = Node(value)  # create the new node
        
        if self.head is None or pos == 0:  # if first node to be inserted
            new_node.next_node = self.head #    set the head to the new node's next_node
            self.head = new_node           #    set head as the new node
            return
   
        prev_node: Node = self._get_node_at(pos - 1)  # find the previous node
        next_node = prev_node.next_node               # saves the next node
        prev_node.next_node = new_node                # set the new node as the next_node of the previous node
        new_node.next_node = next_node                # set the next_node of the new node as the next_node
        
    
    def delete(self, pos: int = -1):
        if self.head is None:  # if the list is empty
            return             #    do nothing

        if pos == 0:                         # if wants to delete head
            old_head: Node = self.head       #     save the old head
            self.head = old_head.next_node   #     set the head as the old head's next_node
            del old_head                     #     delete the old head
            return

        if pos < 0:               # if wants to pop last item
            pos = self.size() - 1 #     set pos to the last-last item
        
        prev_node: Node = self._get_node_at(pos - 1)   # find the previous node
        node_to_delete: Node = prev_node.next_node     # save the node they want to delete
        if node_to_delete is None:                     # if prev_node is already tail of list: raise Exception
            raise IndexError(f"Index [{pos}] out of bounds. LinkedList size: {pos}")
        prev_node.next_node = node_to_delete.next_node # set the previous node's next_node to node to delete's next_node
        del node_to_delete                             # delete the node


    def _get_node_at(self, index: int) -> Node:  # O(n)
        if index < 0:               # if wants last node
            return self.get_tail()  #     return the tail

        if self.head is None:       # if the list is empty
            return None             #     return None
        
        curr_node: Node = self.head         # go to head
        for _ in range(index):              # for index
            curr_node = curr_node.next_node #     go to the next node
            if curr_node is None:           #     if next node is None: raise Exception
                raise IndexError(f"Index [{index + 1}] out of bounds. LinkedList size: {_ + 1}")

        return curr_node # return the node


    def get_tail(self) -> Node:  # O(n)
        if self.head is None:
            return None

        curr_node: Node = self.head
        while curr_node.next_node:
            curr_node = curr_node.next_node

        return curr_node


    def size(self):  # O(n)
        if self.head is None:
            return 0
        
        size = 1
        curr_node = self.head
        while curr_node.next_node:
            curr_node = curr_node.next_node
            size += 1
        return size


    def __getitem__(self, index: int):  # O(n)
        return self._get_node_at(index).value


    def print(self):  # O(n)
        curr_node: Node = self.head
        while curr_node:
            print(curr_node.value, end=', ')
            curr_node = curr_node.next_node
        print(f'[{self.size()}]')



ll = LinkedList()
print("Inserting in Linked List")
ll.print()
ll.insert(0, 0)
for i in range(1, 10):
    ll.insert(i)

ll.print()
ll.insert('middle', 5)
ll.print()
ll.insert('start', 0)
ll.print()
ll.insert('end', ll.size())
ll.print()

print("\nAcessing Linked List")
print('ll[5] =', ll[5])

print("\nDeleting from Linked List")
ll.print()
ll.delete()
ll.print()
ll.delete(0)
ll.print()
ll.delete(5)
ll.print()
ll.delete(11)
ll.print()
