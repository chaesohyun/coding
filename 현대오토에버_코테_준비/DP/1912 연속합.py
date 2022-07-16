# 연속되는 몇 개의 수를 선택하여 모두 더한 값 중 가장 큰 합 구하기
n=int(input())
arr=list(map(int, input().split()))

sum=[arr[0]]


for i in range(len(arr)-1):
    sum.append(max(sum[i]+arr[i+1],arr[i+1]))
print(max(sum))