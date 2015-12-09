from proc import *

def main():
    while True:
        try:
            dataset = raw_input('Please input the full path of your dataset, note that your data file must be .zip or .tar:\n')
            path =  os.getcwd()
            if dataset == 'exit':
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
            #Counting frequency for single fields
            fields = ['hashtag', 'coordinates', 'mention', 'source', 'tweet', 'user']
            for f in fields:
                print 'Processing %s'%(f)
                out = count_single_field(f, data)
                print '%d %s in total'%(len(out), f)
                if f == 'tweet':
                    dict_to_dsv(out, '%s/Vis/data/%s.csv'%(path, f), '|')
                    print 'Processing words'
                    word = count_word(out, stopwords)
                    print '%d words in total'%(len(word))
                    dict_to_dsv(word, '%s/Vis/data/word.csv'%(path))
                else:
                    dict_to_dsv(out, '%s/Vis/data/%s.csv'%(path, f))
            break


        except KeyboardInterrupt:
            print 'terminated!'
            sys.exit()

if __name__ == '__main__':
    main()

