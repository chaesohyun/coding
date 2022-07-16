# [,],{,},(,)로 이루어진 문자열이 주어졌을 때, 6가지의 조건을 만족했을 때, '완전한 괄호 문자열'이라고 한다.
# 완전한 문자열일 경우 1, 아닐 경우 0으로 배열로 return
# 6가지의 조건
## 1 [,] 사이에는 [,],{,} 올 수 있음.
## 2. {,} 사이에는 (,) 올 수 있음.
## 3. (,) 사이에는 [,],{,} 못 옴
## 4. 여는 괄호와 닫는 괄호의 짝이 맞아야함.
## 5. { ( ] ) 불가능 - 여는 괄호를 닫는 괄호에서도 우선순위가 존재함.
## 6.
# pars=['{[]()}','({()})','[{}(()]','[{()}}{]','{(})]']
pars=['[(){{()}}]','([])','[()]()[{}]','(}','{}','[]','()']
def solution(pars):
    answer=[]
    for i in pars:
        if len(i)%2!=0:
            continue
        stack = [i[0]]
        for j in range(1,len(i)):
            if (stack[-1]=='(' and i[j]==')') or (stack[-1]=='{' and i[j]=='}') or (stack[-1]=='[' and i[j]==']'):
                if len(stack)!=0:
                    stack.pop()
                else:
                    answer.append(1)
                continue
            if (stack[-1]=='(' and (i[j]=='[' or i[j]=='{')) or (stack[-1]=='{' and i[j]=='['):
                answer.append(0)
                continue
            if j==len(i)-1 and len(stack)!=0:
                answer.append(0)
                continue
            stack.append(i[j])

    return answer
print(solution(pars))
