# N개의 돌로 다리를 만든다.
# 한 칸 또는 두 칸 건너뛰며 돌다리를 건넌다.

if __name__ == '__main__':
    n=int(input())
    dy=[0]*(n+1)
    dy[1]=1
    dy[2]=2

    for i in range(3,n+1):
        dy[n]=dy[n-1]+dy[n-2]
    print(dy[n])