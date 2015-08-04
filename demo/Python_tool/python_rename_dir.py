#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def ListSdkDirToText(dir, file, faName):
	files = os.listdir(dir)
	for name in files:
		fullname = os.path.join(dir, name)
		if (os.path.isdir(fullname)):
			ListSdkDirToText(fullname, file, name)
		if name=='Plugins' or name=='Plugin':
			file.write(faName+',\n')

def reNameDir(dir):
	files = os.listdir(dir);
	for name in files:
		fullname = os.path.join(dir, name);
		if (os.path.isdir(fullname)):
			reNameDir(fullname)
		if name == 'Plugin':
			os.rename(dir + '\\' + name, dir + '\\' + 'Plugins');
def test():
	dir = os.getcwd()
	reNameDir(dir)

if __name__=='__main__':
	test()
