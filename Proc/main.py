from .proc import *

def main():
    while True:
        try:
            dataset = raw_input('Please input the full path of your dataset, note that your data file must be .zip or .tar:\n')
            path =  os.getcwd()
            if dataset = 'exit':
                raise KeyboardInterrupt
            data = load_data(dataset)
            break
        except KeyboardInterrupt:
            print 'Terminated!'
            sys.exit()
        except ValueError:
            print 'Invalid data! Please consult out github repo for detailed information.'
            continue
    while True:
        try:
            fields = ['hashtag', 'coordinates', 'mention', 'source', 'tweet', 'user']
            for f in field:
                out = count_single_field(f, data)
                dict_to_csv(out, '%s/Vis/data/%s.txt'%(path, f))
                if f == 'tweet':
                    word = count_wourd(out, stopwords)
                    dict_to_csv(word, '%s/Vis/data/word.txt'%(path))

        except KeyboardInterrupt:
            print 'terminated!'
            sys.exit()



