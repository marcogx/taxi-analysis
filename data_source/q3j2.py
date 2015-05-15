import sys

current_key = None
current_count = 0
current_sum = 0
for line in sys.stdin:
	date, avg1, sum1 = line.split('\t')
	date = date[5:7]
	avg1=float(avg1)
	if current_key == date:
		current_count+=1
		current_sum+=avg1
	else:
		if current_key:
			avg_new = current_sum/current_count
			print '[\'%s\', %f],' % (current_key, avg_new)
		current_key=date
		current_sum=0
		current_sum+=avg1
		current_count=0
		current_count+=1

if current_key == date:
	if current_key:
		avg_new = current_sum/current_count
		print '[\'%s\', %f],' % (current_key, avg_new)
