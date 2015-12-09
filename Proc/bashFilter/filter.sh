#!/bin/sh
gzcat ../../Data/Hillary/hillary/* | ./jq-osx-amd64 '.entities, .user_mentions | .[]? | .screen_name' > ../../Data/Hillary/result_mention.txt
gzcat ../../Data/Hillary/hillary/* | ./jq-osx-amd64 '.user| .location' > ../../Data/Hillary/result_cola.txt
gzcat ../../Data/Hillary/hillary/* | ./jq-osx-amd64 '.entities| .hashtags |.[]?|.text' > ../../Data/Hillary/result_hash.txt
gzcat ../../Data/Hillary/hillary/* | ./jq-osx-amd64 '.source' > ../../Data/Hillary/result_source.txt
gzcat ../../Data/Hillary/hillary/* | ./jq-osx-amd64 '.retweeted_status| .text'> ../../Data/Hillary/result_tweet.txt
gzcat ../../Data/Hillary/hillary/* | ./jq-osx-amd64 '.user| .screen_name' > ../../Data/Hillary/result_user.txt
gzcat ../../Data/Hillary/hillary/* | ./jq-osx-amd64 '.coordinates| .coordinates| tostring' > ../../Data/Hillary/result_coord.txt
