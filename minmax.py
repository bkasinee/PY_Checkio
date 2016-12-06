# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 00:43:07 2016

@author: ssits
"""
def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        vars = args[0]
    else:
        vars = args[:]
    ans = None
    for arg in vars:
        if ans is None:
            ans = arg
            continue
        if key is not None:
            if key(arg) < key(ans):
                ans = arg
        else:
            if arg < ans:
                ans = arg
    return ans


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        vars = args[0]
    else:
        vars = args[:]
    ans = None
    for arg in vars:
        if ans is None:
            ans = arg
            continue
        if key is not None:
            if key(arg) > key(ans):
                ans = arg
        else:
            if arg > ans:
                ans = arg
    return ans



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(range(6)) == 5 ,"max range"
    assert min((9, )) == 9, "null"
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"