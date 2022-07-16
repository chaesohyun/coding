# 500,100,50,10원 짜리 동전
# N 원이 거슬러줘야할 돈일 때, 동전의 최소 개수 구하기

N=int(input())
cnt=0
while N!=0:
    print(N)

    if N>500:
        N-=500
        cnt+=1
    elif N<500 and N>100:
        N-=100
        cnt+=1
    elif N<100 and N>50:
        N-=50
        cnt+=1
    elif N<50 and N>=10:
        N-=10
        cnt+=1

print(cnt)
