#/usr/bin/sh

input=data/*.log
output=login_count_2.txt
cat $input |  grep LOGIN | awk '{count[$5]++}END{for(name in count)print name,count[name]}' | sort -k2 -nr > $output

cat $output | awk '{
  if ( $2 + 0 > 5 ) {
    print $0;
  }
}' > $output-gt5

cat $output | awk '{
  if ( $2 + 0 <= 5 ) {
    print $0;
  }
}' > $output-let5
