#/usr/bin/sh

###################################################
# 根据日志中的LOGIN标记，统计每个ID的登录次数
# 并按照登录次数0-5、大于5两类输出
###################################################

# the second test log
input=data/*.log
output=login_count_2.txt
cat $input |  grep LOGIN | awk '{count[$5]++}END{for(name in count)print name,count[name]}' | sort -k2 -nr > $output

cat $output | awk '{
  if ( $2 + 0 > 5 ) {
    print $0;
  }
}' > $output-gt5

cat $output | awk '{
  if ( $2 + 0 <= 5 ) {
    print $0;
  }
}' > $output-let5


# the third test log
input=data/*.txt
output=login_count_3.txt
cat $input |  grep LOGIN | awk '{count[$5]++}END{for(name in count)print name,count[name]}' | sort -k2 -nr > $output

cat $output | awk '{
  if ( $2 + 0 > 5 ) {
    print $0;
  }
}' > $output-gt5

cat $output | awk '{
  if ( $2 + 0 <= 5 ) {
    print $0;
  }
}' > $output-let5
