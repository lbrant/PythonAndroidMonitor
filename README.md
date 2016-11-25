# PythonAndroidMonitor #

This tool is used to monitor device memory info base on adb command and python, data is saved to CSV file, and can be used to make Excel chart.

###Note:
 1. adb should be added in environment path;
 2. python code is based Python3.x;
 3. Excel chart may need adjust depend on data size. 
 4. Example chart:
 ![](http://i.imgur.com/Jz83hED.png)

###User guide:
 1. Connect your mobile phone to pc;
 2. Run the script, and input process you will monitor, for example: com.zebra.carcloud.gate;
	> Please input the process name:
 3. Input catch interval in seconds, such as 10, too small is meaningless;
	> Please input the catch interval(second, value should >= 10):
 4. When the script run for while, the data is saved at:
    > %USER%\PythonAndroidMonitor directory

	On windows, it's C:\Users\%user name%\Desktop\PythonAndroidMonitor\%datetime%, the directory name is last run datetime.
 5. Open the folder,mem_history.txt record detail info and mem_abstract.CSV record abstract info.
 ![](http://i.imgur.com/42s2CKn.png)
mem_abstract.CSV colums: PID,ProcessName,Datetime,PSS(KB)
![](http://i.imgur.com/Rw1oFqA.png)
 6. Open 内存占用情况.xlsx.
 7. In Sheet1, Click '数据' in tool bar，and then click '全部刷新'，and select the CSV file created, wait till data changed, you can find chart in Sheet2.
 ![](http://i.imgur.com/6ZAZ38b.png)
 Sometime, you can adjust chart style depends on data size.
