# 후위연산식이 주어지면 연산한 결과를 출력하는 프로그램
arr=input()
arr=list(map(str,str(arr)))

left=0
right=0
res=0
stack=[]
for x in arr:
    if x=='*' or x=='/' or x=='-' or x=='+':
        right=int(stack.pop())
        left=int(stack.pop())
        if x=='*':
            res=left*right
        elif x=='/':
            res=left/right
        elif x=='+':
            res=left+right
        elif x=='-':
            res=left-right
        stack.append(res)
    else:
        stack.append(x)
print(res)