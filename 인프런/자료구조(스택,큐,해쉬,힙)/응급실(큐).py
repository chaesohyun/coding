# 의사가 한명
# 환자가 도착한 순서대로 진료, 하지만 위험도 높은 환자는 빨리 응급 조치하도록 진료 순서 정함
# 환자 목록에서 제일 앞에 있는 환자목록을 꺼내고, 나머지 대기 목록에서 꺼낸 환자보다 위험도가 높은 환자가
# 존재하면 대기목록 제일 뒤로 다시 넣는다. 그렇지 않으면 진료를 받는다.
# N명 환자 대기목록이 주어지면 M 번째 환자는 몇번째 진료를 받는지 출력

from collections import deque

N,M=map(int,input().split())
tmp=[(pos,val) for pos,val in enumerate(list(map(int, input().split())))]
tmp=deque(tmp)

cnt=0

while True:
    cur=tmp.popleft()
    if any(cur[1]<x[1] for x in tmp):
        tmp.append(cur)
    else:
        cnt=cnt+1
        if M==cur[0]:
            break

print(cnt)