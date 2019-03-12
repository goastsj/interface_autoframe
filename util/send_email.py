#coding=utf-8
from email.mime.text import MIMEText
from smtplib import SMTP
from email.header import Header
class send_email:
    '''
    1.连接到邮件服务器
    2.登录邮箱
    3.发送邮件
    '''
    def send_email(self,from_to,reserve_to,message):
        host="smtp.qq.com"
        port = 25
        uesr="1037905204@qq.com"
        passwords="qfpktnzgxcffbehb"
        email_server=SMTP(host,port)
        email_login=email_server.login(uesr,passwords)
        email_server.sendmail(from_to,reserve_to,message.as_string())
        email_server.quit()
    def send_text(self,send_who,to_who,sub,texts):
        messages=MIMEText(texts,'plain','utf-8')
        #uesrs = ["1037905204@qq.com1"]
        messages['From']=send_who
        messages['To']=to_who
        messages['Subject']=sub
        return messages
if __name__ == '__main__':
    send_who='1037905204@qq.com'
    to_who='13750047512@163.com'
    texts="这是一个测试邮件"
    sub="接口自动化测试报告"
    se=send_email()
    mess=se.send_text(send_who,to_who,sub,texts)
    re=se.send_email(send_who,to_who,mess)
    print(type(re))