#android打包纪录

##设置环境

###unity环境

* Unity版本： 4.6.0 f3
* jdk版本：1.8.0 

---

##各渠道个例

###baidu
	导出Android工程，加密，在雄辉那边打包	
###pptv
	导出Android工程，加密，在雄辉那边打包
###360
	先打出一个没有加密的包，然后解压（在脚本encrypt.bat第19行加入pause），
	在解压出来的asset文件夹中加入com文件（在sdk目录中），然后再继续运行脚本。
###酷派
	导出Android工程让雄辉在网上打包。

###Android工程加密过程

* 用Encrypt.exe加密`热血街霸3D\assets\bin\Data\Managed`目录的`Assembly-CSharp.dll`,`Assembly-CSharp-firstpass.dll`,`Runtime.dll`


##热血andriod各渠道测试帐号

###pptv
	账户名： rxjbdiao1 密码：rxjb1234567890  

###360

	账户名： rxjbdiao1 密码：rxjb1234567890  
	账户名： rxjbdiao2 密码：rxjb1234567890  

###酷派
	帐户名： 15618347512 密码：1234567890


