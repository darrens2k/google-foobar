def solution(m):
    
    # This is a case of an absorbing markov chain
    # A markov chain that is guaranteed to end in a terminal/abosrbing state
    
    # Videos I referenced below
    # https://www.youtube.com/watch?v=bTeKu7WdbT8&ab_channel=patrickJMT
    # https://www.youtube.com/watch?v=BsOkOaB8SFk&ab_channel=patrickJMT
    # https://www.youtube.com/watch?v=qhnFHnLkrfA&ab_channel=patrickJMT

    # needed to work with fractions
    from fractions import Fraction
    
    # handle base cases
    if m == [[0]] or len(m) == 0:
        # guaranteed to be in a terminal state
        return [1,1]

    # in foobar we can not use numpy or sympy, we must build functions to multiply matrices
    def multiply_matrices(a, b):
        # function to return the product of matrices a and b
        # these matrices contain fractions
        
        # relevant metrics
        rows_a = len(a)
        cols_b = len(b[0])
        
        # create output
        output = [[0 for j in range(cols_b)] for i in range(rows_a)]

        # begin multiplication
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    output[i][j] += a[i][k] * b[k][j]           
        
        return output
    
    # we will need to subtract matrices
    def subtract_matrices(a, b):
        # it is assumed both matrices are composed of fractions and are square

        # create output
        output = [[0 for j in range(len(a[0]))] for i in range(len(a))]

        # do subtraction
        for i in range(len(a)):
            for j in range(len(a[0])):
                output[i][j] = a[i][j] - b[i][j]

        return output

    # we will also need to be able to invert matrices
    def inverse_matrix(matrix):
        # get the dimensions of the matrix
        rows = len(matrix)
        cols = len(matrix[0])

        # create the identity matrix
        identity = [[Fraction(0) for j in range(cols)] for i in range(rows)]
        for i in range(rows):
            identity[i][i] = Fraction(1)

        # perform Gauss-Jordan elimination
        for j in range(cols):
            # find the row with the largest absolute value in column j
            max_row = j
            for i in range(j + 1, rows):
                if abs(matrix[i][j]) > abs(matrix[max_row][j]):
                    max_row = i

            # swap the rows
            matrix[j], matrix[max_row] = matrix[max_row], matrix[j]
            identity[j], identity[max_row] = identity[max_row], identity[j]

            # scale the pivot row
            pivot = matrix[j][j]
            if pivot == 0:
                return "Error: Matrix is singular"
            for k in range(j, cols):
                matrix[j][k] /= pivot
            for k in range(cols):
                identity[j][k] /= pivot

            # eliminate the entries below the pivot
            for i in range(j + 1, rows):
                factor = matrix[i][j]
                for k in range(j, cols):
                    matrix[i][k] -= factor * matrix[j][k]
                for k in range(cols):
                    identity[i][k] -= factor * identity[j][k]

        # eliminate the entries above the pivot
        for j in range(cols - 1, 0, -1):
            for i in range(j):
                factor = matrix[i][j]
                for k in range(cols):
                    identity[i][k] -= factor * identity[j][k]

        return identity

    # first put the matrix into standard form
    # all terminal states at the top

    # figure out what rows are terminal and not 
    not_terminal = []
    terminal = []
    for i in range(len(m)):

        # boolean to check if every element is 0
        is_zero = True
        for j in range(len(m[i])):
            if m[i][j] != 0:
                is_zero = False
            
        if is_zero:
            # state is terminal
            terminal.append(i)
        else:
            # if state is not terminal
            not_terminal.append(i)        
    
    # check if first state is terminal
    if 0 in terminal:
        # no probability to enter other states
        output = [1]
        for i in range(len(terminal) - 1):
            output.append(0)
        # add denominator
        output.append(1)
        return output

    # put all terminal states at the top
    m2 = []
    row_counter = 0
    for state in terminal:
        m2.append(m[state])
        # terminal state can only lead to itself
        m2[row_counter][row_counter] = 1
        row_counter += 1
    for state in not_terminal:
        col_counter = 0
        temp_row = []
        for k in range(len(m)):
            # since we re-ordered the states, the probabilities must be re-ordered as well
            if k < len(terminal):
                temp_row.append(m[state][terminal[k]])
            else:
                temp_row.append(m[state][not_terminal[col_counter]])
                col_counter += 1
        m2.append(temp_row)
    
    # create a new matrix to store Fraction objects
    m2_fractions = [[0 for j in range(len(m2[0]))] for i in range(len(m2))]

    # convert all values to Fraction
    for i in range(len(m2)):
        denominator = sum(m2[i])
        for j in range(len(m2[i])):
            # convert each element to Fraction
            m2_fractions[i][j] = Fraction(m2[i][j], denominator)

    # matrix is now in standard form
    # Next we need the limiting matrix
        
    # locate sub matrices of m2: I, R, Q
    
    # I is identity created by terminal states
    # R is created by non-terminal states under terminal states
    # Q is non-terminal states not under terminal states
    I = [row[:len(terminal)] for row in m2_fractions[:len(terminal)]]
    R = [row[:len(terminal)] for row in m2_fractions[len(terminal):]]
    Q = [row[len(terminal):] for row in m2_fractions[len(terminal):]]

    # solve fundamental matrix as inverse of I - Q
    
    # create identity same size as Q
    # create the identity matrix
    identity_sized = [[Fraction(0) for j in range(len(Q))] for i in range(len(Q))]
    for i in range(len(Q)):
        identity_sized[i][i] = Fraction(1)

    # take inverse
    fundamental_matrix = inverse_matrix(subtract_matrices(identity_sized, Q))

    # compute FR
    FR = multiply_matrices(fundamental_matrix, R)
    
    # begin assembling output
    denominators = []
    numerators = []

    for i in range(len(FR[0])):
        value = FR[0][i]
        numerators.append(value.numerator)
        denominators.append(value.denominator)    
    
    # calculate greatest common denominator 
    greatest_common_denominator = max(denominators)
    for i in range(len(denominators)):
        if greatest_common_denominator % denominators[i] != 0:
            while greatest_common_denominator % denominators[i] != 0:
                # loop until gcf is found
                greatest_common_denominator *= denominators[i] / 2

    # adjust numerators as needed to match common denominator
    for i in range(len(denominators)):
        if denominators[i] != 0 and denominators[i] != greatest_common_denominator:
            numerators[i] *= int(greatest_common_denominator / denominators[i])    

    numerators.append(greatest_common_denominator)
    
    return numerators

solution([[0, 2, 1, 0, 0], 
          [0, 0, 0, 3, 4], 
          [0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0]])
