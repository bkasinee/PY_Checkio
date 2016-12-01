# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:18:20 2016

@author: ssits
"""
def max_historgram(i,x,histogram):
    
    area=x
    
        
    l=i-1
    
    while (l>=0):
        if (histogram[l]>=x):        
            area=area+x
            l=l-1
        else:
             break
         
    u=i+1
    
    while (u<=len(histogram)-1):
        if (histogram[u]>=x):        
            area=area+x
            u=u+1
        else:
             break
         
    return area

def largest_histogram(histogram):

    max_his=0
    
    for i in range(0,len(histogram)):
        his_value=histogram[i]
        for x in range(0,his_value):
            max_his_temp=max_historgram(i,x+1,histogram)
            if (max_his_temp>max_his):
                max_his=max_his_temp
        
    
    return max_his


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")