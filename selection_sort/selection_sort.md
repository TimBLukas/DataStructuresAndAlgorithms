# Selection Sort

Selection sort is a rather slow algorithm, that can be used to sort a list.


## Procedure
In order to sort a list using selection sort, you go through the list and pick the biggest (or smallest) item and add it to a new list.
You repeat that as long as there are items in the old list. After going through every item in the list you have a sorted list.

## Time Complexity
Because for every item of the list you have to go through the entire list once, it will take O(n) for each item, since there are n items in the list the time complexity for the entire algorithm is O(n * n) or O(n**2).
This is a rather slow algorithm and therefor isn't used much.


## Implementation
```python
def findSmallest(arr: List) -> int:
    smallest = arr[0]
    smallest_index = 0
    for index, item in enumerate(arr):
        if item < smallest:
            smallest = item
            smallest_index = index

    return smallest_index 
```

This function can then be used to implement selection sort

```python
def selection_sort(arr: List) -> List:
    newArr = []
    copiedArr = list(arr)
    for i in range(len(copiedArr))
        smallest = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr
```

