# Arrays and Lists

## Array
With an array all items in the array are stored directly next to each other in memory.
If you want to add a new item and there is no adjacent space available, all entries are moved to a new location in memory with enough space for all items to be stored next to eachother.

One possibility to avoid having to move is by "reserving" extra memory by adding a specific number of items when defining the array. This way the computer locates the array at a position in memory with enough space for the specified amount of items.
But if you have to store more items than you specified, all items have to be moved again.

> Also note that the space will not be used for anything else, so if you reserve space for 1000 items and only store 1. All the other space is wasted and can't be used for other things.

## Linked Lists
With Linked Lists, items can be stored anywhere in memory.
Each item stores the address of the next item in the list, which means that a bunch of random memory addresses are linked together.

This means that adding a new item is quite easy, you just add the memory address of the new item to the last item of the list. So you never have to move your items.

The deciding disadvantage is, that in order to access an item you first have to go through all the items in the list, to get the memory address, so accessing an item is slower.

## Comparison
- Arrays are great if you want to read random elements in the array, because you can directly access each item due to them being stored directly next to each other.
- With Linked Lists items are not stored directly next to each other so you can't instantly calculate there position, you first have to go through all the other elements.
- But Linked Lists make it easy to attach new list items.

### Run Time Comparisons
|     | Arrays | Lists |
| -------- | ------- | ------- |
| Reading | O(1)    | O(n)    |
| Writing | O(n)     | O(1)     |

> O(1): Constant time
> O(n): Linear time

### Inserting into the middle of a list

How does the approch change if you don't want to add a new item to the end of a list, but rather in the middle?

**Linked Lists**: With linked lists you just have to change the address the previous element points to.
**Arrays**: With arrays you have to shift all elements on position down, and if there's no space, you might have to copy everything to a new locatiton.

List are better if you want to insert elements in the middle of a list!

### Deletions

What if you want to delete an element?

Again lists are better, because you just need to update, what the previous element points to.
With arrays everything needs to be moved up, when an element is deleted.
Unlike insertions, deletinos will always work. Insertions can fail, when there's no space in memory, but you can always delete an element.


## Whis is used more arrays or linked lists?

Arrays are often used beacuse they have a lot of advantages over linked lists.

1. They are better at reads, because they provide random access.
> There are two types of access: random access and sequential. Sequential access means reading the elements one by one, starting with the first element. Linked lists can only do sequential access, because every node only knows the address of the node directly after it.
> Random access means you can jump directly to the element at a specific position.
2. Arrays are faster because they can use caching. A Computer reads the whole section at a time because that makes it a lot faster to go to the next item. This can only be done with arrays, because all items are stored next to each other.
3. Memory efficiency: Arrays only take up extra memory, if you "reserve" extra space for items which isn't used. Linked lists are using extra space per item because they need to store the address of the next item. So linked lists will take up more space if each item is pretty small (compared to arrays).
One exception is with big items, so every single slot of wasted space can be a big deal and the extra memory used by the pointers of the linked list is small in comparison.

In general arrays are used more often than linked lists except in specific use cases.


