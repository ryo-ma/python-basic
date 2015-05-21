# -*- coding: utf-8 -*-
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if __name__ == '__main__':
    result = []
    with open('./col2.txt', mode='r', encoding='utf-8') as f:
        col2 = f.readlines()
        # 重複排除
        col2_uniq = list(set(col2))
        # 要素とカウント結果をタプル形式でリストを生成
        result = [(x, col2.count(x)) for x in col2_uniq]
        for x in sorted(result, key=lambda x: x[1], reverse=True):
            print(x)