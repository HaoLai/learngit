# -*- coding:utf-8 -*-
from functools import reduce
def prod(L):
        def chengji(a,b):
            return a*b
        return reduce(chengji,L)

print('3*5*7*9=', prod([3,5,7,9]))
