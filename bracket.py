# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 13:10:50 2016

@author: ssits
"""

def checkio(expression):
    
    stack=[]
    
    for i in range(0,len(expression)):
        

        if ((expression[i]=="(") | (expression[i]=="[") | (expression[i]=="{")) :
            stack.append(expression[i])

            
        if (expression[i]==")") | (expression[i]=="]") | (expression[i]=="}"):
            
            if (len(stack)==0):
                return False
                
            char_pop=stack.pop()
                
            if (expression[i]==")") :                    
                if (char_pop!="("):
                    return False
                    
            elif (expression[i]=="]") :                   
                if (char_pop!="["):
                    return False
                    
            elif (expression[i]=="}"):                   
                if (char_pop!="{"):
                    return False
                             
    if (len(stack)>0):
        return False
            

                
    return True 

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"