# N개의 숫자가 입력됨
# N개의 수를 오름차순으로 정렬
# N개의 수 중 한 개의 수인 M이 주어지면 이분 검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램


if __name__ == '__main__':
    N,M=map(int,input().split())
    array=list(map(int, input().split()))
    array.sort()
    print(array)
    # 이분 탐색
    left=0
    right=N-1
    pivot = (left + right) // 2
    while left<=right:
        pivot=(left+right)//2
        if array[pivot]==M:
            print(pivot+1)
            break
        elif array[pivot]>M:
            right=pivot
        elif array[pivot]<M:
            left=pivot



