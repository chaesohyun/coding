# M미터의 나무가 필요하다.
# 절단기의 높이 H를 지정한다.
# 자르고 난 후 남은 나무들이 적어도 M미터의 나무이고, 절단기에 설정하는 높이가 최대값을 구하는 프로그램
# 나무의 수 N, 상근이가 가려가려는 나무의 길이 M

N,M=map(int, input().split())
a=list(map(int, input().split()))

left=1
right=max(a)
while left<=right:
    mid=(left+right)//2
    sum=0
    for i in a:
        if i>=mid:
            sum=sum+(i-mid)
    if sum>=M:
        left=mid+1
    else:
        right=mid-1

print(right)