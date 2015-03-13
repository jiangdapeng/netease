#/usr/bin/env bash
input_file=new_input.txt
output_path=netease/python/output

hadoop fs -rmr $output_path

hadoop jar /opt/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar -file statistics_map.py statistics_reduce.py -input netease/input/${input_file} -output $output_path -mapper 'python statistics_map.py' -reducer 'python statistics_reduce.py'

hadoop fs -cat ${output_path}/part-00000

