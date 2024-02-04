def solution(entrances, exits, path):

    # this is a problem of figuring out the maximum possible flow through a network
    # there are several algorithms that can be used to solve this problem
    
    # I will use the Ford-Fulkerson algorithm to do this
    # It operates using augmenting paths, which is an alternate method that could have been used to solve the first problem of level 4
    
    # at its core this is a graph theory problem
    # I am attempting to solve it without using a graph representation
    # Goal is the find the path that maximizes the flow of bunnies
    # I am more or less taking a heuristic approach
    
    # first figure out how many bunnies each state in the path can hold
    # also list to see how many bunnies are in each state
    pathSum = []
    currentAmount = []
    for i in range(len(path)):
        pathSum.append(sum(path[i]))
        if i in entrances:
            currentAmount.append(sum(path[i]))
        else:
            currentAmount.append(0)

    # THIS FUNCTION DOESNT CHOOSE THE OPTIMAL PATH

    # create a function to move from bunnies from one state to another
    def moveBunnies(current, next):
        # check if the next state can take all of the bunnies
        if path[current][next] >= currentAmount[current] and current not in exits:
            # update how many bunnies arrive at the next state
            currentAmount[next] += currentAmount[current]
            # update how many bunnies remain in current state
            currentAmount[current] -= currentAmount[current]
        elif current not in exits:
            # next state can only take some of the bunnies
            canTake = path[current][next]
            # add this amount to the bunnies in the next state
            currentAmount[next] += canTake
            # subtract the bunnies from the previous state
            currentAmount[current] -= canTake
        # implement handling for if we are in an exit state here if needed
        return
    
    # iterate through path
    # for i in range(len(path)):
    #     for j in range(len(path)):
    #         if path[i][j] != 0:
    #             moveBunnies(i, j)

    # Iterate through path
    for i in range(len(path)):
        # Sort the destinations by remaining capacity in descending order
        destinations = sorted(range(len(path)), key=lambda x: path[i][x], reverse=True)
        for j in destinations:
            if path[i][j] != 0:
                moveBunnies(i, j)

    # calculate how many bunnies escape
    escaped = 0
    for i in exits:
        escaped += currentAmount[i]
 
    return escaped

solution([0], [3], [[0, 7, 0, 0], 
                    [0, 0, 6, 0], 
                    [0, 0, 0, 8], 
                    [9, 0, 0, 0]])

solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], 
                          [0, 0, 5, 2, 0, 0], 
                          [0, 0, 0, 0, 4, 4], 
                          [0, 0, 0, 0, 6, 6], 
                          [0, 0, 0, 0, 0, 0], 
                          [0, 0, 0, 0, 0, 0]])

# solution([0], [3], [[0, 10, 20, 0], 
#                     [0, 0, 0, 30], 
#                     [0, 0, 0, 20], 
#                     [0, 0, 0, 0]])

