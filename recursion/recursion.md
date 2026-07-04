# RECURSION

> Suppose you are looking through your grandma's attic and come across a mysterious locked suitcase.
> Your grandma tells you the key is probably in this other box, this box contains more boxes with boxes inside those boxes.
> What Algorithm could be used to search  through these boxes?

One approach to solve the problem described above is something like this:

```

Make a pile of boxes to look through
while (pile is not empty):
  grab a box
  if new box:
    add new box to the pile
    continue
  if key:
    break (you are done)
```
```

An alternative approach would be:
```
```
for item in box:
  if new box:
    start from top with the new box

  if key:
    break
```

```
Every time you make a function call, the computer saves the values for all variables for that call in memory.
To store these things in memory the computer uses a stack, each newly added value is stored on top of the old one, when you return from the function call the values from the stack are popped.

**Example**: Factorial
```python
def factorial(n):
  if n == 1:  
    return 1 
  else:
    return n * factorial (n - 1)
```
```
```

With recursion you need to keep in mind that everything is stored on the stack, but depending on how much you have to store on the stack you need to keep in mind that it can take up a lot of memory to do so.
If you get to the point were your stack contains to much memory, you have two options:
1. You can rewrite to use a loop instead
2. You can use tail recursion, which is an advanced recursion topic that may not be supported by all languages.

Summary:
- Recursion is when a function calls itself.
- Every recursive function has two cases:
  1. the base case 
  2. the recursive case
- A stack has two operations push and pop 
- All function calls go to the stack
- The call stack can get very large which takes up a lot of memory
