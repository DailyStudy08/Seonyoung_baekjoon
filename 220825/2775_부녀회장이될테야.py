# a층 b호에 살려면 (a-1)층 1~b호 사람 수의 합만큼 사람들을 데려와 살아야함
# 비어있는 집 없을 대 k층 n호에 몇명이 살고있는지 출력
# 0층부터 있고, 각 층에는 1호부터 있음
# 0층의 i호에는 i명이 산다.


from re import A


T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    apart = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(k+1):
        for j in range(1, n+1):
            if i == 0:
                apart[i][j] = i
            else:
                apart[i][j] = apart[i][j-1] + apart[i-1][j]
    print(apart)
    print(apart[k][n])         