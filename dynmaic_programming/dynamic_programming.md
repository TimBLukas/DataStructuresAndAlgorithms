# Dynamic programming

> A technique of solving problems by splitting them into subproblems and solving these subproblems

Dynamic programming starts by solving subproblems and builds up to solving the big problem.
Dynamic programming is quite hard since you have the find the correct subproblems for solving the problem.

Every dynamic programming algorithm starts with a grid.

> The knapsack problem:
> You are a thief with a knapsack that can carry 4 lb of goods. You have three items that you can put into the knapsack:
> A stereo (4 lbs, 3000$), a laptop (3 lbs, 2000$) and a guitar (1 lbs, 1500$).
> The problem is figuring out which items to steal the get the maximum value of goods.

For the knapsack problem the grid would look like this:
The rows of the grid are the items, the columns are knapsack wights from 1 lb to 4 lb.

| Item   | 1     | 2 | 3 | 4 |
|--------|-------|---|---|---|
| Guitar |  |   |   |   |
| Stereo |       |   |   |   |
| Laptop |       |   |   |   |

The grid starts out empty. You are going to fill in each cell of the grid Once the grid is filled in, you'll have the answer to the problem.

Start with the first row (Guitar), this means you are trying to fit the guitar into the knapsack. At each cell there's a simple decision: Steal the guitar or not.
The first cell has a knapsack of capacity 1 lb The guitar is also 1 lb, which menas it fits into the knapsack - The value of the cell is $1500 and it contains the guitar.

| Item   | 1     | 2 | 3 | 4 |
|--------|-------|---|---|---|
| Guitar | $1500 |   |   |   |
| Stereo |       |   |   |   |
| Laptop |       |   |   |   |

If you look at the next cell you can find that the guitar will fit in there as well (The same is true for the rest of the cells in this row).
Remember that you are in the first row so you only have guitar to choose from, you are pretending the other items aren't available to steal right now.

| Item   | 1     | 2 | 3 | 4 |
|--------|-------|---|---|---|
| Guitar | $1500 | $1500 | $1500 | $1500 |
| Stereo |       |   |   |   |
| Laptop |       |   |   |   |

In the stereo row, you can steal the stereo as well as the guitar. At every row, you can steal the item at that row or the items in the rows above it.
In the first cell you can only fit the guitar rmeaning the maximum value is 1500$.

| Item   | 1     | 2 | 3 | 4 |
|--------|-------|---|---|---|
| Guitar | $1500 | $1500 | $1500 | $1500 |
| Stereo | $1500 |   |   |   |
| Laptop |       |   |   |   |

The same thing is true for 2 lbs and 3 lbs (The stereo can't fit)

| Item   | 1     | 2 | 3 | 4 |
|--------|-------|---|---|---|
| Guitar | $1500 | $1500 | $1500 | $1500 |
| Stereo | $1500 | $1500 | $1500 |   |
| Laptop |       |   |   |   |

But if you look at the 4 lbs column, the stereo fits so you get a higher value.

| Item   | 1     | 2 | 3 | 4 |
|--------|-------|---|---|---|
| Guitar | $1500 | $1500 | $1500 | $1500 |
| Stereo | $1500 | $1500 | $1500 | $3000 |
| Laptop |       |   |   |   |

Your new estimate will therefor be $3000.

In the laptop row in the first two columns, neither the laptop nor the stereo will fit:

| Item   | 1     | 2 | 3 | 4 |
|--------|-------|---|---|---|
| Guitar | $1500 | $1500 | $1500 | $1500 |
| Stereo | $1500 | $1500 | $1500 | $3000 |
| Laptop | $1500 | $1500 |   |   |

In the 3 lbs column however the laptop does fit updating its estimate

| Item   | 1     | 2 | 3 | 4 |
|--------|-------|---|---|---|
| Guitar | $1500 | $1500 | $1500 | $1500 |
| Stereo | $1500 | $1500 | $1500 | $3000 |
| Laptop | $1500 | $1500 | $2000 |   |

In the 4lbs column things get interesting: the current estimate is $3000, you can put the laptop in the knapsack but it's only worth $2000, but you have 1lbs free. Since the table shows us the maximum value we can fit into 1 lbs of space ($1500) we can see the maximum value is $3500 updating the new maximum for 4 lbs of space.
The idea of keeping track of the smaller backpack sizes is what helped here: If you have remaining space, you can find the maximum value you can use that space for.
The final table looks like this:

| Item   | 1     | 2 | 3 | 4 |
|--------|-------|---|---|---|
| Guitar | $1500 | $1500 | $1500 | $1500 |
| Stereo | $1500 | $1500 | $1500 | $3000 |
| Laptop | $1500 | $1500 | $2000 | **$3500** |

The formula for calculating each cell is as follows:
```
cell[i][j] = max of 
        1. the previous max(value at cell[i-1][j])
        2. value of current item + calue of the remaining space (cell[i-1][j - items weigth])
```

This formula can be used with every cell in the grid.

> Note:
> With dynamic programming you either take the item or not. There's no way for to figure out that you could take half an item.
> Dynamic programming also only works if each subproblem is discrete - meaning the subproblems don't depend on other subproblems.

Take Aways dynamic programming:
- Dynamic programming is useful when you're trying to optimize something given a constraint.
- You can use dynamic programming when the problem can be broken into discrete subproblems and they don't depend on onanother.

Some general tips to follow are:
1. It's often useful to picture a dynamic programming problem as a grid.
2. The values in the cells are usually what you're trying to optimize.
3. Each cell is a subproblem, so think about how you can divide your problem into subproblems, this will help you figure out what the axes are.