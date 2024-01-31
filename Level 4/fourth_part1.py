
def solution(banana_list):
    
    # WHAT TO DO IF ODD NUMBER OF TRAINERS
    def gcd(a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if a == b:
            return a
        if a > b:
            return gcd(a - b, b)
        return gcd(a, b - a)
    print(gcd(1,4))

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

    # if first element is odd, check to see if it can be paired with an even
    # or if first element is even, check if it can be paired with an odd one
    
    # Function to locate an odd element within the input list
    def find_odd(input_list):
        # don't check the first element
        for i in range(1, len(input_list)):
            if input_list[i] % 2 != 0:
                # return the index and value of the odd element found
                return {'value':input_list[i], 'index':i}
            
        # no odd element found
        return False
    
    # Function to locate an even element within the input list
    def find_even(input_list):
        # don't check the first element
        for i in range(1, len(input_list)):
            if input_list[i] % 2 == 0:
                # return the index and value of the even element found
                return {'value':input_list[i], 'index':i}
            
        # no even element found
        return False
    
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
        
    # Function to play turns with all other trainers
    def play_turns(input_list, mem_dict):
        # list to store outcomes of playing with each trainer
        # first element; 1 = infinite, 0 = tie
        # second element = index
        outcomes = []
        
        # iterate through all other trainers
        for i in range(1, len(input_list)):
            # boolean to check if turn reached an infinite or tie state
            not_done = True
            # list to store outcomes of turns 
            turns = []
            # initialize first and second trainers
            first = input_list[0]
            second = input_list[i]
            
            # loop until terminal state reached
            while not_done:
                # play a turn
                turn = play_turn(first, second, mem_dict)
                # check if even/odd pair, infinite pair
                if (turn[0] % 2 != 0 and turn[1] % 2 == 0) or (turn[0] % 2 == 0 and turn[1] % 2 != 0):
                    not_done = False
                    outcomes.append([1, i])
                # if we return to a state we have seen before, likely that we are in infinite state
                if turn in turns:
                    not_done = False
                    outcomes.append([1, i])
                # if two trainers have same amount, we also stop
                if turn == [-1, -1]:
                    not_done = False
                    outcomes.append([0, i])
                # keep track of outcomes of turns
                turns.append(turn)
                # update first and second trainer values
                first, second = turn
                
        return outcomes
        
    # create counters for trainers that leave and stay
    stay = 0
    leave = 0
    
    # trainers that form infinite pairs with no one
    problems = []
    
    # copy of banana list to work on
    copy_list = banana_list[:]
    
    # start iterating through the list
    while len(copy_list) > 0:
        # locate current trainer
        current = copy_list[0]
        
        # check if the current trainer is odd, then find an even trainer and remove them both
        next_even = False
        next_odd = False
        flag = False
        if current % 2 != 0:
            next_even = find_even(copy_list)
            if next_even != False:
                # this means we did find an even number
                # remove current trainer and the one with the even number from the list
                copy_list.pop(0)
                copy_list.pop(next_even["index"] - 1)
                # they are stuck fighting forever
                stay += 2
            else:
                # if entering here, this means that no even number was found
                # need to play turns on other elements in the list to find if another infinite pair can occur
                # raise flag if this occurs
                flag = True
        else:
            # current trainer is even
            next_odd = find_odd(copy_list)
            if next_odd != False:
                # we did find an odd number
                # remove them both from the list
                copy_list.pop(0)
                copy_list.pop(next_odd["index"] - 1)
                # they will fight forever
                stay += 2
            else:
                # no odd trainer found
                # raise flag
                flag = True
                
        # check if flag was raised
        if flag:
            # this means no immediate pair was found that will be stuck forever
            # need to play turns with other trainers to see if an infinite pair can be found
            possibilites = play_turns(copy_list, mem)
            
            found_infinite = False
            
            # iterate through possibilities to see if an infinite pair was found
            for i in range(len(possibilites)):
                if possibilites[i][0] == 1:
                    # found infinite pair, remove both trainers
                    found_infinite = True
                    copy_list.pop(0)
                    copy_list.pop(possibilites[i][0] - 1)
                    stay += 2
                    break
            
            if not found_infinite:
                # did not find infinite pair
                # add trainer to problem list
                problems.append(current)
                # remove current element from banana list
                copy_list.pop(0)
                # print('no infinite partner found')
                # if after banana list is empty, we have even number of problem items, add them to the ones that remain
    
    # now play turns for all problem trainers
    print(problems)

    return leave + len(banana_list)
    
    

    
    # basic rules
    # if 1 is odd and 1 is even, this will be infinite
    # if both are odd we must play the turn through
    # if both are even either could happen
    # divide both by 2 to see if it will be infinite
    
solution([1,7,3,21,13,19])