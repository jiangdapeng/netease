本作业代码运行环境说明：
1. 需要安装hadoop(我在Linux上安装hadoop单机版，版本hadoop-1.2.1)
2. 需要安装python(版本：Python 2.7.5)
3. 需要安装hive(版本：hive-1.0.0)

输入文件说明：
1. 输入文件格式如:new_input.txt, 字段之间用'\t'分隔

运行说明：
1. 使用hadoop的m/r框架，采用java找出每个id的最高等级,最低等级,平均持有金钱和最大分数，结果会输出到标准输出：
  bash run_java.sh

2. 使用hadoop的m/r框架，采用python找出每个id的最高等级,最低等级,平均持有金钱和最大分数，结果输出到标准输出:
  bash run_python.sh

3. 使用hive实现同样的功能：
  hive -f hive.sql

如果输入数据是new_input.txt，最终的输出结果应该与result.txt相同
