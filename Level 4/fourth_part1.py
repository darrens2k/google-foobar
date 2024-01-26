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
        
    # create counters for trainers that leave and stay
    stay = 0
    leave = 0
    
    # start iterating through the list
    
    # locate current trainer
    current = banana_list[0]
    
    # check if the current trainer is odd, then find an even trainer and remove them both
    if current % 2 != 0:
        next_even = find_even(banana_list)
        
    # first iterate through the list and remove all trainer pairs that would be stuck forever
    # even/odd pair will fight infinitely
    
    
    
    # basic rules
    # if 1 is odd and 1 is even, this will be infinite
    # if both are odd we must play the turn through
    # if both are even either could happen
    # divide both by 2 to see if it will be infinite
    
solution([1,2])