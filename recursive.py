# -*- coding: utf-8 -*-
"""
Created on Wed May 19 08:18:35 2021

@author: maxic

to try fibonachi and gcd 
"""

def myfibo(i):
    fiboold =  1
    fibolast = 1
    fibonew =  1
    while i >=2:
        fibonew = fiboold + fibolast
        fiboold = fibolast
        fibolast = fibonew
        i -= 1
    return fibonew
 
    
def mygcd(i,j):
    import math
    x = [i,j]
    r = []
    
    while  i*j != 0:
        if i >= j:
            x.append(math.floor(i/j))
            i = i % j
            r.append(i)
            
        else:
            x.append(math.floor(j/i))            
            j = j % i            
            r.append(j)
    return i+j, x, r

def gcd(i,j):
    if j == 0:
        return i
    else:
        return gcd (j, i%j)
    
def mgcd(i,j):
    if j == 0:
        return i
    elif i >=j :
        return mgcd(j, i%j)
    else:
        return mgcd(i, j%i)
    
    
# import random
# i = 10
# while i > 0:
#      a = random.randint(1,100)   
#      b = random.randint(1,100)   
#      i -= 1
#      print (a,b,mygcd(a,b))
     

x = ['jocleyn', 'justin', 'selena']
r = 3
x.append(3)
x.append(r)
print(x)
