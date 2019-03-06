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
            flag=True
        else:
            flag=False
        return flag
if __name__ == '__main__':
    com=common_util()
    res=com.comstr('555','{"resultCode":"100","resultMsg":"请求成功","data":{"notice":"哈哈哈哈这是公告哈哈哈哈哈","storedValue":"0.00","point":"195","pointTargetUrl":"http://172.25.63.137:9333/goods.html#/goodsIndex","couponsNum":"7","cardNum":"1","cardTargetUrl":"http://172.25.62.54:28888/project/cardBag/#/cardBag","activityList":[],"bursary":{"bigTitle":"我的小金库","subTitle":"个人财富生活","financingInfo":{"financingValue":"106893.00","financingProfit":"0.00","earningsYesterday":"0.01","targetUrl":null},"loanInfo":{"repayLoan":"0.00","bill":"0.00","totalAvlCredit":"0.00","userRepayDay":null,"targetUrl":null}},"loanInfo":{"recommendFlag":false,"title":"WeHotel借贷","detail":[{"bigTitle":"随行借","subTitle":"乐信集团旗下","loanMoney":"50000.00","buttonName":"立即领取","buttonType":1,"labels":["新客送1000积分","借8000元30天免息"],"bottomTitle":null,"flag":0}]},"currentFinancing":{"recommendFlag":true,"title":"WeHotel理财","detail":[{"bigTitle":"理财宝","subTitle":"易方达基金","buttonName":"立即买入","type":"lcb","labels":["免手续费"],"interestRate":"3.33%","bottomTitle":"七日年化","flag":1,"targetUrl":"000359"},{"bigTitle":"桔子理财-爱定存","subTitle":null,"buttonName":null,"type":"jz","labels":["固定锁定期","到期可转出"],"interestRate":"6.03%-8.29%","bottomTitle":"目标年化收益","flag":1,"targetUrl":null}]},"insurance":{"recommendFlag":false,"title":"WeHotel保险","detail":[{"bigTitle":"境外旅游保险","subTitle":"中国人寿","buttonName":"立即投保","type":"zgrs","labels":["全年酒店意外保障","所有意外都保障"],"bottomTitle":"全年酒店意外保险","initMoney":"5.43起"},{"bigTitle":"个人100万重大疾病保险","subTitle":null,"buttonName":"免费领取","type":"insurance_ad","labels":["200万高保额","所有意外均保障"],"bottomTitle":"所有意外都保障","initMoney":null}]},"integralInfo":{"title":"分期专区","subTitle":"首单立减30元","indexUrl":"http://172.25.63.137:9333/?sid=434817#/instalment","productInfos":[{"title":"常售价+【现金+积分】","imgPath":"http://172.25.63.205:8081/images/inn/18GqwS9aBZ","regularPrice":16500,"promotPrice":null,"promotPoints":null,"regularPoints":3667,"price":"165.00","favorPoints":3667,"detailUrl":"http://172.25.63.137:9333/?sid=434817#/goodsDetail?productId=741","priceName":""},{"title":"包邮测试商品","imgPath":"http://10.237.151.62:8080/images/inn/17PDCrfQ9p","regularPrice":210700,"promotPrice":null,"promotPoints":null,"regularPoints":95,"price":"2107.00","favorPoints":95,"detailUrl":"http://172.25.63.137:9333/?sid=434817#/goodsDetail?productId=602","priceName":""},{"title":"【现金+积分】+【积分】","imgPath":"http://172.25.63.205:8081/images/inn/18Gl9ozK8o","regularPrice":16500,"promotPrice":null,"promotPoints":null,"regularPoints":3667,"price":"165.00","favorPoints":3667,"detailUrl":"http://172.25.63.137:9333/?sid=434817#/goodsDetail?productId=738","priceName":""},{"title":"纯积分","imgPath":"http://172.25.63.205:8081/images/inn/192owKXgjc","regularPrice":1000,"promotPrice":null,"promotPoints":null,"regularPoints":98,"price":"10.00","favorPoints":98,"detailUrl":"http://172.25.63.137:9333/?sid=434817#/goodsDetail?productId=739","priceName":"1321235623"},{"title":"常售价+【常售价+积分】A【电子发票商品】","imgPath":"http://172.25.63.205:8081/images/inn/18Gqh6lHyS","regularPrice":16500,"promotPrice":null,"promotPoints":null,"regularPoints":3667,"price":"165.00","favorPoints":3667,"detailUrl":"http://172.25.63.137:9333/?sid=434817#/goodsDetail?productId=740","priceName":"1321321"}]},"blackList":false,"display":true}}')
    print(res)




