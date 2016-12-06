# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 15:35:51 2016

@author: ssits
"""
def checkHealthySub(x,grid):
    
    for l in range(1,((x[2]+1)/2)):
            
                ex_len=x[2]-(2*l)
                
                #Left Check
                x_cor=x[0]-l
                y_cor_str=x[1]-((ex_len)/2)
                y_cor_end=x[1]+((ex_len)/2)
                
                
                if (x_cor<0):
                    x_cor=0
                    
                if (x_cor>(len(grid[0])-1)):
                    x_cor=(len(grid[0])-1)

                
                if (y_cor_str<0):
                    y_cor_str=0

                
                if (y_cor_end>(len(grid[0])-1)):
                    y_cor_end=(len(grid[0])-1)
                
                #lst_zero=[r for r in grid[x_cor][y_cor_str:y_cor_end] if r==0]
                
                
                lst_zero=[grid[x_cor][r] for r in range(y_cor_str,y_cor_end+1) if grid[x_cor][r]==0]
                

                if (len(lst_zero)>0):
                    return False
                    
                if (y_cor_str>0):
                    if (grid[x_cor][y_cor_str-1]>0):
                        return False
                
                if (y_cor_end<(len(grid[0])-1)):
                    if (grid[x_cor][y_cor_end+1]>0):
                        return False

                #Right Check
                x_cor=x[0]+l
                y_cor_str=x[1]-((ex_len)/2)
                y_cor_end=x[1]+((ex_len)/2)
                
                
                if (x_cor<0):
                    x_cor=0
                    
                if (x_cor>(len(grid[0])-1)):
                    x_cor=(len(grid[0])-1)

                
                if (y_cor_str<0):
                    y_cor_str=0

                
                if (y_cor_end>(len(grid[0])-1)):
                    y_cor_end=(len(grid[0])-1)
                
                #lst_zero=[r for r in grid[x_cor][y_cor_str:y_cor_end] if r==0]
                lst_zero=[grid[x_cor][r] for r in range(y_cor_str,y_cor_end+1) if grid[x_cor][r]==0]
                
                if (len(lst_zero)>0):
                    return False
                    
                if (y_cor_str>0):
                    if (grid[x_cor][y_cor_str-1]>0):
                        return False
                
                if (y_cor_end<(len(grid[0])-1)):
                    if (grid[x_cor][y_cor_end+1]>0):
                        return False
                    
    if (x[0]+((x[2]+1)/2))<len(grid): 
        x_cor_u=grid[x[0]+((x[2]+1)/2)][x[1]] 
    else:
        x_cor_u=0
    
    if (x[0]-((x[2]+1)/2))>=0:
        x_cor_l=grid[x[0]-((x[2]+1)/2)][x[1]] 
    else:
        x_cor_l=0
    
    if ((x_cor_u==0) & (x_cor_l==0)):
        return True
    else:
        return False
    
def checkHealthy(grid,list_maybe_centroid):
    lst_out=[]
    max_colo=0
    for x in list_maybe_centroid:
        if (checkHealthySub(x,grid)==True):
            if (x[2]==max_colo):
                lst_out=lst_out + [[x[0],x[1]]]                
            elif (x[2]>max_colo):
                max_colo=x[2]
                lst_out=[[x[0],x[1]]]    
    return lst_out        
        
def getCentroid(grid):
    '''
        y0 y1 y2 y3
    x0 
    x1
    x2
    x3
    '''
    list_consec=[]

    for x in range(0,len(grid)):
        for n in range(0,len(grid[x])):
            y=n
            count=0
            while (y<(len(grid[0]))):
                if (  (y>n) & (grid[x][y]==1)  & (grid[x][y-1]==1) ) | ((y==n) & (grid[x][y]==1)):
                    count=count+1
                    y=y+1
                else:
                    y=len(grid[0])
            if (count%2==1) & (count>1):
                reach=[k for k in list_consec if (    (k[0]==x)   &    ( ( k[1]+ (k[2]/2) ) > (n+(count/2)) )   ) ]
                if (len(reach)==0):
                    list_consec=list_consec + [[x,n+(count/2),count]]
      
    return list_consec

def healthy(grid):
    
    list_maybe_centroid=getCentroid(grid)     
    
    out=checkHealthy(grid,list_maybe_centroid)
    
    if (len(out)>=1):
        return out[0]
    elif (len(out)==0):
        return [0,0]

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check(result, answers):
        assert list(result) in answers

        
    check(healthy(((0, 1, 0),
                   (1, 1, 1),
                   (0, 1, 0),)), [[1, 1]])
    check(healthy(((0, 0, 1, 0, 0),
                   (0, 1, 1, 1, 0),
                   (0, 0, 1, 0, 0),
                   (0, 0, 0, 0, 0),
                   (0, 0, 1, 0, 0),)), [[1, 2]])
    check(healthy(((0, 0, 1, 0, 0),
                   (0, 1, 1, 1, 0),
                   (0, 0, 1, 0, 0),
                   (0, 0, 1, 0, 0),
                   (0, 0, 1, 0, 0),)), [[0, 0]])
    x=healthy(((1,1,1,0,0,0,0,0,0,0,0,0,0,0,0),
             (1,1,1,0,0,0,0,0,0,0,0,1,0,0,0),
             (1,1,1,0,0,0,0,0,0,0,1,1,1,0,0),
             (0,0,0,0,0,0,0,0,0,1,1,1,1,1,0),
             (0,0,0,0,1,0,0,0,0,0,1,1,1,0,0),
             (0,0,0,1,1,1,0,0,0,0,0,1,0,0,0),
             (0,0,1,1,1,1,1,0,0,0,0,0,0,0,0),
             (0,0,0,1,1,1,0,0,0,0,0,0,0,0,0),
             (0,0,0,0,1,0,0,0,0,0,0,0,0,0,0),
             (0,0,0,0,0,0,0,0,0,1,0,0,0,0,0),
             (1,1,1,1,1,1,0,0,1,1,1,0,0,0,0),
             (1,1,1,1,1,1,0,1,1,1,1,1,0,0,0),
             (1,1,1,1,1,1,0,0,1,1,1,0,0,0,0),
             (1,1,1,1,1,1,0,0,0,1,0,0,0,0,0),
             (1,1,1,1,1,1,0,0,0,0,0,0,0,0,0)))
    check(healthy(((0,0,0,0,0,1,0,0,0,0,1,1,0,0,0),
                   (0,0,0,0,1,1,1,0,0,0,1,1,1,0,0),
                   (0,0,0,0,0,1,0,0,0,1,1,1,1,1,0),
                   (0,0,0,0,0,0,0,0,1,1,1,1,1,1,1),
                   (0,0,0,1,0,0,0,0,0,1,1,1,1,1,0),
                   (0,0,1,1,1,0,0,0,0,0,1,1,1,0,0),
                   (0,1,1,1,1,1,0,0,0,0,0,1,0,0,0),
                   (1,1,1,1,1,1,1,0,0,0,0,0,0,0,0),
                   (0,1,1,0,1,1,0,0,0,0,1,0,0,0,0),
                   (0,0,1,1,1,0,0,0,0,1,1,1,0,0,0),
                   (0,0,0,1,0,0,0,0,1,1,1,1,1,0,0),
                   (0,0,0,0,0,0,0,1,1,1,1,1,1,1,0),
                   (0,0,0,0,0,0,0,0,1,1,1,1,1,0,0),
                   (0,0,0,0,0,0,0,0,0,1,1,1,0,0,0),
                   (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))),[[1,5]])
    check(healthy(((0, 0, 0, 0, 0, 0, 1, 0),
                   (0, 0, 1, 0, 0, 1, 1, 1),
                   (0, 1, 1, 1, 0, 0, 1, 0),
                   (1, 1, 1, 1, 1, 0, 0, 0),
                   (0, 1, 1, 1, 0, 0, 1, 0),
                   (0, 0, 1, 0, 0, 1, 1, 1),
                   (0, 0, 0, 0, 0, 0, 1, 0),)), [[3, 2]])
    check(healthy(((0, 0, 0, 0, 0, 0, 2, 0),
                   (0, 0, 0, 2, 2, 2, 2, 2),
                   (0, 0, 1, 0, 0, 0, 2, 0),
                   (0, 1, 1, 1, 0, 0, 2, 0),
                   (1, 1, 1, 1, 1, 0, 2, 0),
                   (0, 1, 1, 1, 0, 0, 2, 0),
                   (0, 0, 1, 0, 0, 0, 2, 0),
                   (0, 0, 0, 1, 0, 0, 2, 0),
                   (0, 0, 1, 1, 1, 0, 2, 0),
                   (0, 1, 1, 1, 1, 1, 0, 0),
                   (0, 0, 1, 1, 1, 0, 0, 0),
                   (0, 0, 0, 1, 0, 0, 0, 0),)), [[4, 2], [9, 3]])
