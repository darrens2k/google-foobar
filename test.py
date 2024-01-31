
def solution(banana_list):

    # define base cases
    
    # if only 1 trainer
    if len(banana_list) == 1:
        return 1
    
    # if all trainers have the same amount of bananas
    same_amount = True
    prev = banana_list[0]
    for value in banana_list:
        if value != prev:
            same_amount = False
            break
    
    if same_amount:
        return len(banana_list)
    
    # define a nested list to store possible pairings for each trainer
    # 1 = infinite pairing, 0 = they will leave
    # trainer cannot be paired with themself
    potentials = []
    for i in range(len(banana_list)):
        temp = []
        for j in range(len(banana_list)):
            temp.append(0)
        potentials.append(temp)
    
    # create a memory for memoization
    mem = {}
    
    # Function to play a single turn
    def play_turn(a, b, memory):
        # check if we have seen this before
        if (a, b) in memory:
            return memory[(a,b)]
        # nothing happens if a = b
        if a == b:
            return [-1, -1]
        # a loses if it is bigger
        if a > b:
            memory[(a, b)] = [a - b, b + b]
            return [a - b, b + b]
        # b loses if it is bigger
        else:
            memory[(a, b)] = [a + a, b - a]
            return [a + a, b - a]
        
    # Function to determine if two trainers will be in an infinite battle or not
    def play_turns(a, b, result, input_list, mem_dict):
        # a and b are indices of the elements in the input list
        first = input_list[a]
        second = input_list[b]
        
        # an odd/even pair will be stuck in an infinite battle
        if (first % 2 == 0 and second % 2 != 0) or (first % 2 != 0 and second % 2 == 0):        
            # update the outcomes list
            result[a][b] = 1
            return result
            
        # play turns to check outcome
        # boolean to check if turn reached an infinite or tie state
        not_done = True
        # list to store outcomes of turns 
        turns = []
        # initialize counter
        counter = 0
        
        # loop until terminal state reached, or 15 turns have past
        while not_done or counter == 15:
            # play a turn
            turn = play_turn(first, second, mem_dict)
            # check if even/odd pair, infinite pair
            if (turn[0] % 2 != 0 and turn[1] % 2 == 0) or (turn[0] % 2 == 0 and turn[1] % 2 != 0):
                not_done = False
                result[a][b] = 1
            # if we return to a state we have seen before, likely that we are in infinite state
            if turn in turns:
                not_done = False
                result[a][b] = 1
            # if two trainers have same amount, we also stop, not infinite pair
            if turn == [-1, -1]:
                not_done = False
                result[a][b] = 0
            # keep track of outcomes of turns
            turns.append(turn)
            # update first and second trainer values
            first, second = turn
            # update counter
            counter += 1
                
        return result
        
    # create counters for trainers that leave and stay
    stay = 0
    leave = 0
    
    # trainers that form infinite pairs with no one
    problems = []
    
    # copy of banana list to work on
    copy_list = banana_list[:]
    
    # iterate through the input list
    for i in range(len(banana_list)):
        # goal is to figure out what other trainers each trainer can be paired with
        # nested loop is required
        for j in range(len(banana_list)):
            if i != j:
                # call function that will accept two trainers, and calculate whether or not they will be in an infinite battle
                # don't call a trainer on itself
                potentials = play_turns(i, j, potentials, banana_list, mem)
        
    # figure out how many pairs each trainer can make
    totals = []
    for res in potentials:
        totals.append(sum(res))
        # if a single row contains all 0s, change to 200s
        # this will ensure we recognize later on that it has no possible pairs
        if sum(res) == 0:
            for i in range(len(potentials)):
                res[i] = 200
    
    # create a pair for the trainer with smallest amount of potential pairs
    # pick the option that appears the least for other trainers
    
    # function to check how many other trainers share these 1s
    def check_ones(col):
        # counter
        count = 0
        # iterate through the potentials matrix
        for i in range(len(potentials)):
            # check if each row shares the 1 located in the col
            if potentials[i][col] == 1:
                count += 1
        # return amount of trainers that share that 1
        return count
    # loop through potentials
    # boolean for loop condition
    finished = False
    while not finished:
        print(totals)
        # trainer with smallest amount of pairs
        lowest = min(totals)
        # index of this trainer (row of trainer in potentials)
        loc = totals.index(lowest)
        # check if the lowest row is 100s
        if potentials[loc][0] >= 100:
            # exit if this is the case
            finished = True
            break
        # locate all the 1s in this row
        # keep track of the one with lowest amount of occurrences
        lowest = [0, 100]
        ones = []
        for i in range(len(potentials)):
            if potentials[loc][i] == 1:
                occurences = check_ones(i)
                # ones = [col of 1, # of other trainers that share it]
                ones.append([i, occurences])
                # update lowest occurence location
                if occurences < lowest[1]:
                    lowest = [i, occurences]
        
        # remove this 1 and current trainer from the list
        for i in range(len(potentials)):
            if potentials[i][0] < 100:
                # change the 1 to 0 for all trainers
                potentials[i][lowest[0]] = 0
                # change the current trainer to 0 for all trainers
                potentials[i][loc] = 0
                # since the current trainer is removed, replace its row with 100s
                if i == loc:
                    for j in range(len(potentials)):
                        potentials[i][j] = 100
        
        # update the lowest value of totals to 100 so it is not picked again
        totals[loc] = 100
    
    # if at the end we have only 100s in potentials, no trainers remain
    # if we have 200s, then some trainers are left over
    for i in range(len(potentials)):
        if potentials[i][0] == 100:
            stay += 1
        else:
            leave += 1
    
    for res in potentials:
        print(res)
    

    return leave
    
    

    
    # basic rules
    # if 1 is odd and 1 is even, this will be infinite
    # if both are odd we must play the turn through
    # if both are even either could happen
    # divide both by 2 to see if it will be infinite
    
solution([1,7,2])