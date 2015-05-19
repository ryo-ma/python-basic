# -*- coding: utf-8 -*-
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='shift-jis')
if __name__ == '__main__':
    with open('./address.txt', mode='r', encoding='utf-8') as f:
        col2 = [line.split('\t')[1].rstrip() for line in f.readlines()]
        for line in sorted(col2):
            print(line)