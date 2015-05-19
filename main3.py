# -*- coding: utf-8 -*-
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='shift-jis')

def file_write(file_name, text):
    with open(file_name, mode='w', encoding='utf-8') as f:
        f.write(text)


if __name__ == '__main__':
    col1 = []
    col2 = []
    with open('./address.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            sp = line.split('\t')
            col1.append(sp[0])
            col2.append(sp[1].rstrip())
        file_write('col1.txt', '\n'.join(col1))
        file_write('col2.txt', '\n'.join(col2))