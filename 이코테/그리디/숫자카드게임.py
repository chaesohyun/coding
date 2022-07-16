# 가장 높은 숫자 한 장 뽑는 게임
# N X M형태 - 뽑고자 하는 카드 해당되는 행 선택 - 가장 낮은 카드 뽑는다.

N,M=map(int, input().split())
tmp=[]
min_res=0
for _ in range(N):
    data=list(map(int, input().split()))
    min_res=min(data)
    tmp.append(min_res)
max_res=max(tmp)
print(max_res)

