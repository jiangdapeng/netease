#/usr/bin/sh

###################################################
# 根据行为统计结果中LOGIN的次数
# 按照0-5为一类，大于5为一类
# 分别输出UID 行为类型  统计次数
###################################################

# the second test log
input=action_count_2.txt
output=user_2_login
cat $input | grep LOGIN | awk '{
if ( $3 + 0 <= 5 ) {
  print $1,$3;
}
}' > $output.let5

cat $input | grep LOGIN | awk '{
if ( $3 + 0 > 5 ) {
  print $1,$3;
}
}' > $output.gt5

#####################################
# 内测三
#
#####################################

input=action_count_3.txt
output=user_3_login
cat $input | grep LOGIN | awk '{
if ( $3 + 0 <= 5 ) {
  print $1,$3;
}
}' > $output.let5

cat $input | grep LOGIN | awk '{
if ( $3 + 0 > 5 ) {
  print $1,$3;
}
}' > $output.gt5

join -o 1.1 -o 2.2 -o 2.3 user_2_login.let5 action_count_2.txt > user_2_login_let5.txt
join -o 1.1 -o 2.2 -o 2.3 user_2_login.gt5 action_count_2.txt > user_2_login_gt5.txt

join -o 1.1 -o 2.2 -o 2.3 user_3_login.let5 action_count_3.txt > user_3_login_let5.txt
join -o 1.1 -o 2.2 -o 2.3 user_3_login.gt5 action_count_3.txt > user_3_login_gt5.txt

rm *.gt5
rm *.let5
