#-*- coding:gbk -*-
#批量处理编码格式转换
import codecs
import os
path1 = 'E://dir/'
def ReadFile(filePath,encoding="utf-8"):
    with codecs.open(filePath,"r",encoding) as f:
        return f.read()

def WriteFile(filePath,u,encoding="gbk"):
    with codecs.open(filePath,"w",encoding) as f:
        f.write(u)

def UTF8_2_GBK(src,dst):
    content = ReadFile(src,encoding="utf-8")
    WriteFile(dst,content,encoding="gbk")

def GBK_2_UTF8(src,dst):
    content = ReadFile(src,encoding="gbk")
    WriteFile(dst,content,encoding="utf-8")

def dirlist(path):
    filelist =  os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath)
        else:
            if filepath.endswith('.txt'):
                print(filepath)
                #os.rename(filepath, filepath.replace('.txt','.doc'))
                try:
                    UTF8_2_GBK(filepath,filepath)
                except Exception as ex:
                    f=open('error.txt','a')
                    f.write(filepath + '\n')
                    f.close()

dirlist(path1)