# 1부터 9로 채워진 7x7 격자판 위에서
# 가로, 세로 방향으로 길이 5자리 회문수가 몇 개 있는 구하는 프로그램
# 회문수 : 앞, 뒤에서부터 읽으나 같은 수

x=[]
for i in range(7):
    arr=list(map(int, input().split()))
    x.append(arr)

count=0
# 가로
for i in range(7):
    for j in range(3):
        if x[i][j]==x[i][j+4] and x[i][j+1]==x[i][j+3]:
            count=count+1

# 세로
for i in range(7):
    for j in range(3):
        if x[j][i]==x[j+4][i] and x[j][i]==x[j+3][i]:
            count=count+1
print(count)
