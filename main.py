"""
可以正確執行。但輸出還沒格式化，不夠整齊美觀。
"""


def step():
    pass


def main():
    print("b\n")

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
            print("[", i, "][", j, "]=", square[i][j])
            num += 1
        else:
            i += 2
            j += 1

            if i > 4:
                i = i - 5
            if j > 4:
                j = j - 5

            square[i][j] = num + 1
            print("[", i, "][", j, "]=", square[i][j])
            num += 1

    for m in range(5):
        for n in range(5):
            print(square[m][n], end=" ")
        print("\n")


if __name__ == '__main__':
    main()
