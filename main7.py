# -*- coding: utf-8 -*-
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='shift-jis')
if __name__ == '__main__':
    argvs = sys.argv
    with open('./address.txt', mode='r', encoding='utf-8') as f:
        col1 = [line.split('\t')[0] for line in f]
        # 重複排除
        col1_uniq = list(set(col1))
        # データ名/カウント数で出力
        for data in col1_uniq:
            print(data.rstrip(), "/", str(col1.count(data)))