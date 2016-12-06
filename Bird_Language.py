# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:03:58 2016

@author: ssits
"""

VOWELS = "aeiouy"

def translate(phrase):
    set_vow=set(VOWELS)
    lst_phrase=list(phrase)
    i=0
    out_phrase=""
    while (i < len(lst_phrase)):
        if (lst_phrase[i] in set_vow):
            out_phrase=out_phrase + lst_phrase[i]
            i=i+3
        elif (lst_phrase[i].strip()==""):
            out_phrase=out_phrase + " "
            i=i+1
        else:
            out_phrase=out_phrase + lst_phrase[i]
            i=i+2
    return out_phrase

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"