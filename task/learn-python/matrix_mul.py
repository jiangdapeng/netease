#!/usr/bin/python
#-*-coding=utf-8-*-
'''
矩阵A与矩阵B的乘积
矩阵存分别存放在a.txt和b.txt
'''

import sys
import numpy as np
def matrix_mul(a,b):
  return list(np.array(a).dot(np.array(b)))

def save_matrix(m,filename):
  with open(filename,"w") as out:
    for row in m:
      out.write(" ".join([str(n) for n in row]))
      out.write("\n")

def matrix_file_mul(afile,bfile,result_file):
  a = []
  for line in open(afile):
    a.append([float(n) for n in line.strip().split()])

  b = []
  for line in open(bfile):
    b.append([float(n) for n in line.strip().split()])
  
  result = matrix_mul(a,b)
  save_matrix(result,result_file)

if __name__ == "__main__":
  if len(sys.argv) != 4:
    print('''
    usage:
      python matrix_mul.py a.txt b.txt result.txt
    ''')
  else:
    a = sys.argv[1]
    b = sys.argv[2]
    r = sys.argv[3]
    matrix_file_mul(a,b,r)
