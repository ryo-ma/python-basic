# -*- coding: utf-8 -*-
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='shift-jis')
if __name__ == '__main__':
    result = []
    with open('./col2.txt', mode='r', encoding='utf-8') as f:
        col2 = f.readlines()
        # print(col2)
        col2_uniq = list(set(col2))
        # 処理時間がかかる
        result = [(x, col2.count(x)) for x in col2_uniq]
        for x in sorted(result, key=lambda x: x[1], reverse=True):
            print(x)