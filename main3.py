# -*- coding: utf-8 -*-
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='shift-jis')

# ファイル書き込み用関数
def file_write(file_name, text):
    with open(file_name, mode='w', encoding='utf-8') as f_out:
        f_out.write(text)

if __name__ == '__main__':
    col1 = []
    col2 = []
    with open('./address.txt', mode='r', encoding='utf-8') as f_in:
        for line in f_in:
            sp = line.split('\t')
            col1.append(sp[0])
            col2.append(sp[1].rstrip())
        file_write('col1.txt', '\n'.join(col1))
        file_write('col2.txt', '\n'.join(col2))
