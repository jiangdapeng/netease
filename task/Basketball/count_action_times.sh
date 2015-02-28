#/usr/bin/sh

###################################################
# 根据日志中的行为标记，统计每个ID的各种行为的次数
# 并按照如下格式输出：
# ID 行为类型 统计次数 
###################################################

# the second test log
input=data/*.log
output=action_count_2.txt

echo "processing test 2 log data"
###########################################
# match的目的是去除不符合格式的数据
# 因为在数据处理过程总发现若干条异常数据
###########################################
cat $input | awk '
{
  if ( match($5,/^uid/) !=0 ){
    count[$5,$4]++;
  }
}
END{
  for(user in count) {
    split(user,idx,SUBSEP);
    print idx[1],idx[2],count[user];
  }
}' | sort -k1,2 > $output

echo "test 2 log done"


input=data/*.txt
output=action_count_3.txt

echo "processing test 3 log data"
###########################################
# match的目的是去除不符合格式的数据
# 因为在数据处理过程总发现若干条异常数据
###########################################
cat $input | awk '
{
  if ( match($5,/^uid/) !=0 ){
    count[$5,$4]++;
  }
}
END{
  for(user in count) {
    split(user,idx,SUBSEP);
    print idx[1],idx[2],count[user];
  }
}' | sort -k1,2 > $output 

echo "test 3 log done"
