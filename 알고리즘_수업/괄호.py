# T개의 테스트 데이터
# 괄호가 올바른 문자열이면 yes 아니면 no
import sys
T=int(input())
for _ in range(T):
    stack=[]
    x=sys.stdin.readline()
    cnt=0
    for i in range(len(x)):
        if i=='(':
            cnt=cnt+1
        elif i==')':
            cnt=cnt-1
        if cnt<0:
            print("NO")
    if cnt==0:
        print("YES")
    else:
        print("NO")
