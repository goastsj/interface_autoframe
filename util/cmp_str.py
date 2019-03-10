#coding=utf-8
import json
class com_str:
    def com_result(self,dict_one,dict_two):
        #isinstance(dict_one,str)
        #dict_twos=json.loads(dict_two)
        #if isinstance(dict_two,'unicode'):
            #dict_one.encode('unicode_escape').decode('string_escape')
        flag=False
        #对字符串进行比较
        if dict_one in dict_two:
            flag=True
        else:
            flag=False
        return flag
