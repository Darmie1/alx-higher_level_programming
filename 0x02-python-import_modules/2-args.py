#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    numbaofargs = len(args)
    if numbaofargs == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(numbaofargs, 's' if numbaofargs > 1 else ''))
        for i, arg in enumerate(args, 1):
            print("{}: {}".format(i, arg))
