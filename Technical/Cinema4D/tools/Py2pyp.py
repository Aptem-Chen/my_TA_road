#! python3
# -*- coding: utf-8 -*-

"""
	此工具用来批量更改.py文件为.pyp文件，
	.pyp文件可以在C4D中使用Source Protector功能来进行加密，生成.pypc文件
	.pypc可以在C4D启动时自动加载

	注：
		生成.pyp文件的范围为该脚本同级目录下所有py文件
		生成.pyp文件的编码为"utf-8"
"""
from os.path import dirname
from os.path import abspath
from os.path import isfile
from os import listdir
from shutil import copyfileobj

def main():
	current_dir = dirname(abspath(__file__))
	files = listdir(current_dir)

	for f in files:
		f = "".join([current_dir, "\\", f])
		if isfile(f) and f.endswith(".py"):
			pyp_file = "".join([f[:-3], ".pyp"])
			with open(f, encoding="utf-8") as src, open(pyp_file, mode="w", encoding="utf-8") as target:
				copyfileobj(src, target)

if __name__ == "__main__":
	main()