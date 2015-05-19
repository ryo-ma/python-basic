# -*- coding: utf-8 -*-
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='shift-jis')
if __name__ == '__main__':
    argvs = sys.argv
    with open('./address.txt', mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        index = int(argvs[1])
        print(lines[:index])