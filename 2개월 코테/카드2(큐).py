# N장의 카드 1~N 번호 / 1번 카드가 제일 위에, N번 카드가 제일 밑에
# 제일 위 카드를 바닥에 버리고, 제일 위 카드를 제일 아래 카드 밑으로 옮긴다.
# 제일 마지막에 남는 카드 구하기

from collections import deque

N=int(input())
arr=deque()
for i in range(1,N+1):
    arr.appendleft(i)

for _ in range(N//2):
    arr.pop()
    arr.appendleft(arr.pop())


if len(arr)>1:
    arr.pop()
print(arr.pop())

