 if __name__ == '__main__':
     solution()

    def solution(rows, columns, queries):
        # 행렬 셋팅
        a = []
        x = 1
        for i in range(columns):
            a.append([])
            for j in range(rows):
                a[i].append(x)
                x = x + 1
        print(a)
        # queries 찾기
        tmp = []
        max_array = []
        for i in range(len(queries)):
            # 직사각형 가로, 높이
            w = queries[i][2] - queries[i][0]
            h = queries[i][3] - queries[i][1]

            # 꼭짓점
            # 행렬에서의 인덱스와 맞추기 위해 1씩 빼준다.
            x = queries[i][0] - 1
            y = queries[i][1] - 1
            z = queries[i][2] - 1
            q = queries[i][3] - 1
            print(x, y, z, q)
            print(a[x][y])
            # print(a[x][y], a[z][q])
            # 윗, 아랫 변
            # for k in range(w):
            #     tmp.append(a[x+k][y])
            #     tmp.append(a[z-k][q])
            # print(tmp)

        return