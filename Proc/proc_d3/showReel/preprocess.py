import json
import pickle
import itertools
import collections
import operator

data = pickle.load(open('data.pkl','rb'))
print len(data)
top_n = 4

def takeInput(data,top_n):
	# Get all the hashtags
	hashtag = list(itertools.chain(*[i[1] for i in data]))
	# get the top 4 hashtags
	# can change later
	topNhash = dict(collections.Counter(hashtag).most_common(top_n))
	# data_new only contains data where the top N most common hashtags
	data_new = [i for i in data if len(set(i[1]).intersection(set(topNhash.keys()))) > 0]
	# data_final:list of tuples where each tuple is a flattened out from data_new and iff i[1] in top4hash.keys()
	# eliminate out elements in data_new where some hashtags in data_new are not from the top 4
	data_final = list(itertools.chain(*[[(i[0],j) for j in i[1] if j in topNhash.keys()] for i in data_new]))
	
	# temp: get only the relevant data from data_final
	# a.k.a. the ones that match top N hashtags
	temp = []
	for i in topNhash.keys():
		temp.append([j for j in data_final if j[1] == i])

	# category: same data as temp, but reform the date and data structure
	category = []
	for i in temp:
		wtf = []
		for j in i:
			time = j[0].split(' ')
			month,day,hour,year = time[1].encode('ascii','ignore'),time[2].encode('ascii','ignore'),time[3].encode('ascii','ignore').split(':')[0],time[-1].encode('ascii','ignore')
			wtf.append(('%s-%s-%s-%s' % (month,day,year,hour),j[1]))
		category.append(wtf)  

	# OH MY FUCKING GOD, FINALLY!
	data_FINAL = []
	for i in category:
		sort_list = sorted(i,key=lambda x: (x[0].split('-')[3],x[0].split('-')[1]))
		data_FINAL.append(sort_list) 

	return data_FINAL     


if __name__ == '__main__':

	data_FINAL = takeInput(data,top_n)
	with open('data_tweet.csv','wb') as f:
		f.write('symbol,date,price'+'\n')
		for i in data_FINAL:
			for j in sorted(collections.Counter(i).items(), key = operator.itemgetter(0)):
				f.write('%s,%s,%s'%(j[0][1],j[0][0],j[1])+'\n')

	
