import sys
from collections import deque
T = int(sys.stdin.readline())
for tc in range(T):
    N, M = map(int, sys.stdin.readline().split())
    Q = deque(map(int, sys.stdin.readline().split()))
    for i in range(len(Q)):
        for j in range(i+1, len(Q)+1):
            if Q[i] < Q[j]:
                