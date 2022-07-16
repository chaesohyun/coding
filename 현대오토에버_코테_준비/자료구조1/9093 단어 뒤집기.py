# 테스트 케이스 수
import sys

N= int(input())
for i in range(N):
    word=sys.stdin.readline().split()
    for j in word:
        print(j[::-1],end=" ")