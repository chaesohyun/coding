# N이 1이 될 때까지 두 과정 중 하나를 반복적 수행
# N-1 OR N//K
# 최소 실행 횟수 구하기
# _------>>> 최대한 많이 나누기

N,K=map(int, input().split())
cnt=0
while N!=1:
    if N%K==0:
        N/=K
    else:
        N-=1
    cnt+=1
print(cnt)