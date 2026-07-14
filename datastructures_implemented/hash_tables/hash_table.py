from dataclasses import dataclass
from typing import Any


BUCKETS: int = 64


@dataclass
class Node:
    val: tuple[Any, Any]
    next: "Node | None" = None

class HashTable:
    def __init__(self):
        self.table = [None for _ in range(BUCKETS)]

    def _hash(self, s: str) -> int:
        return len(s) % BUCKETS

    def _get_index(self, s):
        if isinstance(s, str):
            return self._hash(s)
        return self._hash(str(s))

    def _extend_linked_list(self, head: Node, key, val):
        curr = head

        while curr.next is not None:
            curr = curr.next

        curr.next = Node((key, val))

    def add(self, key, value):
        idx = self._get_index(key)

        if self.table[idx] is None:
            self.table[idx] = Node((key, value))
        else:
            if isinstance(self.table[idx], Node):
                self._extend_linked_list(self.table[idx], key, value)

    def get(self, key):
        idx = self._get_index(key)
        curr = self.table[idx]

        while curr is not None:
            if curr.val[0] == key:
                return curr.val[1]
            curr = curr.next

        return None

    def iter(self):
        for bucket in self.table:
            curr = bucket

            while curr is not None:
                yield curr.val
                curr = curr.next


def main():
    hash_table = HashTable()

    hash_table.add("First", 1)
    hash_table.add("Second", 2)
    hash_table.add("Third", 3)

    print(hash_table.get("First"))
    print(hash_table.get("Third"))


if __name__ == "__main__":
    main()