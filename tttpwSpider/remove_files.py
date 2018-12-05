import os
import shutil

def isAllChinese(s):    #检测是否全部为中文
    for c in s:
        if not('\u4e00' <= c <= '\u9fa5'):
            return False
    return True


file_dir = os.getcwd()
for root, dirs, files in os.walk(file_dir):
    print(root) #当前目录路径
    print(dirs) #当前路径下所有子目录
    print(files) #当前路径下所有非目录子文件

    if dirs:
        for dir in dirs:
            print(dir)
            res = isAllChinese(dir)
            if res:
                print("删除")
                print(root + "/" + dir)
                shutil.rmtree(root + "/" + dir)
