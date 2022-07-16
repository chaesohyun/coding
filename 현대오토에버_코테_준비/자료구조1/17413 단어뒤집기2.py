import sys
s=sys.stdin.readline()
stack=[]
result=[]
tag_bool=False
for i in list(s):
    if i=='<':
        result.append(i)
        tag_bool=True
    elif tag_bool==True and 

