# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 00:21:04 2016

@author: ssits
"""

def cipher(mtx_grille,mtx_pwd):
    list_X=[i for i, j in enumerate(mtx_grille) if j == 'X']
    list_pwd=[mtx_pwd[j] for i, j in enumerate(list_X)]
    return ''.join(list_pwd)
    

def recall_password(cipher_grille, ciphered_password):
    ciphered_txt=""
    
    mtx_grille = [[a1 for a1 in list(cipher_grille[0])],[a2 for a2 in list(cipher_grille[1])],[a3 for a3 in list(cipher_grille[2])],[a4 for a4 in list(cipher_grille[3])]]     
    mtx_pwd = [[a1 for a1 in list(ciphered_password[0])],[a2 for a2 in list(ciphered_password[1])],[a3 for a3 in list(ciphered_password[2])],[a4 for a4 in list(ciphered_password[3])]]     
    
    for x in range(0,4):
        
        for i in range(0,4):
            grille_round=mtx_grille[i]
            pwd_round=mtx_pwd[i]
            ciphered_txt = ciphered_txt + cipher(grille_round,pwd_round)
            
        mtx_grille = [[row[0] for row in reversed(mtx_grille)],[row[1] for row in reversed(mtx_grille)],[row[2] for row in reversed(mtx_grille)],[row[3] for row in reversed(mtx_grille)]]     

    
    return ciphered_txt


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'