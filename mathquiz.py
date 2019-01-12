#!/usr/bin/python3

import numpy as np
import random
import sys

seeds= (np.random.rand(300,5)*100+1).astype(np.uint8)
print(seeds.shape)
(x,y)=seeds.shape

def rand_ope(s):
    op=['+','-','*']
    if(len(str(s))==1):
        q=random.randint(0,2)
        return op[q]   
    else:
        q=random.randint(0,1)
    return op[q]

def printQuiz(s):
    return((" %3d %s%3d = "%(s,rand_ope(s),random.randint(1,99))))

for mx in range(1,x):
    vx =seeds[mx]

    t=[printQuiz(st) for st in vx]

    print("%s\n\n\n\n"%("\t".join(t)))
