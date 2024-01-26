# solution to first problem

def solution(i):

    # generate string of primes to 5 beyond given index
    first_prime = 2

    # create function to locate the next prime
    def find_next_prime(current):

        # first guess is just adding 1
        next_guess = current + 1

        # infinite loop until next prime is found
        while True:
            # check if current guess is a prime
            for j in range(2, next_guess):
                # if this is true, the guess is not a prime
                if next_guess % j == 0:
                    break
            else: 
                print(next_guess, j)
                return next_guess
            # move to next guess
            next_guess += 1
    
    # create string
    primes = '' + str(first_prime)

    current_prime = first_prime

    while len(primes) <= i + 5:

        current_prime = find_next_prime(current_prime)
        
        primes += str(current_prime)

    return primes[i:i+5]


print(solution(-3))
                
        