import sys
N=int(input())
x=[]
for _ in range(N):
    x.append(int(input()))
stack=[]
ans=[]
m=0
for a in x:
    if a>m:
        while a>m:
            m+=1
            stack.append(m)
            ans+=['+']
        stack.pop()
        ans+=['-']
    else:
        if stack[-1]!=a:
            print("NO")
            sys.exit(0)
        stack.pop()
        ans+=['-']

print('\n'.join(ans)+'\n')

