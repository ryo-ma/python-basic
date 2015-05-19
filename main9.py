# -*- coding: utf-8 -*-
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='shift-jis')
if __name__ == '__main__':
    with open('./address.txt', mode='r', encoding='utf-8') as f:
        for line in sorted(f.readlines(),key=lambda x:x.split('\t')[1] + x.split('\t')[0], reverse=True):
           print(line.rstrip())