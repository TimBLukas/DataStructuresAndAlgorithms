"""
Linked List:
A singly linked list is a fundamental data structure,
it consists of nodes where each node contains a data field and a
reference to the next node in the linked list. The next of the last node is null,
indicating the end of the list. Linked Lists support efficient insertion and deletion operations.

https://www.geeksforgeeks.org/dsa/singly-linked-list-tutorial/

Operations:
- Traversal:
- Insertion
- Deletion
-  Searching
- Updating
- Reverseal
"""


class Node:
    """
    A single Node that is part of the linked list
    has the fields val and next
    """
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, val=None):
        self.val = val
        self.next = None


    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self._len = 0

        if iterable:
            for x in iterable:
                self.append(x)


    def __repr__(self):
        return f"LinkedList({list(self)})"


    def __str__(self):
        return " -> ".join(map(str, self))


    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.val
            curr = curr.next


    def __len__(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count


    def append(self, val):
        if not self.head:
            self.head = Node(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)


    def get(self, idx):
        curr = self.head
        for _ in range(idx):
            if not curr:
                raise IndexError
            curr = curr.next
        if not curr:
            raise IndexError
        return curr.val


    def remove(self, idx):
        if idx == 0:
            if not self.head:
                raise IndexError
            self.head = self.head.next
            return

        prev = self.head
        for _ in range(idx - 1):
            if not prev or not prev.next:
                raise IndexError
            prev = prev.next

        if not prev.next:
            raise IndexError
        prev.next = prev.next.next


    def pop(self):
        if not self.head:
            raise IndexError

        if not self.head.next:
            val = self.head.val
            self.head = None
            return val

        prev = self.head
        curr = self.head.next
        while curr.next:
            prev = curr
            curr = curr.next

        prev.next = None
        return curr.val


    def find(self, val):
        curr = self.head
        i = 0
        while curr:
            if curr.val == val:
                return i
            curr = curr.next
            i += 1
        return -1


    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev



    def copy(self):
        return LinkedList(self)



class DoublyLinkedList:
    def __init__(self):
        pass


def print_list(list: LinkedList):
    print("List: ")
    for val in list:
        print(val)

def main():
    ll = LinkedList(1)

    ll.append(2)
    ll.append(3)
    ll.append(4)

    ll.append(5)
    ll.append(6)
    ll.append(7)

    print_list(ll)
    print(ll.get(2))
    print(len(ll))

    ll.reverse()
    print_list(ll)






if __name__ == "__main__":
    main()
