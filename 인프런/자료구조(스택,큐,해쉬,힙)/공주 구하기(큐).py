# 왕자가 N명이 있는데 공주를 구하러 가겠다고 한다.
# 공주를 구하러 갈 왕자를 결정
#  왕자들을 나이 순으로 1~N번까지 차례로 번호를 매긴다.
# 1~N번 시계 방향으로 동그랗게 앉고, 1부터 번호를 외치는데
# 한 왕자가 K를 외치면 그 왕자를 제외하고 다시 1부터 번호를 외친다.
# 마지막 남은 왕자가 공주를 구하러 간다.
from collections import deque
N, K=map(int, input().split())
x=deque([])
for i in range(N):
    x.append(i+1)

while x:
    for i in range(K-1):
        x.append(x.popleft())
    x.popleft()
    if len(x)==1:
        print(x[0])