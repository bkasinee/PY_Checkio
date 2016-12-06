# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:09:58 2016

@author: ssits
"""

def rotate(state, pipe_numbers):
    
    lst_out=[]
    
    for i in range(0,len(state)):
        if (i>0): 
            new_state=[x1 for x1 in state[(-i):]] + [x2 for x2 in state[:-(i)]] 
        else:
            new_state=state
        
        list_false = [n for n in pipe_numbers if new_state[n]==0]
        
        if (len(list_false)==0):
            lst_out=lst_out+[i]

        
    return lst_out


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"
    assert rotate([1,1,1],[0])==[0, 1, 2]