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
  Searching
- Updating
- Reverseal
"""

# 1 - 2 - 3 - 5


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, head):
        if isinstance(head, Node):
            self.head = head
        else:
            self.head = Node(head)

        self.len = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.head = self.head.next
        
        if self.head.next is not None:
            self.head = self.head.next
            return self.head.val

        return StopIteration

    def __len___(self):
        return self.len()

    def append(self, val):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(val)


    def remove(self, idx):
        prev = self.head
        curr = self.head
        cnt = 0
        if idx:
            for _ in range(idx):
                if curr.next == None:
                    return ValueError("end of list reached")
                prev = curr 
                curr = curr.next 
            prev.next = curr.next
            return
        

    def pop(self):
        while curr is not None:
            prev = curr
            curr = curr.next

        prev.next == None
        return curr

        
    def find(self, val):
        start = self.head
        i = 0
        while curr is not None:
            if curr.val == val:
                return i
            prev = curr
            curr = curr.next
            i += 1


    def get(self, idx: int):
        curr = self.head
        for i in range(idx):
            if curr.next == None:
                return ValueError("End of list reached")
            curr = curr.next

        return curr.val


    def update(self, idx, val):
        curr = self.head
        for i in range(idx):
            if curr.next == None:
                return ValueError("End of list reached")
            curr = curr.next

        curr.val = val

    def reverse(self):
        curr = self.head
        prev = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def len(self) -> int:
        l = 0
        curr = self.head
        while curr is not None:
            curr = curr.next
            l += 1
        return l


class DoublyLinkedList:
    def __init__(self):
        pass


def print_list(list: LinkedList):
    for val in list:
        print(val)

def main():
    ll = LinkedList(1)

    ll.append(2)
    ll.append(3)
    ll.append(4)


    ll.update(2, 20)

    print_list(ll)






if __name__ == "__main__":
    main()
