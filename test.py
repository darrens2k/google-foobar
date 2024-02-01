
def solution(banana_list):
    
    # Base cases:
    
    # If there's only one trainer, return 1
    if len(banana_list) == 1:
        return 1
    
    # If all trainers have the same number of bananas, return the number of trainers
    same_amount = True
    prev = banana_list[0]
    for value in banana_list:
        if value != prev:
            same_amount = False
            break
    
    if same_amount:
        return len(banana_list)
    
    # Initialize a nested list to store possible pairings for each trainer
    # 1 represents infinite pairing, 0 represents they will leave
    # Trainer cannot be paired with themself
    potentials = []
    for i in range(len(banana_list)):
        temp = []
        for j in range(len(banana_list)):
            temp.append(0)
        potentials.append(temp)
    
    # Create a memory for memoization
    mem = {}
    
    # Function to play a single turn
    def play_turn(a, b, memory):
        # Check if we have seen this before
        if (a, b) in memory:
            return memory[(a,b)]
        # Nothing happens if a = b
        if a == b:
            return [-1, -1]
        # A loses if it is bigger
        if a > b:
            memory[(a, b)] = [a - b, b + b]
            return [a - b, b + b]
        # B loses if it is bigger
        else:
            memory[(a, b)] = [a + a, b - a]
            return [a + a, b - a]
        
    # Function to determine if two trainers will be in an infinite battle or not
    def play_turns(a, b, result, input_list, mem_dict):
        # A and B are indices of the elements in the input list
        first = input_list[a]
        second = input_list[b]
        
        # An odd/even pair will be stuck in an infinite battle
        if (first % 2 == 0 and second % 2 != 0) or (first % 2 != 0 and second % 2 == 0):        
            # Update the outcomes list
            result[a][b] = 1
            return result
            
        # Play turns to check outcome
        # Boolean to check if turn reached an infinite or tie state
        not_done = True
        # List to store outcomes of turns 
        turns = []
        # Initialize counter
        counter = 0
        
        # Loop until terminal state reached, or 15 turns have passed
        while not_done or counter == 15:
            # Play a turn
            turn = play_turn(first, second, mem_dict)
            # Check if even/odd pair, infinite pair
            if (turn[0] % 2 != 0 and turn[1] % 2 == 0) or (turn[0] % 2 == 0 and turn[1] % 2 != 0):
                not_done = False
                result[a][b] = 1
            # If we return to a state we have seen before, likely that we are in infinite state
            if turn in turns:
                not_done = False
                result[a][b] = 1
            # If two trainers have the same amount, we also stop, not infinite pair
            if turn == [-1, -1]:
                not_done = False
                result[a][b] = 0
            # Keep track of outcomes of turns
            turns.append(turn)
            # Update first and second trainer values
            first, second = turn
            # Update counter
            counter += 1
                
        return result
        
    # Create counters for trainers that leave and stay
    stay = 0
    leave = 0
    
    # Iterate through the input list
    for i in range(len(banana_list)):
        # Goal is to figure out what other trainers each trainer can be paired with
        # Nested loop is required
        for j in range(len(banana_list)):
            if i != j:
                # Call function that will accept two trainers, and calculate whether or not they will be in an infinite battle
                # Don't call a trainer on itself
                potentials = play_turns(i, j, potentials, banana_list, mem)
    
    # We have now created a graph that represents what trainers can be paired with what trainers
    # We need to find the maximum possible amount of edges in this graph that can be connected
    # This is called the maximal matching set
    # The blossom algorithm can be used to find the maximal matching set a general graph
    
    # Now we need to convert the matrix to a graph
    # This can be done using a dictionary
    graph = {}
    for i in range(len(potentials)):
        temp = []
        for j in range(len(potentials)):
            if potentials[i][j] == 1:
                temp.append(j)
        graph[i] = temp
    
    
    # Implement blossom algorithm
    # Credit for Implementation: https://medium.com/@ckildalbrandt/demystifying-edmonds-blossom-algorithm-with-python-code-6353eb043311
    def lca(match, base, p, a, b):
        used = [False] * len(match)
        while True:
            a = base[a]
            used[a] = True
            if match[a] == -1:
                break
            a = p[match[a]]
        while True:
            b = base[b]
            if used[b]:
                return b
            b = p[match[b]]

    # Mark the path from v to the base of the blossom
    def mark_path(match, base, blossom, p, v, b, children):
        while base[v] != b:
            blossom[base[v]] = blossom[base[match[v]]] = True
            p[v] = children
            children = match[v]
            v = p[match[v]]

    def find_path(graph, match, p, root):
        n = len(graph)
        used = [False] * n
        p[:] = [-1] * n
        base = list(range(n))
        used[root] = True
        q = [root]

        while q:
            v = q.pop(0)
            for to in graph[v]:
                if base[v] == base[to] or match[v] == to:
                    continue
                if to == root or (match[to] != -1 and p[match[to]] != -1):
                    curbase = lca(match, base, p, v, to)
                    blossom = [False] * n
                    mark_path(match, base, blossom, p, v, curbase, to)
                    mark_path(match, base, blossom, p, to, curbase, v)
                    for i in range(n):
                        if blossom[base[i]]:
                            base[i] = curbase
                            if not used[i]:
                                used[i] = True
                                q.append(i)
                elif p[to] == -1:
                    p[to] = v
                    if match[to] == -1:
                        return to
                    to = match[to]
                    used[to] = True
                    q.append(to)
        return -1

    # Implementation of Blossom Algorithm
    def max_matching(graph):
        n = len(graph)
        match = [-1] * n
        p = [0] * n
        for i in range(n):
            if match[i] == -1:
                v = find_path(graph, match, p, i)
                while v != -1:
                    pv = p[v]
                    ppv = match[pv]
                    match[v] = pv
                    match[pv] = v
                    v = ppv
        # Returns number of pairs in graph
        return sum(1 for x in match if x != -1)

    # Return the difference between the total number of trainers and the size of the maximal matching set
    return len(banana_list) - max_matching(graph)

# Test the function with a sample input
# solution([1, 7, 3, 21, 13, 19])
solution([33553445, 987, 155, 94, 1, 47])
# solution([32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1])
# The expected output for the provided input is 2
