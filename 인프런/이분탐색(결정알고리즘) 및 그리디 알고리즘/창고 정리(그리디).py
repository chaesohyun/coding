# M회의 높이 조정을 마친 후 가장 높은곳과 가장 낮은 곳의 차이 출력
# 높이 조정은 가장 높은 곳에서 가장 낮은 곳으로 이동하는 것 의미
L=int(input())
arr=list(map(int, input().split()))
M=int(input())

for i in range(M):
    arr.sort()
    # 가장 높은 곳 , 낮은 곳의 인덱스 찾아서 +1, -1 해주기
    arr[0]=arr[0]+1
    arr[L-1]=arr[L-1]-1


print(max(arr)-min(arr))

