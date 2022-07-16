for i in range(3):
    a,b,c,d,e,f=map(int, input().split())
    res_a=d-a
    res_b=e-b
    res_c=f-c
    if res_c<0:
        res_c=60+res_c
        res_b=res_b-1
    if res_b<0:
        res_b=60+res_b
        res_a=res_a-1

    print(res_a,res_b,res_c)
