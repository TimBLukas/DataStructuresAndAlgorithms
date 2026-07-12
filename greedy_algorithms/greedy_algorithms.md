# Greedy algorithms

## The classroom scheduling problem

> Suppose you have a classroom and want to hold as many classes here as possible. You get a list of classes, but can't hold all of them in the classroom
> because some of them overleap.
> You want to hold as many classes as possible. How do you pick what set of classes to hold so that you get the biggest set of classes possible?

The Algorithms for this is as follows
```
1. Pick the class that ends the soonest. This is the first class that will be held in the classroom
2. Now you have to pick a class that starts after the first class. Again you pic kthe class that ends the soonest. This is the second class that will be held.

You keep doing this until no class can be picked and you'll end up with the answer.
```

A greedy algorithms is simple: at each step, pick the optimal move. In case of the classroom problem you pick the one that ends the soonest.
At each step, you pick the locally optimal solution, and in the end, you'releft with the globally optimal solution to this scheduling problem.

> NOTE: The greedy algorithm is not going to work always, but they're simple to implement.

## Approcimation algorithms

Suppose you're starting a radio show and wantt to reach listeners in all 50 US states. You have to decide what stations to play on to reach all those listeners.
THe problem with this is that it takes a long time to calculate every possible subset of stations. It takes O(2**n) time because there are 2**n subsets.
It is possible to calculate this if you have small set of 5-10 stations. But if the number of stations increases it gets increasingly more unefficient to calculate all options.

You can however use a greedy algorithm to solve this problem and come quite close to the optimal solution:

```
1. Pick the station that covers the most states that haven't been covered yet. It's ok if the station covers some states that have been covered already
2. Repeat until all the states are covered
```

This is called and approcimation algorithm. When calculating the exact solution will take too much time, an approcimation algorithm will work. Approximation algorithms are
judged by:
- how fast they are
- how close they come to the optimal solution

Greedy algorithms are a good choice because not only are they simple to come up with, but that simplicity means they usually run fast, too.
In this case, the greedy algorithm runs in O(n**2) time, where n is the number of radio stations.
If we implement this problem in code it would look like this:
```python
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
stations = {
        "kone": set(["id", "nv", "ut"])
        "ktwo": set(["wa", "id", "mt"])
        "kthree": set(["or", "nv", "ca"])
        "kfour": set(["nv", "ut"])
        "kfive": set(["ca", "az"])
}

final_stations = set()

while states_needed:
        best_station = None
        states_covered = set()

        for station, states_for_station in stations.items():
                covered = states_needed & states_for_station
                # The line above is called a set intersection
                # there are set unions ( set1 | set2), set intersections (set1 & set2) and seet differences (set1 - set2), covered is a set of states that were in bot states_needed andstates_for_station
                if len(covered) > len(states_covered):
                        best_station = station
                        states_covered = covered
        states_needed -= states_covered
        final_stations.add(best_station)


print(final_stations)
```

The greedy algorithm won't always give you the correct answer but it runs much faster. The set-covering problem is known as an NP-hard problem.