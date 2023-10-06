#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    Ttalsum = sum(int(arg) for arg in args)
    print(Ttalsum)
