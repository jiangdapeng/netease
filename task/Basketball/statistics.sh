#/usr/bin/sh

###################################################
# 分别统计登录次数为0-5、大于5两类用户各个行为指标的平均值
# 
# 
###################################################

for log in {2,3}
do
  # the second test log
  input1=user_${log}_login_let5.txt
  output1=user_${log}_login_let5.sta
  
  cat $input1 | awk '
  {
    count[$2]+= $3
    n[$2]++;
  }
  END{
    print "行为类型 累计次数  行为人数  平均次数";
    for ( action in count ) {
      print action,count[action],n[action],count[action]/n[action];
    }
  }
  '
  
  input2=user_${log}_login_gt5.txt
  output2=user_${log}_login_gt5.sta
  
  cat $input2 | awk '
  {
    count[$2]+= $3
    n[$2]++;
  }
  END{
    print "行为类型 累计次数  行为人数  平均次数";
    for ( action in count ) {
      print action,count[action],n[action],count[action]/n[action];
    }
  }
  '
done
