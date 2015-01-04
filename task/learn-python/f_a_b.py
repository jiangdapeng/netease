#!/usr/bin/python
#-*-coding=utf-8-*-

def f(a,b):
  '''
  f(a,b) = 
    0, if a<0 and b <0
    1, else if a == 0 
    a, else if b == 0
    f(a-1,b) + 2* f(a,b-1) + 1, otherwise
  '''
  if a >= 0 and b >= 0:
    cache = [[None for j in range(b+1)] for i in range(a+1)]
    for j in range(b+1):
      cache[0][j] = 1
    for i in range(1,a+1):
      cache[i][0] = i
  def do_f(a,b):
    #print("a = %d, b=%d" % (a,b))
    if a < 0 or b <0:
      return 0
    if cache[a][b] == None:
      cache[a][b] = do_f(a-1,b) + 2*do_f(a,b-1) + 1
    return cache[a][b]
  return do_f(a,b)

def test():
  for i in range(10):
    for j in range(10):
      print("f(%d,%d)=%d" % (i,j,f(i,j)))

if __name__ == "__main__":
  test()
