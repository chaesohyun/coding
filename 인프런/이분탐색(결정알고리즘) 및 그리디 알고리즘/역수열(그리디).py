# 1~n까지의 수를 한번만 사용하여 이루어진 수열
# 각각의 수 앞에 놓인 자신보다 큰 수의 갯수를 수열로 표현한 것을 역수열
# 1 앞에 있는 수 중 1보다 큰 수들의 갯수, 2, 3, ...
# 역수열이 주어졌을 때, 원래의 수열을 출력

N=int(input())
lst=list(map(int, input().split()))

seq=[0]*N

for i in range(N):
    for j in range(N):
        if lst[i]==0 and seq[j]==0:
            seq[j]=i+1
            break
        elif seq[j]==0:
            lst[i]-=1
print(seq)

# 8
# 5 3 4 0 2 1 1 0