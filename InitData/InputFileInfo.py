# coding=utf-8
import  time
import os
# 获取当前路径，若日志路径为空，则自动搜索目录下的WebLog目录；
PATH =  os.getcwd()


# 日志分析类
class InputFileInfo :
    # 存储对象名等于文件名+时间戳

    def __init__(self,logPath,):
        if logPath is None :
            logPath = PATH
    # 获取名字
    def setJobName(self):
        jobName = None
        try:
            pass
        except :
            pass
        
        return jobName
    def checkFilePath(self):
        pass
    def checkReadPermissions(self):
        pass
    def checkWritePermissions(self):
        pass
