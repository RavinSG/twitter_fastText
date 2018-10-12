import json
import os
import bz2
# import preprocess_fasttext as ftp
import threading
from os.path import join, getsize
import re

eng_tweet_count = 0
def get_tweets_from_file(input_filename, output_filename):
    destination = open(output_filename, 'a', encoding='utf-8')
    tweet_file = open(input_filename)
    global eng_tweet_count
    for i in tweet_file:
        tweet_data = json.loads(i)
        if 'text' in tweet_data.keys():
            tweet = tweet_data['text']
            tweet = re.sub("[\n]+", " <newline> ", tweet)
            lang = tweet_data['lang']
            if lang == 'en':
                eng_tweet_count = eng_tweet_count + 1
                #tweet = ftp.ft_process(tweet)
                #tweet = re.sub("RT <user> : ", "", tweet)
                destination.write(tweet + "\n")
    print("English tweets: ", eng_tweet_count)
    return None


def navigate_folder(folder_name, file_name):
    for root, dirs, files in os.walk(folder_name):
        print(root)
        print(dirs)
        for i in files:
            if i.endswith('.bz2'):
                file_path = os.path.join(root, i)
                input_folder = '-'.join(root.split('\\')[1:])
                destination = 'processed/' + input_folder + '-' + '.'.join(i.split('.')[0:2])
                print(destination)
                with open(destination, 'wb') as new_file, bz2.BZ2File(file_path, 'rb') as file:
                    for data in iter(lambda: file.read(100 * 1024), b''):
                        new_file.write(data)
                get_tweets_from_file(destination, file_name)
                os.remove(destination)


t1 = threading.Thread(target=navigate_folder, args=['twitter-stream-2017-12-01\\2017\\12\\1\\00','Thread1_noLang.txt'])
t2 = threading.Thread(target=navigate_folder, args=['twitter-stream-2017-12-01\\2017\\12\\2','Thread2.txt'])
t3 = threading.Thread(target=navigate_folder, args=['twitter-stream-2017-12-01\\2017\\12\\3','Thread3.txt'])
t4 = threading.Thread(target=navigate_folder, args=['twitter-stream-2017-12-01\\2017\\12\\4','Thread4.txt'])
t5 = threading.Thread(target=navigate_folder, args=['twitter-stream-2017-12-01\\2017\\12\\5','Thread5.txt'])
t6 = threading.Thread(target=navigate_folder, args=['twitter-stream-2017-12-01\\2017\\12\\6','Thread6.txt'])

t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()
