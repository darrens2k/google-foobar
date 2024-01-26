def solution(n):

    # dictionary for memoization
    mem = {}

    # helper function to find sum of odd divisors
    def sum_odd_divisors(n):

        divisor_sum = 0

        for i in range(1, n + 1):

            if n % i == 0 and i % 2 != 0:
                
                divisor_sum += i
    
        return divisor_sum
    
    # helper function to implement the partition function
    # finds all distinct partitions that sum to n
    # reference: https://mathworld.wolfram.com/PartitionFunctionQ.html
    def distinct_partitions(n):

        # base cases
        if n == 0 or n == 1:

            return 1
        
        # check if in memory
        if n in mem:
            return mem[n]

        temp_sum = 0

        for k in range(1, n + 1):

            temp_sum += sum_odd_divisors(k) * distinct_partitions(n - k)

        q = (1.0 / n) * temp_sum

        # save to memory
        mem[n] = q

        return q

    return int(distinct_partitions(n) - 1)

print(solution(200))