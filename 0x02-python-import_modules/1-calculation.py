#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    resultOFadd = add(a, b)
    resultOFsub = sub(a, b)
    resultOFmul = mul(a, b)
    resultOFdiv = div(a, b)
    print("{} + {} = {}".format(a, b, resultOFadd))
    print("{} - {} = {}".format(a, b, resultOFsub))
    print("{} * {} = {}".format(a, b, resultOFmul))
    print("{} / {} = {}".format(a, b, resultOFdiv))
