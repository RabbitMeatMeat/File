##Mission 
	
	只编译修改的proto && table

###当前的机制
	
	1. Complie Table Proto File
		
		编译c_table_*文件和 common_*文件

	2. Complie MSG Proto File
		
		编译command_* && command_user_* 文件
	
	3. Pack All Tables To Binary
		
		1.编译c_table_* && common_*
		2.遍历TableDes列表， Excel -> bytes
	    3.加密	

###修改后机制
	
	记录下每个文件的修改时间，每次读取对比。	
	
	