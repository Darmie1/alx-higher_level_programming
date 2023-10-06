#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    no_fargs = len(args)
    if no_fargs == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(no_fargs, 's' if no_fargs > 1 else ''))
        for i, arg in enumerate(args, 1):
            print("{}: {}".format(i, arg))
