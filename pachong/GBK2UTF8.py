import codecs

def ReadFile(filePath, encoding="GBK"):
    with codecs.open(filePath, "r", encoding) as f:
        return f.read()

def WriteFile(filePath, u, encoding="utf-8"):
    with codecs.open(filePath, "w", encoding) as f:
        f.write(u)

#def GBK_2_UTF8(src, dst):
# content = ReadFile("D:/mathwork/python/new/train/newpos.txt", encoding="GBK")
# WriteFile("D:/mathwork/python/new/train/newpos1.txt", content, encoding="utf-8")
content1 = ReadFile("D:/mathwork/python/new/train/newneg.txt", encoding="GBK")
WriteFile("D:/mathwork/python/new/train/newneg1.txt", content1, encoding="utf-8")