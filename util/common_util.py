#coding=utf-8
import json
class common_util:
    def comstr(self,str_one,str_two):
        #if isinstance(str_one,str):
            #str_one=json.loads(str_one)
       # if isinstance(str_two,str):
            #str_two=json.loads(str_two)
        flag=None
        if str_one in str_two:
            flag=true
        else:
            flag=false
        return flag


