# Depth First Search (DFS)
> A search algorithm for traversing a tree or graph data structure

Steps:
1. Pick a route
2. Keep going until you reach a dead end, or a previously visited node
3. Backtrack to the Last Node that has unvisited adjacent neighbors


Implementation for a Adjecency Matrix
```python
def dfs_helper(src: int, visited: list[bool]) -> None:
        if visited[src]:
                return 
        else:
                visited[src] = True

        for i in range(len(matrix[src])):
                if matrix[src][i] == 1:
                        dfs_helper(i, visited)
        return

def dfs(src: int) -> None:
        visited: list[bool] = []
        dfs_helper(src, visited)
        
```

