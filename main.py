"""
《資料結構Python蔡明志》
可以正確執行。控制台輸出已經格式化。
"""


def main():
    square = [[0] * 5 for i in range(5)]

    square[0][2] = 1

    i, j = 0, 2
    num = 1

    while num < 25:
        i -= 1
        j -= 1

        if i < 0:
            i = 4
        if j < 0:
            j = 4

        if square[i][j] == 0:
            square[i][j] = num + 1
            print("[", i, "][", j, "] =", square[i][j])
            num += 1
        else:
            i += 2
            j += 1

            if i > 4:
                i = i - 5
            if j > 4:
                j = j - 5

            square[i][j] = num + 1
            print("[", i, "][", j, "] =", square[i][j])
            num += 1

    print("")  # 換行

    for m in range(5):
        for n in range(5):
            print('%2s' % square[m][n], end="  ")
        print("\n")

    print("version: e\n")


if __name__ == '__main__':
    main()
