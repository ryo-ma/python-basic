# -*- coding: utf-8 -*-
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='shift-jis')
if __name__ == '__main__':
    str = ''
    with open('./address.txt', mode='r', encoding='utf-8') as f:
       str = f.read().replace('\t', ' ')
    with open('./address.txt', mode='w', encoding='utf-8') as f:
        f.write(str)