from dataclasses import dataclass
from typing import Any


BUCKETS: int = 64

@dataclass
class Node:
    val: tuple[Any, Any]
    next

class HashTable:
    table = [(None, None) for i in range(BUCKETS)]

    def __init__(self):
        pass

    def _hash(self, s: str) -> int:
        return (len(s)) % BUCKETS

    def _get_index(self, s):
        if isinstance(s, str):
            return self._hash(s)
        return self._hash(str(s))

    def _extend_linked_list(self, head: Node, key, val):
        curr = head
        while curr.next is not None:
            curr = curr.next

        curr.next = Node((key, val), None)

    def add(self, key, value):
        idx = self._get_index(key)
        if self.table[idx] == None:
            self.table[idx] = (key, value)
        else:
            if isinstance(self.table[idx], Node):
                self._extend_linked_list(head, key, value)
            else:
                self.table[idx] = Node((self.table[idx][0], self.table[idx][1]), None)

    def get(self, key):
        idx = self._get_index(key)
        val = self.table[idx]

        if not isinstance(val, Node):
            return val

        else:
            pass

    def iter(self):
        pass


def main():
    hash_table = HashTable()

    hash_table.add("First", 1)
    hash_table.add("Second", 2)
    hash_table.add("Third", 3)




if __name__ == "__main__":
    main()
