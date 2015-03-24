CREATE TABLE IF NOT EXISTS  log(id INT, level INT, coin INT, score INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';
LOAD DATA LOCAL INPATH '/home/jdp/code/netease/task/hadoop/new_input.txt' OVERWRITE INTO TABLE log;
SELECT id , max(level) as max_level , min(level) as min_level, sum(coin)/count(*) as total_coin, max(score) as highest_score  from log GROUP BY id;
