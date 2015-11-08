import shlex, subprocess
import matplotlib.pyplot as plt
import numpy as np

def get_count():
	# command_line = raw_input("Please enter your command")
	command_line = 'wc -l *.json'
	p = subprocess.Popen(command_line, stdout = subprocess.PIPE, stderr=subprocess.PIPE, shell='True')
	stdout, stderr = p.communicate()
	# print stdout, type(stdout)
	return stdout

def parse_count(stdout):
	parsed_out = stdout.split('\n')
	total = parsed_out[-2].strip().split(' ')[0]
	print 'Total number of tweet is : %s' % (total)
	return parsed_out[:-2]

def analyze_count(out):
	name = []
	count = []
	for i in out:
		element = i.strip().split(' ')
		count.append(int(element[0]))
		name.append(element[1])
	print name
	
	x = np.array(range(len(name)))
	y = np.array(count)
	x_label = np.array(name)
	plt.xticks(x, x_label, rotation = 90)
	plt.bar(x, y)
	plt.title('Number of tweets by time series')
	plt.show()
	plt.savefig('Number of Tweets vs Time')


if __name__ == '__main__':
	analyze_count(parse_count(get_count()))