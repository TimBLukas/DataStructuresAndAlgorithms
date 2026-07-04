# Quicksort

> Quicksort is a specific algorithm implementing the divide and conquer technique, which is a well known recursive technique for solving problems.

## Divide and conquer

D&C works the following way:
1. Figure out a simple case as the base case
2. Figure out how to reduce your problem to get to the base case.

**Example:**
You're given an array of numbers. You have to add up all the numbers and return the total. It's pretty easy to do this with a loop:
```python
def sum(arr):
  total = 0
  for x in arr:
    total += x 
  return total
```

To solve the same problem in a recursive function you can apply D&C 
1. Figure out the base case: What's the siplest array you could get? If you get an array with 0 or 1 element, that's pretty easy to sum up.
2. You need to move closer to an empty array with every recursive call. How do you reduce your problem size?
```
sum([2,4,6]) = 2 + sum([4,6])
```

The entire sum function would look like this:
```python
def sum(arr: list[int]):
  if len(arr) == 1:
    return arr[0]
  else:
    return arr[0] + sum(arr[1:])
```


## Quicksort

Quicksort is an sorting algorithm that is much faster than selection sort and frequently used. Quicksort also uses D&C.

The base case for quicksort are empty arrays or arrays with just one element. These arrays can just be returned, as there is nothing to sort.

```python
def quicksort(arr: list[int]) -> list[int]:
  if len(arr) < 2:
    return arr
```

If the array is longer than one or two elements we can apply divide and conquer:
you select one element as your pivot element (e.g. the first element of the array).
Next you will need to find the elements smaller than the pivot and the elements larger than the pivot element.

> This process is called partitioning.

After that step you will have:
- A sub-array of all the numbers less than the pivot
- The pivot
- A sub-array of all the numbers greater than the pivot

The two sub-arrays aren't sorted. They're just partitioned. But if they were sorted, then sorting the whole arry would be pretty easy:
`[sub-array less] + pivot + [sub-array greater]`

To sort the sub-arrays you can just recursivly call the quicksort function on them.

The code for quicksort looks like this:
```python
def quicksort(arr: list[int]) -> list[int]:
  if len(arr) < 2:
    return arr

  else:
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)
```

