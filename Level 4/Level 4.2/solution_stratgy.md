# Solution Strategy
### A high level overview of the strategy/concepts used within my solution.

### Utilized Concepts:
* Graph Theory (Maximum Flow)
* Object Oriented Programming (OOP)
* Breadth First Search (BFS)

The solution to this problem requires you to caclulate the maximum flow of a graph. There are many algorithms that can be used to do this, I used the Ford-Fulkerson algorithm.  

I created classes to represent a Directed Weighted Graph in my solution, and also created its adjancency matrix. For the sake of simplicity, I created main input and exit nodes for when there were multiple exits and entrances and set their edges to have a flow of 10,000 so they would not be bottle necks.

The algorithm mainly operates by exploring all valid (ensure the exit can be reached and the flow capacity of any edge is not exceeded) augmenting paths and summing the flows through all of them.