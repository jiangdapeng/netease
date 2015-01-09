#!/usr/bin/python
#-*-coding=utf-8-*-
'''
功能：
  抓取 http://top.baidu.com/buzz.php?p=mmogame 页面
  将top50的游戏的排名、关键字、搜索指数发送到指定邮箱
抓取使用示例：
>> html = crawl_page(url)
>> top50 = extract_content(html)
>> for game in top50:
  print("%s\t%s\t%s" % (game[0],game[1],game[2]))

1 英雄联盟  2558405
2 地下城与勇士  1112334
3 穿越火线  933657
4 魔兽世界  597056
5 梦幻西游  489173
...

'''

import urllib2
import gzip, cStringIO
from bs4 import BeautifulSoup
import time

from mailsender import MailSender

gzip_flag = "\x1f\x8b\x08\x00\x00\x00"
url = "http://top.baidu.com/buzz.php?p=mmogame"
config = {
    "host":"smtp.126.com",
    "user":"jdptest@126.com",
    "pwd":"testjdp",
    "to_list":["jdpdyx@126.com","632592036@qq.com"]
    }

def log(msg):
  print("%s %s" % (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),msg))

def crawl_page(url=url):
  '''
  下载网页，注意这里下载过来很可能是gzip压缩文件
  因此需要解压缩处理
  '''
  html = urllib2.urlopen(url).read()
  # gzip压缩文件
  if html[:6] == gzip_flag:
    html = gzip.GzipFile(fileobj=cStringIO.StringIO(html)).read()
  
  html = html.decode("gbk")
  return html

def extract_content(html):
  '''
  从网页中抽取前50游戏的排名、关键字、搜索指数
  '''
  soup = BeautifulSoup(html)
  table = soup.table
  games = []
  for row in table.findAll('tr')[1:]:
    cols = row.findAll('td')
    try:
      rank = cols[0].span.text
      keywords = cols[1].a.text
      index = cols[-1].span.text
      games.append([rank,keywords,index])
    except Exception, e:
      print(e)
  return games

def format_content(top50):
  table_head = "Rank\tKeywords\tIndex"
  content = "\n".join(["%+2s\t%-10s\t%+10s" % (game[0],game[1],game[2]) for game in top50])
  content = "%s\n%s" % (table_head, content)
  return content


def report_top50():
  '''
  抓取数据并发送到指定邮箱
  '''
  log("downloading")
  top50 = extract_content(crawl_page(url))
  
  log("formating")
  content = format_content(top50)

  timestamp = time.strftime('%Y-%m-%d',time.localtime(time.time())) 
  subject = "%s 百度游戏排行版" % timestamp

  log("sending email to %s" % config['user']) 
  sender = MailSender(config['host'],config['user'],config['pwd'])
  sender.sendmail(config['to_list'],subject,content)
  log("OK") 

if __name__ == "__main__":
  report_top50()
