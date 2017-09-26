import math


# フィボナッチ数列出力用


def get_fib_seq(num):
    if num == 0:
        return [0]
    if num == 1:
        return [0, 1]

    num_seq = [0, 1]
    fn_2 = 0
    fn_1 = 1
    for n in range(2, num + 1):
        num_seq.append(fn_2 + fn_1)
        fn_2, fn_1 = fn_1, fn_2 + fn_1

    return num_seq


# フィボナッチの単項出力用


def get_fib_num(num):
    return int((math.pow((1 + math.sqrt(5)) / 2, num) - math.pow((-1 - math.sqrt(5)) / 2, -num)) / math.sqrt(5))


if __name__ == '__main__':
    print("Fibonacci sequence (0=>20) is")
    print(get_fib_seq(20))
    print("Fibonacci number (50) is")
    print(get_fib_num(50))
    exit(0)
