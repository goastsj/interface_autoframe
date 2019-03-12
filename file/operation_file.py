#coding-8
import os
import hashlib
class operation_file:
    def __init__(self):
        pass
    #查找重复文件名
    def get_file(self,dirname):
        L1 = []
        for root,dirs,files in os.walk(dirname):
            for file in files:
                #s=os.path.getsize(i_path)
                #L1.append(file)
                if file in L1:
                    print(os.renames(file,os.path.join(root,file)))
                else:
                    L1.append(file)
        print(L1)
    #判定文件是否大于某值,size以字节为单位
    def get_filesize(self,filepath,size):
        s=os.path.getsize(filepath)
        flag=None
        if s>size:
            flag=True
        else:
            flag=False
        return flag

    #获取文件的MD5值
    def md5_file(self,filepath):
        m = hashlib.md5()
        fp=open(filepath)
        rb=800
        m = hashlib.md5()
        with open(filepath,'rb') as fp:
            while True:
                buf=fp.read(rb)
                if not buf:
                    break
                else:
                    m.update(fp.read(rb))
            return m.hexdigest()

if __name__ == '__main__':
    op_file=operation_file()
    res=op_file.get_file(r"E:\项目资料\储值充值\礼享会微信接口文档")
    #op_file.md5_file(r"E:\项目资料\储值充值\礼享会微信接口文档\对接微信公众平台接口文档-20181208.docx")
