# -*- coding: utf-8 -*-
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if __name__ == "__main__":
	with open('./address.txt', mode='r', encoding='utf-8') as f_in:
		print(len(f_in.readlines()))
