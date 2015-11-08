#!/bin/sh
zcat *.gz |./jq '.entities, .user_mentions | .[]? | .screen_name' > mentionedName
zcat *.gz | ./jq '.user| .location' > location
zcat *.gz | ./jq '.entities| .hashtags |.[]?|.text' > hashtags
zcat *.gz | ./jq '.source' > source
zcat *.gz | ./jq '.retweeted_status| .text'> retweetText
zcat *.gz | ./jq '.user| .screen_name' > screen_name
