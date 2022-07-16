# 문장이 주어졌을 때, 단어 뒤집어 출력
# 단어는 영어로만 이루어짐
import sys
N=int(input())
for _ in range(N):
    stack=[]
    x = sys.stdin.readline().split()

    for i in range(len(x)):
        tmp=[]
        tmp=x[i][::-1]
        stack.append(tmp)
    for i in stack:
        print(i, end=' ')

