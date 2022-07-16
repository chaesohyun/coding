# h-24가 24를 넘을 수 있는 반례를 생각해서 h=h%24로 대체하여 정답


h,m,s=map(int, input().split())
a=int(input())
x=s+a

if x>=60:
    m=m+x//60
    s=x-(x//60 *60)
    if m >= 60:
        h=h+m//60
        m=m-(m//60 *60)
    if h>=24:
        h=h%24

else:
    s=x
    if h>=24:
        h=h%24

print(h,m,s)