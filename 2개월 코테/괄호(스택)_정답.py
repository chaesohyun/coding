for _ in range(int(input())):
    stack=[]
    ans="YES"
    for x in input():
        if x=="(":
            stack.append(x)
        else:
            if len(stack)>0:
                stack.pop()
            else:
                ans="NO"
    if len(stack)>0:
        ans="NO"
    print(ans)