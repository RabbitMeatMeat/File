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

def test():
	dir = os.getcwd()
	outfile = "name.txt"

	file = open(outfile, "w")
	if not file:
		print("cannot open the file %s for writing" % outfile)
	ListSdkDirToText(dir, file,'')

if __name__=='__main__':
	test()