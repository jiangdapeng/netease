#/usr/bin/env python
#-*-coding=utf8-*-
import sys

def main():

  for line in sys.stdin:
    fields = line.split()
    print("%s\t%s" % (fields[0], "\t".join(fields[1:])))

main()
