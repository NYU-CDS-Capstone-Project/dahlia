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
- Public opinion analysis and prediction of award.

## Visualization Tools

- We intent to use D3, javascript, and other tools to build interactive visualization on website.

## Oct 5 2015
- Pushed code for reading json file and running preliminary analysis on the hillary dataset

