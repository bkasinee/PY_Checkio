# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 14:29:19 2016

@author: ssits
"""

def char_position(letter):
    return ord(letter) - 97

def pos_to_char(pos):
    return chr(pos + 97)

def safe_pawns(pawns):
    count_safe=0
    for x in pawns:
        lst_x=list(x)
        chr_lb=pos_to_char(char_position(lst_x[0])-1)
        chr_rb=pos_to_char(char_position(lst_x[0])+1)
        int_rowb=int(lst_x[1])-1
        str_lb=chr_lb + str(int_rowb)
        str_rb=chr_rb + str(int_rowb)
        if ((str_lb in pawns) | (str_rb in pawns)):
            count_safe=count_safe+1
            
    return count_safe
    
    
    
    
    
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1