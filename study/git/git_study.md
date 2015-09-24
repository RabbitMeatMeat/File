##git study

###设置
	$ git config --global user.name "Your Name"
	$ git config --global user.email "email@example.com"

### new repository
	$ pwd //显示当前目录
	git init

### add file to repository
	git add XX.XX
	git commit -m "XXX" // 提交的说明，可以是任何东西

### 退回到原先版本
	git log //查看历史记录
	git reflog //记录每一次命令
	git reset --hard HEAD^ // 上一个版本
	git reset -- hard XXXXX // xxxxcommit id 退回到标记版本
	
### 文件回退到版本库
	git checkout -- file


### 已经add的文件回退到版本库
 	
	git reset HEAD file
	git checkout -- file
	


### 推送到远程

	本地关联远程库
	git remote add origin git@github.com:rabbithair/XXX.git	
	关联后，使用该命令第一次推送master分支的所有内容；
	git push -u origin master
	接下来推送
	git push origin master



###关于分支

####查看分支
	
	git branch

####创建分支
	git branch name

####切换分支
	git checkout name

####创建+切换分支
	git checkout -b name

####合并某分支到当前分支
	git merge name

####删除分支
	git branch -d name
