# 숫자 하나를 주고, m개의 숫자를 제거하여 가장 큰 수를 만들 것
N,m=map(int, input().split())
N=list(map(int, str(N)))

stack=[]
for i in N:
    while m>0 and stack and stack[-1]<i:
        stack.pop()
        m=m-1
    stack.append(i)
if m>0:
    stack=stack[:-m]
res=''.join(map(str,stack))
print(res)