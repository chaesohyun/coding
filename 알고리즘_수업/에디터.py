import sys

s = sys.stdin.readline()
x=list(s.strip())
N=int(input())

stack=[]
for i in range(N):

    if s[0]=='P':
        x.append(s[1])
    elif s[0]=='L':
        stack.append(x[-1])
        x.pop()
    elif s[0]=='D':
        x.append(stack[-1])
        stack.pop()
    elif s[0]=='B':
        x.pop()

print(''.join(x+stack))