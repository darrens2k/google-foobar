# Solution Strategy
### A high level overview of the strategy/concepts used within my solution.

### Utilized Concepts:
* Object Oriented Programming (OOP)
* Recursion
* Post Order Tree Traversal
* Properties of Perfect Binary Trees

The function solution accepts an integer h (representing the height of a perfect binary tree) and a list of indices q. The function returns all of the nodes that sit above the nodes at the indices listed in q.  

Within my function I create a Node class that I use to create the perfect binary tree. Once I have created the tree I perform a post order traversal on the tree. If in the traversal I arrive at a node whose index is listed in the input list q, I save the index of its parent node to the output list.

