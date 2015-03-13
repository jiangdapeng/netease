package org.jdp;

import java.io.IOException;
import java.util.*;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;

public class Statistics {

   public static String list2string(String[] arr, String sep) {
     if (arr == null) {
       return null; 
     }
     StringBuilder result = new StringBuilder();
     boolean flag = false;
     for(String s : arr) {
        if (flag) {
          result.append(sep);
        }else {
          flag = true;
        }
        result.append(s);
     }
     return result.toString();
   }

   public static class Map extends MapReduceBase implements Mapper<LongWritable, Text, Text, Text> {
     //private final static IntWritable one = new IntWritable(1);
     private Text id = new Text();

     public void map(LongWritable key, Text value, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {
       String line = value.toString();
       String[] fields = line.split("\t");
       id.set(fields[0]);
       String[] rest = Arrays.copyOfRange(fields,1,fields.length);
       String outStr = list2string(rest,"\t");
       Text outText = new Text(outStr);
       output.collect(id, outText);
     }
   }

   public static class Reduce extends MapReduceBase implements Reducer<Text, Text, Text, Text> {
     public void reduce(Text key, Iterator<Text> values, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {
       int sum = 0;
       int high = -1;
       int low = 1000000;
       int max_score = -1;
       int count = 0;
       String row = null;
       while (values.hasNext()) {
         count += 1;
         row = values.next().toString();
         if ( row.length() < 1 ) {
           continue;
         }
         String[] fields = row.split("\t");

         int level = Integer.parseInt(fields[0]);
         int coin = Integer.parseInt(fields[1]);
         int score = Integer.parseInt(fields[2]);

         sum += coin;
         if ( level > high ) {
           high = level;
         }
         if ( level < low ) {
           low = level;
         }

         if ( score > max_score ) {
           max_score = score;
         }
       }
       String result = String.format("%d\t%d\t%.2f\t%d",high,low,sum*1.0/count,max_score);
       output.collect(key, new Text(result));
     }
   }

   public static void main(String[] args) throws Exception {
     JobConf conf = new JobConf(Statistics.class);
     conf.setJobName("statistics");

     conf.setOutputKeyClass(Text.class);
     conf.setOutputValueClass(Text.class);

     conf.setMapperClass(Map.class);
     //conf.setCombinerClass(Reduce.class);
     conf.setReducerClass(Reduce.class);

     conf.setInputFormat(TextInputFormat.class);
     conf.setOutputFormat(TextOutputFormat.class);

     FileInputFormat.setInputPaths(conf, new Path(args[0]));
     FileOutputFormat.setOutputPath(conf, new Path(args[1]));

     JobClient.runJob(conf);
   }
}
