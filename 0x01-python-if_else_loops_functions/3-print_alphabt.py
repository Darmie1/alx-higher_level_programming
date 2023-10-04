#!/usr/bin/python3
for letaz in range(ord('a'), ord('z') + 1):
    if chr(letaz) not in 'qe':
        print(chr(letaz), end='')
