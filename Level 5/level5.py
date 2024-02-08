def solution(s):
    
    # this problem uses the beatty sequence, or is similar to it at the very least
    
    # to use this sequence we likely need a recurrence relation
    # recurrence relation provided here: https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s
    
    # we need to maintain a precision of up to 101 digits (or 100 decimals)
    # given that the inputs can have 101 digits
    
    # the only number we input aside from the actual input is root 2, so we need this to 100 decimal precision
    preciseDecimalRoot2 = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
        
    # convert the string input to an int
    s = int(s)
    
    def find_sum(num):

        # base case
        if num < 1:
            return 0
        elif num == 1:
            return 1
        
        # this is reducing the size of our problem quickly, it multiplies the input by root2 - 1, which is the decmial portion of root2
        # must normalize the decimal portion to a decimal by dividing by 100 decimal places
        n_next = num * (preciseDecimalRoot2 / 10**100)
        
        return num * n_next + num * (num + 1)/2 - n_next * (n_next + 1)/2 - find_sum(n_next)
    
    # return answer as a floored integer converted to a string
    return str(int(find_sum(s)))
    
solution("5")


