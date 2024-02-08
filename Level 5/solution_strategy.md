# Solution Strategy
### A high level overview of the strategy/concepts used within my solution.

### Utilized Concepts:
* Beatty Sequence

This problem can be solved by computing the sum of the Beatty Sequence. Thankfully, recursion relations do exist for this, here is the recurrence relation that I followed: https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s

Another important thing to note here is the level of precision required. Notice that inputs can have up 101 digits, your code must be able to precisely operate with 101 digit numbers.
