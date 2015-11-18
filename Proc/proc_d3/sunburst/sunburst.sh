cat ../*.json | ../jq/jq '.retweeted_status| .text'> retweetText
python preprocess.py
