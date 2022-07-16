# N개의 수열의 i번째 수부터 j번째 수까지의 합이 M이 되는 경우의 수 구하기
N,M=map(int,input().split())
arr=list(map(int, input().split()))

count=0
for i in range(N+1):
    hap=0
    for j in range(N+1):
        hap=sum(arr[i:j])
        if hap==M:
            print(arr[i:j])
            count=count+1
            break
print(count)
