#!/usr/bin/python
#-*-coding=utf-8-*-

'''
发送txt文本邮件
'''
import smtplib  
from email.mime.text import MIMEText  
mailto_list=["jdpdyx@126.com"] 
mail_host="smtp.126.com"  #设置服务器
mail_user="jiajj2012@126.com"    #用户名
mail_pass="jiajunjun!"   #口令 
mail_postfix="126.com"  #发件箱的后缀

class MailSender():
  def __init__(self,host,user=None,pwd=None):
    self.host = host
    self.user = user
    self.pwd = pwd

  def sendmail(self, to_list,sub,content):
    msg = MIMEText(content,_subtype='plain',_charset="UTF-8")
    msg['Subject'] = sub
    msg['From'] = self.user
    msg['To'] = ";".join(to_list)
    try:  
      server = smtplib.SMTP(self.host)  
      server.login(self.user,self.pwd)  
      server.sendmail(self.user, to_list, msg.as_string())  
      server.close()  
    except Exception, e:  
      print(str(e))
  
if __name__ == '__main__':  
  sender = MailSender(mail_host,mail_user,mail_pass)
  sender.sendmail(mailto_list,"hello","hello world！")
  sender.sendmail(mailto_list,"I love you","dapeng jiajunjun love you")
  print "发送成功"  
