import click
import sys

import os
osPATH =  os.getcwd()
@click.command()
@click.option('--logpath', default=osPATH, help='WEB日志文件目录.')
@click.option('--outpath', default=osPATH, help='分析报告输出目录.')
def getLogPath(logpath,outpath):
    print(logpath)
    print(outpath)
    return True



if __name__ == '__main__':
    getLogPath()