#coding utf-8
import requests

class runmethod:
    def get_main(self,url,params=None,header=None):
        if header:
            res=requests.get(url=url,params=params,headers=header)
        else:
            res=requests.get(url=url,params=params)
        return res
    def post_main(self,url,data,header=None):
        if header:
            res=requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()
    def method_main(self,method,url,data=None,headers=None):
        res=None
        if method=="Post":
            res=self.post_main(url,data,headers)
        else:
            res=self.get_main(url,data,headers)
        return res


if __name__ == '__main__':
    methods=runmethod()
    #res=methods.method_main('Post','http://m.imooc.com/passport/user/login','{"uid":"0","service_id":"1","os":"Android","secrectd_code":"ffffffff-b423-2a1e-ffff-ffffcbeed19a","osv":"4.4.4","chan_id":"10102001","screen_size":"768*1366","password":"cluZgkasMLF2LZPexIJMbw==","timestamp":"1507260001708","plat_id":"2","v_id":"5.1.2","token":"50609fd5ffd05c734195d4bbc8dd5092","email":"hQMVwpqKhWbGx5nOcz1fdA==","brand":"ZUK ZUK Z2121","app_id":"1","uuid":""}')
    res=methods.method_main('Get','https://www.baidu.com/')
    print(res)

