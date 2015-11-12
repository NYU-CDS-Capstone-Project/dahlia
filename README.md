# Team Dahlia 
## Instant visualization of Twitter data using an online dashboard

**Team Member:**
   
* Meihao Chen
* Yitong Wang

**Advisor:**
* Pablo Barbera


## Potential datasets

### Tweets about Hillary Clinton's presidential announcement

- All tweets mentioning "hillary", "hillary clinton" or "clinton" between April 12, 2015 at 17:00 UTC and April 14, 2015 at 17:00 UTC. Tweets are stored in JSON format by hour (each file is a different hour of data) and gzipped, inside a tar file. [LINK](https://s3.amazonaws.com/smappdata/hillary.tar)
#### Analysis Tasks

- General description of the dataset: number of tweets in total; number of tweets in a time series; important word count; number of retweets

### Tweets about the 2014 Oscars

- All tweets mentioning "oscars", "oscar", "red carpet", "oscars2014", "academy", "award", "awards" between March 2nd, 23:00 UTC and March 3rd 06:00 UTC. Tweets are stored in JSON format by hour (each file is a different hour of data) and gzipped, inside a tar file. [LINK](https://s3.amazonaws.com/smappdata/oscars.tar)

#### Analysis Tasks

- General decription of the dataset: count hashtags, number of tweets in a time series
- Name entity recognition research. [LINK](http://www.sciencedirect.com/science/article/pii/S0004370212000276)
- Public opinion analysis and prediction of award. [LINK](http://delivery.acm.org/10.1145/2340000/2337551/a66-paltoglou.pdf?ip=216.165.95.72&id=2337551&acc=ACTIVE%20SERVICE&key=36E5A5D4E382B3FA%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&CFID=550903582&CFTOKEN=65484671&__acm__=1444078116_3245547784ac583d81e3a2ab37a00c10)

## Visualization Tools

- We intent to use D3, javascript, and other tools to build interactive visualization on website.

## Oct 5 2015
- Pushed code for reading json file and running preliminary analysis on the hillary dataset

## Nov 8 2015: Re-structuring this repository
### Data
#### Hillary
- Preliminary: basic counts of fields (used for the exploratory data presentation)
- dataForVis: processed data for d3 visualization

#### Oscar
- OscarNameCount: data derived from name entity tagger on the tweet texts, which gives the number of occurrences of names
- filteredData: Fields extracted from Oscar-related tweets
- Rest: Counts of each field data file

### Document
- All the references file and project descriptions

### Proc
#### bashFilter
- Scripts for running lmr (local map reduce), jq, counting data, and generating data for d3 (hier_bund.sh)

#### countMapReduce
- MapReduce scripts for processing the raw field data extracted using jq

#### nameRecognition
- Scripts for generating the name entity from the tweets

#### proc_d3
- Scripts for processing data into the format that can be used for d3 visualization 
- Normally takes the data processed by jq

### Vis
- Contains all the files needed for constructing the webpage


