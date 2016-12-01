# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 12:15:38 2016

@author: ssits
"""

def res_sum(lastSum,data):
    
    item_value=data[0]
    
    if (len(data[1:])>0):
        lastSum= res_sum(lastSum+item_value,data[1:])
    else:
        lastSum= lastSum+item_value
        
    return lastSum

 
    
    
    

def checkio(data):
    lastSum=0
    return res_sum(lastSum,data)

if __name__ == "__main__":
    print checkio([1, 2, 3])
    print checkio([1, 2, 3]) == 6
    print checkio([2, 2, 2, 2, 2, 2])
    print checkio([2, 2, 2, 2, 2, 2]) == 12
