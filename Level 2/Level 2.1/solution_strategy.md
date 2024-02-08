# Solution Strategy
### A high level overview of the strategy/concepts used within my solution.

### Utilized Concepts:
* List manipulation
* List sorting

This function takes as input a list of integers and returns as a string the largest possible product of a subset. To begin I first split the problem into two subproblems, finding the largest possible product of the positive and negative elements in the input array.

* For the positive elements, the largest possible product of them is simply the product of them all.
* The negative elements are not quite as simple. 
  * If there are an even number of negative elements, then we can simply take the product of all the possible numbers as the product will be positive and the largest possible.
  * If there are an odd number of negative elements then the list must be sorted, and then smallest negative element will be dropped. After this we now have an even number of negative elements and can simply take their product.

After this is completed, we return the product of the products of the positive and negative elements as a string.