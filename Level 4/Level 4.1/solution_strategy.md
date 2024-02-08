# Solution Strategy
### A high level overview of the strategy/concepts used within my solution.

### Utilized Concepts:
* GCD
* Sets in Python

At its core this is really a graph theory problem relating to maximum matching, and it could be solved using the Blossom algorithm. I went about it in a different way, following a somewhat rule based approach. I devised a set of rules to figure out if a given pair of trainers will be in an infinite battle or not, and compared all of the trainers to each other.

Here are the rules I followed:
* If the amount of bananas each trainer has sum to an odd number, they will be in an infinite battle
* If they are equal then they will stop battling (not in an infinite battle)
* If the sum of the amount of bananas they have divided by their GCD is a power of 2 then they will be an infinite battle.

Once you know what pairs will result in infinite battles, then you can simply begin to pair up trainers starting with the trainer that can be paried with the least amount of other trainers.

