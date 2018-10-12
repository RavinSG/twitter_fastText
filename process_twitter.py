import preprocess_fasttext as ft
import re

count = 0

def read_tweets(file):
    global count
    file = open(file,'r', encoding='utf-8')
    processed = open("Reg_processed.txt", 'a', encoding='utf-8')

    for i in file:
        count = count + 1
        if count % 100000 == 0:
            print("Processed tweets: ", count)
        tweet = ft.ft_process(i)
        tweet = re.sub("RT <user> : ", "", tweet)
        tweet = re.sub("<newline>", "", tweet)
        tweet = re.sub(" …", "", tweet)
        processed.write(tweet+ "\n")

files = ['2017-01.txt', '2017-02.txt', '2017-05.txt']

for file in files:
    read_tweets(file)