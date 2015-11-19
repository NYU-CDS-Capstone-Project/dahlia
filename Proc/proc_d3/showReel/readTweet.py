import os
import sys
import string
from operator import *
import matplotlib.pyplot as plt
import numpy as np
import pickle

# Graph the top n in the following fields: tweets, users, location, hashtags and mentions. 

def sortLine(top, name):
	print 'Sorting the raw results...'
	lines = []
	with open(name,'rb') as inp:
		for line in inp:
			l = line.strip('\n').split('\t')
			new = (l[:-1][0], int(l[-1]))
			lines.append(new)

	lines_new = sorted(lines, key = itemgetter(1), reverse = True)
	print 'Done'
	return lines_new[:top]

# def graphing(data):
# 	name, count = zip(*data)
# 	x = np.array(range(len(data)))
# 	y = np.array(count)
# 	x_label = np.array(name)
# 	plt.xticks(x, x_label, rotation = 45)
# 	plt.bar(x, y)
# 	plt.title('Most active users')
# 	plt.show()
  

# if __name__ == '__main__':
# 	# user = open('result_user.txt', 'rb')
# 	# location = open('result_loca.txt', 'rb')
# 	hashtag = open('result_hash.txt', 'rb')
# 	# mention = open('result_mention.txt', 'rb')
# 	# tweet = open('result_tweet.txt', 'rb')

# 	# users_top = sortLine(user, 15)
# 	# loca_top = sortLine(location, 10)
# 	hash_top = sortLine(hashtag, 10, 'hash_top')
# 	# mention_top = sortLine(mention, 15)
# 	# tweet_top = sortLine(tweet, 10)
