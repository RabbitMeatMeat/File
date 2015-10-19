#Virtualenv getting started

#Main Advantages
 
	1.you can use different package sets for each project
	2.you can use different python versions for each project


##virtualenvwrapper

###install 
	
	1.pip install virtualenvwrapper
	2.mkdir ~/.virtualenvs
	3.export WORKON_HOME=$HOME/.virtualenvs
	4.source /usr/local/bin/virtualenvwrapper_lazy.sh
		
----
	
	1.安装
	2.3.创建环境变量
	4.执行脚本

###start
1.Create a virtual environment, This creates the venv floder inside WORKON_HOME 
	
	mkvirtualenv venv

2.Work on a virtual environment

	workon venv

3.Deactivating

	deactivate

4.To delete
	
	rmvirtualenv venv

