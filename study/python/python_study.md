##库的导入
	
源码安装
	
	下载tar.gz包，解压进入运行setup.py

Pip安装
		
	pip install name



----
----
----
##about Excel

###模块：xlrd, xlwt, xlutils

-----

####xlrd: 读取excel
	
导入库

	import xlrd

打开excel

	data = xlrd.open_workbook("name.xls")

获得表单

	table = data.sheet_by_index(0)
	table = data.sheet_by_name(u"Sheet1")

获取行数

	rows = table.nrows
	cols = table.ncols

读取数据
	
	firstRow = table.row_values(0)
	firstColumn = table.col_values(0)
	
	for i in range(nrows):
		table.row_values(i)
	
	cell = table.cell(0,0).value
	cell = table.row(0)[0].value

####xlwt: 新建excel，并写入

导入库

	import xlwt

新建excel

	wbk = xlwt.Workbook()

创建表单

	sheet = wbk.add_sheet("sheet 1")

写入表单

	sheet.write(0,0,"test text")

保存excel
	
	wbk.save("test.xls")

####xlutils: 修改excel

导入库
	
	from xlrd import open_workbook	
	from xlutils.copy import copy

修改excel

	data = open_workbook("name.xls")
	wb = copy(data)
	ws = wb.get_sheet(0)
	wr.write(0,0,"changed!")
	wb.save("name.xls")




	

