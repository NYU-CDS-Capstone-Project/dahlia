#!/bin/sh

cat *.json | ./jq/jq '{user: .user| .screen_name, mentions:.entities | .user_mentions | .[]? | .screen_name, statCount: .user| .statuses_count}' > countEdge_1

python ../proc_d3/preprocess.py

