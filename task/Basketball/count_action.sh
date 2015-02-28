#/usr/bin/bash

input=login_count_2.txt-gt5
while read online;
do
  echo $online
done < $input
