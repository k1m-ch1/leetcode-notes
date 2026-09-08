So we're given a `coins` array which represents the types of coins we have.

We want to return the fewest number of coins needed to form that money.

So I think this is probably a greedy algorithm.

Essentially, what we do is, we can like for now, copy it to another array, and then I guess we'll sort it just in case.

We'll also store the amount using a temp variable.

Now we essentially turn it into a queue. Compare the last element of the queue with the temp variable. If it's smaller, then we can subtract it and continue. If it's bigger, take away from the queue. If the queue is empty, and our temp isn't zero, return -1. otherwise, it should return whatever we've calculated.

# Correction

I guess the greedy approach doesn't work all the time.

One way to do it is to create the whole tree... but i'm guessing that's unnecessary?

Could we perhaps use some sort of backtracking? I mean, that's the only way to find the minimum is to breath first search the whole tree right? 

First, check constraints:

```
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
```

So the coins array is small. I think we can use recursion + memoization with this.


