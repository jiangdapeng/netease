#/usr/bin/env bash
hadoop jar /opt/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar -file statistics_map.py statistics_reduce.py -input netease/input/input.txt -output netease/output -mapper 'python statistics_map.py' -reducer 'python statistics_reduce.py'

