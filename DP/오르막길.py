if __name__ == '__main__':
    N = int(input())
    a = list(map(int, input().split()))

    x = []
    high = []
    for i in range(N):
        if i<(N-1):
            if a[i] < a[i+1]:
                x.append(a[i])
            else:
                x.append(a[i])
                high.append(max(x)-min(x))
                x = []
        else:
            x.append(a[i])
            high.append(max(x) - min(x))

    print(max(high))