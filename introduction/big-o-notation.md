# Big O Notation

> Big O notations is special notation that tells you how fast an algorithm is.

Different algorithms differ in the rate they grow at!
Big O notation tells you how fast an algorithm is.
For example: Suppose you have a list of size n. Simple search needs to check each element, so it will take n operations.
The run time in big O notation is $$ O(n) $$. Big O notations doesn't tell you the speed in seconds, big O notation lets you compare
the number of operations. It tells you how fast the algorithm grows.

## Different big O run times

> Note that big O establishes a worst-case run time: If you look through a phone book using simple search and your target is the first
> name in the book, the big O notation of that algorithm is not $$ O(1) $$ but instead it's still $$ O(n) $$.
> Big O is used for wort-case scenario analysis, this means that if you see the big O notation of simple search, you can be sure it will never be more than $$ O(n) $$.

**Common big O run times:**

- $$ O(log n) $$, also known as log time. Example: binary search
- $$ O(n) $$, also known as linear time. Example: simple search
- $$ O(n\*log n) $$. Example: a fast sorting algorithm like quicksort.
- $$ O(n\*\*2) $$ Example: a slow sorting algorithm, like selection sort.
- $$ O(n!) $$ Example: a really slow algorithm, like the traveling salesman.

## Main Takeaways

- Algorithm speed isn't measured in seconds but in growth of the number of operations
- Instead of seconds, we talk about how quickly the run time of an algorithm increases as the size of the input increases.
- Run time of algorithms is expressed in big O notation
- $$ O(log n) is faster than $$ O(n) $$, and it gets a lot faster, as the list of items you're searching grows.

## Exercises

Give the run time for each of these scenarios in terms of big O.

1. You have a name, and you want to find the person's phone number in the phone book.

   > Using binary search the run time is $$ O(log n) $$

2. You have a phone number, and you want to find the person's name in the phone book.

   > You will have to search through the entire book, meaning the run time will be $$ O(n) $$

3. You want to read the numbers of every person in the phone book

   > ?

4. You want to read the numbers of just the As.
   > Since you have to read through every number of n persons (whose name start with A) the runtime is $$ O(n) $$
