import sys

N=int(input())
for i in range(N):
    s=sys.stdin.readline().split()
    stack=[]
    for j in s:
        if j=='(':
            stack.append(j)
        elif j==')':
            if len(stack)!=0:
                stack.pop()
