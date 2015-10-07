#! /usr/bin/env bash
# scipts for locally running mapreduce jobs, should not be 
# confused with the lmr software

cat ./*.json | ./countMapReduce/countUser_map.py | sort | ./countMapReduce/countUser_reduce.py > result_user
cat ./*.json | ./countMapReduce/countHash_map.py | sort | ./countMapreduce/countHash_reduce.py > result_hash
cat ./*.json | ./countMapReduce/countLoca_map.py | sort | ./countMapReduce/countLoca_reduce.py > result_loca
cat ./*.json | ./countMapReduce/countMention_map.py | sort | ./countMapReduce/countMention_reduce.py > result_mention
cat ./*.json | ./countMapReduce/countTweet_map.py | sort | ./countMapReduce/countTweet_reduce.py > result_tweet
 
