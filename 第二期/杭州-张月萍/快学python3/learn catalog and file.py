# -*- coding: utf-8 -*-
# __author__ = 'Carina'

import os

path = __file__
print("当前文件全路径为： %s" % path)

# 是目录则返回True，否则返回False
print("目录判断：%s" % os.path.isdir(path))

# 判断是否为文件，是则返回True，否则返回False
print("文件判断：%s" % os.path.isfile(path))

# 判断目录或文件是否存在
print("目录/文件存在：%s" % os.path.exists(path))

# 获取文件大小，若目标为目录则返回0
print("文件大小：%s" % os.path.getsize(path))

# 获取文件的绝对路径
print("文件绝对路径：%s" % os.path.abspath(path))

# 将目标路径规范化， 即更规范的路径表达方式，跨平台标识
print("规范化路径：%s" % os.path.normpath(path))

# 将文件名和目录分割
# 若传入的是目录，则将最后的目录名做为文件名分割
print("目录和文件名分割：", end="")
print(os.path.split(path))

# 分离文件名和扩展名
print("文件名和扩展名分离：",end="")
print(os.path.splitext(path))

# 获取文件名
print("文件名为：%s" % os.path.basename(path))

# 获取文件所在目录
print("文件目录为：%s" % os.path.dirname(path))


# 目录遍历
# walk返回值说明：返回值为一个迭代器对象，它的每个部分包含一个元组，即(目录X, [目录X下的目录列表], [目录X下的文件列表])
def walk_for(target_dir):
    # root 当前根目录
    # dirs ：root下的子目录
    # files：root下的子文件
    walk_result = os.walk(target_dir)
    print(type(walk_result))

    for root, dirs, files in walk_result:
        print(type(root),type(dirs),type(files))
        print("-", root)

        # 遍历当前子目录
        for name in dirs:
            print("当前子目录", name)

        # 遍历当前目录的子文件
        for name in files:
            print(" --", name)

if __name__ == "__main__":
    target_dir = os.curdir
    walk_for(target_dir)
