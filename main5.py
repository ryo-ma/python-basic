# -*- coding: utf-8 -*-
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='shift-jis')
if __name__ == '__main__':
    argvs = sys.argv
    # コマンドライン引数が正しいか
    if len(argvs) < 2:
        print('引数が足りません')
        sys.exit(0)
    with open('./address.txt', mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        index = int(argvs[1])
        for x in lines[:index]:
            print(x.rstrip())
