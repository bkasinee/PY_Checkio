# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 17:04:48 2016

@author: ssits
"""



def is_palindromic(sub_text):
    lst_str1=list(sub_text)
    lst_str2=reversed(list(sub_text))
    str_str1=''.join(lst_str1)
    str_str2=''.join(lst_str2)
    if (str_str1==str_str2):
        return True
    else:
        return False
    
    
def longest_palindromic(text):
    
    max_text=""
    
    for i in range(0,len(text)):
        for x in range(i+1,len(text)+1):
            substr_text=text[i:x]
            if ((len(substr_text)>len(max_text)) & (is_palindromic(substr_text))):
                max_text=substr_text
        
    
    return max_text

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
