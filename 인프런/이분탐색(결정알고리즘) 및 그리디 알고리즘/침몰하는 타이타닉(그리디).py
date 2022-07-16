# N명의 승객이 구명보트에 2명 이하로만 탈 수 있고, M kg이하로 제한
# N명의 승객 몸무게가 주어졌을 때, 모두 탈출하기 위한 구명보트의 최소 갯수는

N,M=map(int,input().split())
x=list(map(int, input().split()))
x.sort()

cnt=0
while x:
    if x[0] + x[-1] < M:
        cnt = cnt + 1
        x.remove(x[0])
        x.remove(x[-1])
        break
    else:
        cnt = cnt + 1
        x.remove(x[-1])
print(cnt)

# 5 140
# 90 50 70 100 60