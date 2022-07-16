# 중위표기식이 입력되면 후위표기식으로 변환하는 프로그램
# 3+5 가 중위표기식 , 35+가 후위표기식
# 3+5*2 --> 352-*
# 목표 : 후위표기식은 연산자의 우선순위를 컴퓨터가 따로 구분하지 않고 계산이 가능함.

arr=input()
arr=list(map(str, str(arr)))

stack=[]
res=''
for x in arr:
    if x.isdecimal():
        res=res+x
    else:
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res=res+stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and (stack[-1]!='('):
                res=res+stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(':
                res=res+stack.pop()
            stack.pop()
while stack:
    res=res+stack.pop()

print(res)