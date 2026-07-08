# Breadth First Search

> Breadth First Search is a graph based algorithm that allows you to find the shortest distance between two things.

The shortest distance can mean many things:
- Write a spell checker (fewest edits from the misspelled word to a real word)
- Find a doctor closest to you in your network.
- Build a search engine crawler.

## Graphs

> A graph models a set of connections and is made up of nodes and edges.

A node can be directly connected to many other nodes. Those nodes are called in-neighbors or out-neighbors.
if you have a graph like this: `A <- B <- C`
B is an in-neighbor of A and a out-neighbor of C.

Graphs are a way to model how different things are connected to one another.

## Breadth First Search

Breadth first search is a search algorithm that runs on graphs, it can help answer two types of questions:
1. Is there a path from node A to node B?
2. What is the shortest path from node A to node B

### Finding the shortest path

You would always prefer a first-degree connection over a second-degree connection when you are trying to find the shortest path, a second-degree to a third-degree and so on.

The way breadth-first search works is that the search radiates out from the starting point. It first checks first-degree connections, than second-degree connections and so on.
You could also see this like this:
First-degree connections are added to the list before second-degree connections.
You can just go down the list and and check for the condition. The first-degree connections will be searched before the second-degree connections.

#### Queue

> A Queue works exactly like it does in real life. Queues are similar to stacks, you can't access random elements in the queue. Instead, there are only two operations: enqueue and dequeue.

If you enqueue two items to the list, the first item you added will be dequeued before the second item. Xou can use this for the search list, since it requires the items to be processed in the same order they were added.
The queue is called a FIFO datastructure: first in, first out. In contrast a stack is a LIFO datastructure: last in, first out.

### Implementing the graph

A graph consists of several nodes. Each node can be connnected to other nodes.
The datastructure used to express the relationsships is a hash table.

A graph in python can look like this:
```python
graph = {}
graph["you"] = ["alice", "bob","claire"]
```

graph["you"] will give you an array of all the out-neighbors of "you".

If edges in a graph have a direction the graph is called directed graph: The relationship is one way. An undirected graph doesn't have any arrows.

If you are dealing with an undirected graph there is no difference between in-neighbor and out-neighbor, you can just call them neighbors.

### Implementing the algorithm

Start by creating a queue
```python
from collections import deque
search_queue = deque()
search_queue += graph["you"]
```

This will add all neighbors of "you" to the queue.
To finish the rest:
```python
while search_queue:
  person = search_queue.popleft()
  if person_is_seller(person):
    print(f"{person] is a mango seller!")
    return True
  else:
    search_queue += graph[person]
  return False
```

The is seller function is implemented like this:
```python
def person_is_seller(name):
  return name[-1] == "m"
```

(This is not a real function it is just for demonstration purposes)

Before checking a node it is important to make sure it hasn't been checked before.

Here is the final code:
```python
def search(name):
  search_queue = deque()
  search_queue += graph[name]
  searched = set()

  while search_queue:
    person = search_queue.popleft()
    if not person in searched:
      if person_is_seller(person):
        print(f"{person} is a mango seller")
        return True
      else:
        searched_queue += graph[person]
        searched.add(person)
  return False
```

The runtime of this is often written as O(V+E) (Vertices + Edges).

