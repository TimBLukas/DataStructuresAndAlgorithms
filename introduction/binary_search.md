# Binary Search

> Suppose you're searching for a person in the phone book. Their name starts with K. You could start at the beginning and keep flipping pages until you get to the Ks. But you're more likely to start at a page in the middle because you know the Ks are going to be near the middle of the phone book.
>
> Or suppose you're searching for a word in a dictionary, and it starts with O. Again, you'll start near the middle.
>
> Now suppose you log on to Facebook. When you do, Facebook has to verify that you have an account on the site. So it needs to search for your username in its database. Suppose your username is karlmaggedon. Facebook could start from the As and search for your name - but it makes more sense for it to begin somewhere in the middle.

This is a search problem. And all theses cases use the same algorithm to solve the problem: **binary search**.



## Explaination

Binary search is an algorithm; its input is a sorted list of elements. If an element your looking for is in that list, binary search returns the position where it's located. Otherwise binary search returns null.

In general: binary search will take 
$$
log_2(n) \text{ steps to run in the worst case whereas a simple search will take n steps.}
$$

> Note: binary search only works if the list is in sorted order. For example the names in a phone book are sorted in alphabetical order, so you can use binary search to look for a name.



## Code

The binary search function takes a sorted array and an item as inputs. If the item is in the array, the function returns its position. You'll keep track of what part of the array you have to search through. At the beginning it's the entire array.

```python
low = 0
high = len(arr) - 1
```

Each time you check the middle element

```python
mid = (low + high) // 2 # Mid is rounded down by python automatically
guess = arr(mid)
```

If the guess is to low, you update low accordingly:

```python
if guess < item:
    low = mid + 1
```

And if the guess is too high, you update high.



Full Code:

```python
def binary_search(arr: List, item):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
            
    return None
```





# Exercises

1. Suppose you have a sorted list of 128 names, and you're searching through it using binary search. What's the maximum number of steps it would take?

   > It would take 7 steps (2**7 = 128)

2. Suppose you double the size of the list. What's the maximum number of steps now?

   > It would now take 8 steps (2**8 = 256)

