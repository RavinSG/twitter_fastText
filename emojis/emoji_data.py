import json
import codecs
import csv


def create_file(file_name):
    emoji_file = open(file_name, encoding='utf-8')
    output = open('emoji_pairs.csv', 'w', newline='')
    csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in emoji_file:
        emojis = json.loads(row, encoding='utf-8')
        for i in emojis:
            row = []
            for k in i['emojiPair'].keys():
                row.append(i['emojiPair'][k]['unicodelong'])
            csv_writer.writerow(row)


def create_scores(file_name):
    emoji_file = open(file_name, encoding='utf-8')
    output = open('emoji_score.csv', 'w', newline='')
    csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in emoji_file:
        emojis = json.loads(row, encoding='utf-8')
        for i in emojis:
            row = []
            for k in i['emojiPairSimilarity'].keys():
                row.append(i['emojiPairSimilarity'][k])
            csv_writer.writerow(row)


# create_file('EmoSim508.json')
# create_scores('EmoSim508.json')

file = codecs.open('emoji_pairs.csv', 'r', encoding='unicode_escape')
for i in file:
    line = i.strip().split(',')
    print(line[0], line[1])