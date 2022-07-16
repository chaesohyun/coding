# N개의 랜선을 만들려고 한다.
# K개의 랜선을 가지고 있는데 길이가 제각각이다.
# 모두 N개의 같은 길이 랜선으로 만들려고 한다.
# 정수 단위로 자르면서 최대 랜선의 길이를 구하는 프로그램 작성

K,N=map(int, input().split())
a=[]
for i in range(K):
    a.append(int(input()))

answer=0
left=1
right=max(a)
while left<=right:
    mid=(left+right)//2
    cnt=0
    for i in range(K):
        cnt=cnt+(a[i]//mid)
    if cnt>=N:
        answer=mid
        left=mid+1
    else:
        right=mid-1
print(answer)
