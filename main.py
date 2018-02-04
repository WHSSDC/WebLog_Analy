import click
import sys
import InitData.InputFileInfo
import os
osPATH =  os.getcwd()

# CLI功能实现，所有输出经过过滤后传输到各实例中
# 还没有添加logging 记录器进行异常处理
@click.command()
@click.option('--logpath', default=osPATH, help='WEB日志文件目录,默认值是当前目录.')
@click.option('--outpath', default=osPATH, help='分析报告输出目录,默认值是当前目录.')
def getLogPath(logpath,outpath):
    if logpath is None and outpath is None :
        raise ValueError
    # 这里会向 InputFileInfo 类传参数用于帮助初始化

if __name__ == '__main__':
    getLogPath()