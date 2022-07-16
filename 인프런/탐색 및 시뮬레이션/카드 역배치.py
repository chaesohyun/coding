# 1~20 숫자가 적힌 20 장의 카드가 있는데 오름차순으로 놓여있다.
# 구간 [a,b]가 주어지면 a부터 b까지 카드를 현재의 역순으로 놓는다.
# 10개의 줄에 걸쳐 10개의 구간이 입력되면 1부터 20까지 오름차순 카드들을 10개의 구간 순서대로 뒤집여졌을 때 배치를 출력
x=[]
for i in range(1,21):
    x.append(i)

for i in range(10):
    a,b=map(int, input().split())
    for j in range((b-a+1) //2 ):
        tmp=x[a-1+j]
        x[a-1+j]=x[b-1-j]
        x[b-1-j]=tmp
print(x)
