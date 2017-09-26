def make_fractal(n):
    if n <= int(N):
        return input_pattern

    next_n = int(n / int(N))

    smaller_pattern = make_fractal(next_n)

    this_pattern = [['.' for px in range(n)] for py in range(n)]

    # 白模様用のパターン
    blank = []
    for b in range(next_n):
        blank.append('.')

    for y in range(int(N)):
        for x in range(int(N)):
            quad_y = y * next_n
            quad_x = x * next_n
            for py in range(next_n):
                if input_pattern[y][x] == '#':
                    this_pattern[py + quad_y][quad_x:quad_x + n] = smaller_pattern[py]
                if input_pattern[y][x] == '.':
                    this_pattern[py + quad_y][quad_x:quad_x + n] = blank

    return this_pattern


def show_fractal(f):
    for w in range(num_squares):
        for h in range(num_squares):
            print(f[w][h], end="")
        print("")


if __name__ == '__main__':
    K = input("input K >> ")
    N = input("input N >> ")
    input_pattern = []
    for a in range(int(N)):
        s_i = list(input("input patterns>>> "))
        input_pattern.append(s_i)

    # 一辺に含まれるマスの数
    num_squares = pow(int(N) ** 2, int(K))

    fractal = make_fractal(num_squares)

    show_fractal(fractal)

    exit(0)
