def mapping(m, num):
    if num == 1:
        for i in range(3, 10):
            m[i][3] = 2
        for i in range(11, 18):
            m[i][3] = 2
        for i in range(7, 14):
            m[i][5] = 2
        for i in range(7, 10):
            m[i][7] = 2
        for i in range(11, 14):
            m[i][7] = 2
        for i in range(9, 12):
            m[i][9] = 2
        for i in range(7, 10):
            m[i][13] = 2
        for i in range(11, 14):
            m[i][13] = 2
        for i in range(7, 14):
            m[i][15] = 2
        for i in range(3, 10):
            m[i][17] = 2
        for i in range(11, 18):
            m[i][17] = 2

        for i in range(5, 8):
            m[3][i] = 2
        for i in range(9, 12):
            m[3][i] = 2
        for i in range(13, 16):
            m[3][i] = 2
        for i in range(5, 10):
            m[5][i] = 2
        for i in range(11, 16):
            m[5][i] = 2
        for i in range(9, 12):
            m[7][i] = 2
        for i in range(10, 12):
            m[9][i] = 2
        for i in range(10, 12):
            m[11][i] = 2
        for i in range(9, 12):
            m[13][i] = 2
        for i in range(5, 10):
            m[15][i] = 2
        for i in range(11, 16):
            m[15][i] = 2
        for i in range(5, 8):
            m[17][i] = 2
        for i in range(9, 12):
            m[17][i] = 2
        for i in range(13, 16):
            m[17][i] = 2
        return m

    if num == 2:
        return m
