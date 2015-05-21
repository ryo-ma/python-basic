# -*- coding: utf-8 -*-
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if __name__ == '__main__':
    col1 =[]
    col2 =[]
    result = ''
    with open('col1.txt', mode='r', encoding='utf-8') as f:
        col1.extend(f.readlines())

    with open('col2.txt', mode='r', encoding='utf-8') as f:
        col2.extend(f.readlines())
    print(col2)
    for s1, s2 in zip(col1, col2):
        result += s1.rstrip() + "\t" + s2

    with open('result1.txt', mode='w', encoding='utf-8') as f:
        f.write(result)
