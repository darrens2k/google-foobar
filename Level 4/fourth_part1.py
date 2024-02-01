
def solution(banana_list):
    
    # Function to check if a number is a power of 2
    def isPowerOfTwo(n):
        # Divide (integer division) by 2 until either # % 2 is 0 or the number reaches 0
        if (n == 0):
            return False
        while (n != 1):
            if (n % 2 != 0):
                return False
            # change to / if in python 2 or // if in python 3
            n = n // 2
    
        return True
    
    # Function to play turns of thumbwar
    def play_turns(x, y):
        # if sum is odd they will be stuck in infinite battle
        if (x + y) % 2 != 0: 
            return 0
        # if they are equal they will stop battling
        if (x == y): 
            return 1
        # if the sum divided by the gcd is not a power of 2, then they stop battling
        if isPowerOfTwo((x + y) // gcd(x, y)):
            return 1
        return 0

    # Function to find gcd of two integers
    def gcd(a, b):
        # ensure a is greater than or equal to b
        if a < b:
            a, b = b, a
        
        # euclidean algorithm
        while b != 0:
            a, b = b, a % b
        
        return a

    # Function to compute amount of edges in maximum matches set
    # Could also apply the blossom algorithm here
    def leastRemainingNumbersToMatch(target, infinite_battles):
        # dict to store the amount of times each number appears in an infinite battle
        numbers = {}
        for infinite in infinite_battles:
            if infinite[0] in numbers:
                numbers[infinite[0]] += 1
            else:
                numbers[infinite[0]] = 1
            if infinite[1] in numbers:
                numbers[infinite[1]] += 1
            else:
                numbers[infinite[1]] = 1
                
        # sort dictionary to locate numbers/trainers that are paired the least
        numbers = sorted(numbers, key = lambda x: numbers[x])
        created_pairs = set()
        for n in numbers:
            for infinite in infinite_battles:
                # loop to create matches
                if infinite[0] in created_pairs or infinite[1] in created_pairs:
                    # if a trainer is in an already created pair, skip it
                    continue
                if n in infinite:
                    created_pairs.add(infinite[0])
                    created_pairs.add(infinite[1])
        return target - len(created_pairs)

    # set to store infinite battles
    infinite_battles = set()
    for i in range(len(banana_list) - 1):
        for j in range(i + 1, len(banana_list)):
            # play turns of all trainers
            result = play_turns(banana_list[i], banana_list[j])
            if result == 0:
                # save to set if inifinite battle
                infinite_battles.add((i, j))

    return leastRemainingNumbersToMatch(len(banana_list), infinite_battles)
    
solution([1, 7, 3, 21, 13, 19])
solution([33553445, 987, 155, 94, 1, 47])
solution([32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1])
solution([7, 1, 7, 1, 7, 8])
# solution([1,1,1,2])
# ans is 2