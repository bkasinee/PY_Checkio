import math

def nCr(n,r):
    f = math.factorial
    return f(n) / (f(r) * f(n-r))
    
'''
ref: http://mathworld.wolfram.com/Dice.html (equation #9)
'''
def generating_func(n,m,s):
    sum_ways=0
    for k in range(0, (((s-n)/m) + 1 )):
        sum_ways = sum_ways + (  ((-1)**k)  *  nCr( s-(m*k)-1 , n-1  )  *   nCr( n , k  )  ) 
        
    return sum_ways
    
def probability(dice_number, sides, target):
    if (target<=(sides*dice_number)):
        cof=generating_func(dice_number, sides, target)
        return round(cof/(float(sides)**dice_number),4)
    else:
        return 0.0000  
    

if __name__ == '__main__':
    #These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
        
    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
