# 9x9 보드에서 3x3 보드에 1~9까지 숫자가 중복 없이 나타나게 채우기
# 완성된 스도쿠가 주어질 때, 정확하게 풀었으면 YES, 아니면 NO를 출력
x=[]
for i in range(9):
    arr=list(map(int, input().split()))
    x.append(arr)

# 각 행
count=0
for i in range(9):
    tmp=0
    for j in range(9):
        tmp=tmp+x[i][j]
    if tmp==sum([1,2,3,4,5,6,7,8,9]):
        count=count+1
# 각 열
for i in range(9):
    tmp=0
    for j in range(9):
        tmp=tmp+x[j][i]
    if tmp==sum([1,2,3,4,5,6,7,8,9]):
        count=count+1
# 3x3
for k in range(3):
    for m in range(3):
        tmp=0
        for i in range(3*k,3*k+3):
            for j in range(3*m,3*m+3):
                tmp=tmp+x[i][j]
        if tmp == sum([1, 2, 3, 4, 5, 6, 7, 8, 9]):
            count = count + 1


if count==27:
    print("YES")
else:
    print("NO")