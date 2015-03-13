input_path=/user/jdp/netease/input
output_path=/user/jdp/netease/java/output
class_name=Statistics
tmp_dir=classes

rm -rf $tmp_dir
mkdir $tmp_dir


javac -classpath /opt/hadoop-1.2.1/hadoop-core-1.2.1.jar -d $tmp_dir ${class_name}.java

jar -cvf ${class_name}.jar -C $tmp_dir/ .

hadoop fs -rmr $output_path

hadoop jar ${class_name}.jar org.jdp.${class_name} $input_path $output_path

hadoop fs -cat ${output_path}/part-00000
