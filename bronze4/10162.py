n=int(input())
# 5분, 1분, 10초
# 300초, 60초, 10초

if n%10 !=0 :
    print(-1)
else:
    if n>300:
        a = int(n / 300)
        n=n-int(n/300)*300

    else:
        a=0

    if n<300 and n>60:
        b = int(n / 60)
        n=n-int(n/60)*60
    else:
        b=0

    if n<100 and n>0:
        c=int(n/10)
        n=n-int(n/10)*10
    else:
        c=0

    print(a,b,c)