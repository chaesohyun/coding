# N명의 학생의 수학성적
# 평균을 구하고, N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력

if __name__ == '__main__':
    N=int(input())
    number=list(map(int, input().split()))
    avg=round(sum(number)/N)
    min=2147000000
    for idx, x in enumerate(number):
        tmp=abs(x-avg)
        if tmp<min:
            min=tmp
            score=x
            res=idx+1
        elif tmp==min:
            if x>score:
                score=idx-idx+1

    print(avg, res)



