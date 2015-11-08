#!/bin/sh
cat ./filteredData/userID | sort | ../proc/count.py > IDCount
cat ./filteredData/location |tr '[:upper:]' '[:lower:]'| sort | ../proc/count.py > locationCount
cat ./filteredData/hashtags |tr '[:upper:]' '[:lower:]'| sort | ../proc/count.py > hashtagCount
cat ./filteredData/retweetText |tr '[:upper:]' '[:lower:]'| sort |../proc/count.py > retweetCount
cat ./filteredData/source |tr '[:upper:]' '[:lower:]'| sort | ../proc/count.py > sourceCount
cat ./filteredData/screen_name |tr '[:upper:]' '[:lower:]'| sort | ../proc/count.py > nameCount
cat ./filteredData/userMention |tr '[:upper:]' '[:lower:]'| sort | ../proc/count.py> mentionCount
