def solution(xs):

    # find largest possible sum within subset of array
    # kind of like a dynamic programming question

    # if only 1 number, then return that number
    if len(xs) == 1:
        return xs[0]

    # keep track of positive and negative numbers 
    negative = []
    positive = []
    
    for elem in xs:

        if elem >= 1:
            # only take positives bigger than 1, they can increase product
            positive.append(elem)
        
        elif elem <= -1:
            # include negative 1, could multiply with a negative number to make a positive and increase product
            negative.append(elem)
    
    # largest possible product of positives is just multiplying them
    pos_max = 1
    for pos in positive:
        pos_max = pos_max * pos

    # figure out largest product from negatives
    neg_max = 1

    # if there are an even number of negative numbers, just multiply them together
    if len(negative) % 2 == 0:
        for neg in negative:
            neg_max = neg_max * neg

    # odd number of negative numbers
    else:
        # if we drop the smallest number, then we will get the largest product
        # this then reduces to the case of an even amount of negative numbers

        # locate the most positive number
        temp_max = max(negative)
        
        # remove most positive number from negative list
        negative.remove(temp_max)

        # now this is the same case as an even amount of negative numbers
        for neg in negative:
            neg_max = neg_max * neg

    if len(positive)==0 and len(negative)==0:
        return "0"

    return str(pos_max * neg_max)


# Test the function with some example inputs
test_cases = [
    [3, 4, 5, 6],          # Expected result: 120 (6 * 5 * 4)
    [-3, -4, -5, -6],      # Expected result: -60 (-3 * -4 * -5)
    [-3, 4, -5, 6],        # Expected result: 90 (6 * 4 * -5)
    [0, 4, 5, 6],          # Expected result: 120 (6 * 5 * 4)
    [7],                   # Expected result: 7 (As it's the only element)
    [7, 8],                # Expected result: 56 (7 * 8)
    [0],
    [],
    [-1],
    [0,-1],
    [0,1]
]

for xs in test_cases:
    print(f"List: {xs} -> Largest Product: {solution(xs)}")
