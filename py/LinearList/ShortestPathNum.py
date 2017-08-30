"""
给定如图所示的无向连通图，假定途中所有边的权值为1。
显然，从源点A到终点T的最短路径有多条，求不同的最短路径数目。
A0┌──┐E4  J8┌──┐N12
  │  │F5  K9│  │
B1├──┼──────┼──┤O13
  │  │      │  │
C2├──┼──────┼──┤P14
  │  │G6 L10│  │
D3└──┘H7 M11└──┘T15
"""
from queue import deque


def shortest_path_num(g):
    step = [0 for _ in range(16)]
    path_num = [0 for _ in range(16)]
    path_num[0] = 1
    q = deque()
    q.append(0)

    while q:
        from_ = q.popleft()
        s = step[from_] + 1
        for i in range(1, 16):
            if g[from_][i] != 1:
                continue
            if step[i] == 0 or s < step[i]:
                step[i] = s
                path_num[i] = path_num[from_]
                q.append(i)
            elif step[i] == s:
                path_num[i] += path_num[from_]
    print(path_num)
    return path_num[-1]


if __name__ == '__main__':
    G = [[0 for _ in range(16)] for _ in range(16)]
    G[0][1] = G[0][4] = 1
    G[1][5] = G[1][0] = G[1][2] = 1
    G[2][1] = G[2][6] = G[2][3] = 1
    G[3][2] = G[3][7] = 1
    G[4][0] = G[4][5] = 1
    G[5][1] = G[5][4] = G[5][6] = G[5][9] = 1
    G[6][2] = G[6][5] = G[6][7] = G[6][10] = 1
    G[7][3] = G[7][6] = 1
    G[8][9] = G[8][12] = 1
    G[9][8] = G[9][13] = G[9][10] = 1
    G[10][9] = G[10][14] = G[10][11] = 1
    G[11][10] = G[11][15] = 1
    G[12][8] = G[12][13] = 1
    G[13][9] = G[13][12] = G[13][14] = 1
    G[14][10] = G[14][13] = G[14][15] = 1
    G[15][11] = G[15][14] = 1

    print(shortest_path_num(G))
