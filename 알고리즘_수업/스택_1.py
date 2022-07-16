# 명령의 수 N, N개의 줄에는 명령이 하나씩 주어짐
import sys

N=int(input())
stack=[]
for i in range(N):
    x=sys.stdin.readline().split()
    if x[0]=='push':
        stack.append(x[1])
    elif x[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()

    elif x[0]=='size':
        print(len(stack))
    elif x[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif x[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])