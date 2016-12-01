# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 14:57:47 2016

@author: ssits
"""

def checkio(number):
    str_a= list(bin(number))
    my_list = [int(x) for x in str_a if x == '1']    
    return sum(my_list)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9