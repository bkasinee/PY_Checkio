# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 19:42:22 2016

@author: ssits
"""


def checkio(data):

    #replace this for solution
    x1=int(data[1])
    y1=int(data[3])
    
    x2=int(data[7])
    y2=int(data[9])

    x3=int(data[13])
    y3=int(data[15])
    
    
    
    offset = pow(x2,2) + pow(y2,2);
    bc =   ( pow(x1,2) + pow(y1,2) - offset )/2.0;
    cd =   (offset - pow(x3, 2) - pow(y3, 2))/2.0;
    det =  (x1 - x2) * (y2 - y3) - (x2 - x3)* (y1 - y2); 

    idet = 1.0/det;

    centerx =  (bc * (y2 - y3) - cd * (y1 - y2)) * idet;
    centery =  (cd * (x1 - x2) - bc * (x2 - x3)) * idet;
    radius = pow( pow(x2 - centerx,2) + pow(y2-centery,2) , 0.5);    
    
    str_return="(x-" + ('{:.2f}'.format(centerx)).rstrip('0').rstrip('.') + ")^2+(y-"  + ('{:.2f}'.format(centery)).rstrip('0').rstrip('.') + ")^2=" + ('{:.2f}'.format(radius)).rstrip('0').rstrip('.') + "^2"
    return str_return


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"