
"""
itertools.isslice()
"""

from itertools import islice

listt=[1,2,3,4,5,6,7,8,9]

# islice(list,start,stop,step) ==>return object like map and filter

result=islice(listt,2,5,2)
result2=list(islice(listt,2,None,2))

print(list(result),'\n',result2)