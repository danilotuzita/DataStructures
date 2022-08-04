from LinkedList import LinkedList

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
print('ll[-1] =', ll[-1])

print("\nDeleting from Linked List")
ll.print()
ll.delete()
ll.print()
ll.delete(0)
ll.print()
ll.delete(5)
ll.print()
# ll.delete(11); ll.print() # index out of bounds

ll.reverse()
ll.print()

ll.reverse()
ll.print()

ll.clear()
ll.print()
