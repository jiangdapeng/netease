#!/usr/bin/python
#-*-coding=utf-8-*-

def pyramid(n):
  most = 2*n - 1
  for i in range(1,n+1):
    star = 2*i - 1
    space = n - i
    print(" "*space + "*"*star)

def test():
  pyramid(3)
  pyramid(4)
  pyramid(5)

if __name__ == "__main__":
  test()
