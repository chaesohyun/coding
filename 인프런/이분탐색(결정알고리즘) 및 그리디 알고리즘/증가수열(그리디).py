# 1~N까지 자연수의 길이 N의 수열 입력
# 왼쪽 맨 끝 또는 오른쪽 맨 끝 수를 가져와 나열하여 가장 긴 증가 수열을 만든다.

# 최대 증가 수열의 길이와 문자열을 출력

N=int(input())
x=list(map(int, input().split()))
ch=''
lt=0
rt=N-1
last=0
tmp=[]
while lt<rt:
    tmp.append((x[lt],'L'))
    tmp.append((x[rt],'R'))
    tmp.sort()
    if tmp[0][0]<last:
        ch+=tmp[1][1]
    else:
        ch+=tmp[0][1]
    last=tmp[0][0]
    print(tmp)
    if tmp[0][1]=='L':
        lt+=1
    elif tmp[0][1]=='R':
        rt-=1
    tmp.clear()

print(ch)
print(len(ch))