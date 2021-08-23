#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
targetPath = str(input('请输入待处理文件夹名称： ')).strip()

targetPath = os.path.join(os.getcwd(),targetPath)
if os.path.exists(targetPath) == False:
    print('[' + targetPath + ']  目标文件夹不存在，任务结束')
    exit()

outputPath = str(input('请输入输出文件夹名称(ReplaceFile)： ')).strip()
if outputPath == '':
    outputPath = 'ReplaceFile'

list = os.listdir(targetPath)
outputPath = os.path.join(os.getcwd(),outputPath)
if os.path.exists(outputPath) == False:
    os.mkdir(outputPath)
for fileName in list:
    with open(os.path.join(outputPath,fileName),'w') as file:
        file.write('')
        file.close()
print('=========== 任务完成 ===========')
print('替换文件位置： ' + outputPath)
print('===============================')



