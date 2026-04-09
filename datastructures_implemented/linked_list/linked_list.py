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

        self.tmp = self.head 

    def __iter__(self):
        return self

    def __next__(self):
        if self.tmp.next is not None:
            self.tmp = self.tmp.next
            return self.tmp.data

        self.tmp = self.head
        raise StopIteration

    def __len___(self):
        return self.len()

    def append(self, data):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(data)


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

        
    def find(self, data):
        start = self.head
        i = 0
        while curr is not None:
            if curr.data == data:
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

        return curr.data


    def update(self, idx, data):
        curr = self.head
        for i in range(idx):
            if curr.next == None:
                return ValueError("End of list reached")
            curr = curr.next

        curr.data = data

    def reverse(self):
        curr = self.head
        prev = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    def len(self) -> int:
        l = 0
        curr = self.head
        while curr is not None:
            curr = curr.next
            l += 1
        return l - 1


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


    ll.update(2, 20)

    ll.append(5)
    ll.append(6)
    ll.append(7)

    print_list(ll)
    print(ll.get(2))
    print(ll.len())

    ll.reverse()
    print_list(ll)






if __name__ == "__main__":
    main()
