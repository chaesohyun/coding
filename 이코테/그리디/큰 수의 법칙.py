N,M,K=map(int, input().split())
data=list(map(int, input().split()))

result=0

# (제일 큰 수로 연속 - 그다음 큰수) 이런식으로 반복되기 때문에 가장 큰수와 그다음으로 큰수만 필요함.

data.sort()
first=data[-1]
second=data[-2]

result=0
while M!=0:
    for _ in range(K):
        result+=first
        M-=1
        if M==0:
            break
    if M==0:
        break
    result+=second
    M-=1
print(result)

