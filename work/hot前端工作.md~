#hot前端工作

##添加一个新的表的步骤
1. 添加一个Excel表
2. 添加c_table_xxx.proto  

		表头添加pack Table
		参考后端table_xxx.proto
3. 修改TableManager.cs  

		在tableDescList添加表格
		
4. Pack All table To Binary && Compile Table proto File

		详细代码－>TablePacker.cs
5. 在TableManager.cs添加 xxxTableManager

		继承TableManager创建xxxTableManager
		
6. 修改...\trunk\common\table_tools\c_dump_table.sh
		
		添加python命令，用于网页版本打表

##配置xls表测试功能

1. 修改xls表，提交；
2. 前端编译表， Pack All Tables To Binary；
3. 后端编译表， 到10.0.128.3/dev/选择后端服务器打表； 
	


