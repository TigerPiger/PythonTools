import os
import re
from os.path import isfile, join, splitext
from os import walk

rootPath = "E:\\Linux教学视频\\Linux视频教程课件与笔记\\"

dir_list = os.listdir(rootPath)


filelist = []

def getNumbers(s):
    pattern = re.compile(r'(\d+)')

    pieces = pattern.split(s)
    pieces[1::2] = map(int, pieces[1::2])

    return pieces

# 使用os.walk()函数获取当前文件夹下所有的markdown文件
for (dirpath, dirnames, filenames) in walk(rootPath):
    # 筛选处.md后缀的markdown文件
    markdown_filenames = [join(dirpath, md) for md in filenames if splitext(md)[1] == ".md"]
    filelist.extend(markdown_filenames)

filelist.sort(key=getNumbers)
print(filelist)

# 合并所有的markdown文件
contents = []
for filepath in filelist:
    with open(filepath, encoding='utf-8') as file:
        contents.extend(file.read() + "\n")


with open(join(rootPath, "课堂笔记.md"), mode = 'x', encoding='utf-8') as file:
    file.writelines(contents)


# # 遍历各文件夹
# for dir in dir_list:
#     dir_path = join(rootPath, dir)
#     # 检查是否为文件夹
#     if os.path.isdir(dir_path):
#         file_list = [file for file in os.listdir(dir_path) if isfile(join(dir_path, file))]
#         for file in file_list:
#             file_path = join(rootPath, dir)
#             print("File:" + file + '\t')
#         print("Current Dir: " + dir + '\n')
