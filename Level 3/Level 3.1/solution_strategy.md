# Solution Strategy
### A high level overview of the strategy/concepts used within my solution.

### Utilized Concepts:
* Dynamic Programming (Memoization)
* Distinct Partitions Problem

The function takes an integer n as input, this integer represents the amount of bricks we have available to assemble the staircase. We must return the total amount of different possible staircases that can be assembled using these bricks, where each step is larger than the last.

To ensure that my program ran efficiently, I employed dynamic programming to remember the results of previous calculations, which prevents unnecessary calculations from being repeated and the recursion from going too deep. The solution to this program is essentially the solution to the distant partitions problem, an explanation of how to solve that problem can be found here: https://mathworld.wolfram.com/PartitionFunctionQ.html
