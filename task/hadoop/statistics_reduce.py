#/usr/bin/env python
#-*-coding=utf8-*-

'''
data format
id  level coin  score
'''
import sys

MAX_LEVEL = 100000

# fields in value
LEVEL = 0
COIN = 1
SCORE = 2

def reduce():

  key = None
  pre = None
  records = []
  for line in sys.stdin:
    fields = line.split("\t")
    key = fields[0]
    # 转换为整数
    v = [int(item) for item in fields[1:]]
    if key!= pre and pre != None:
      # id已经改变
      high = -1
      low = MAX_LEVEL
      count = len(records)
      total_coin = 0
      max_score = -1
      for r in records:
        # 总的金钱
        total_coin += r[COIN]

        # 最高等级和最低等级
        if r[LEVEL] > high:
          high = r[LEVEL]
        if r[LEVEL] < low:
          low = r[LEVEL]
       
        # 最高分数
        if r[SCORE] > max_score:
          max_score = r[SCORE]
      
      print("%s\t%d\t%d\t%.2f\t%d" % (pre, high, low, total_coin*1.0/count,max_score))
      pre = key
      records = [v]
    else:
      # 还是同一个id的数据
      records.append(v)
      pre = key

  # 处理最后一批数据
  if pre != None:
    high = -1
    low = MAX_LEVEL
    count = len(records)
    total_coin = 0
    max_score = -1
    for r in records:
      # 总的金钱
      total_coin += r[COIN]

      # 最高等级和最低等级
      if r[LEVEL] > high:
        high = r[LEVEL]
      if r[LEVEL] < low:
        low = r[LEVEL]
     
      # 最高分数
      if r[SCORE] > max_score:
        max_score = r[SCORE]
    
    print("%s\t%d\t%d\t%.2f\t%d" % (pre, high, low, total_coin*1.0/count,max_score))

reduce()
