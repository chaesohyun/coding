import sys
T=int(input())
input=sys.stdin.readline

for _ in range(T):
    s=input().rstrip()
    stack=[]
    cnt = 0
    for x in s:
        res="YES"
        if x=="(":
            stack.append(x)
        else:
            if len(stack)!=0 and stack[-1]=="(":
                stack.pop()
            else:
                res="NO"
    if len(stack)!=0:
        res="NO"
    print(res)

