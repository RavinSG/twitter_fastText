import csv
import codecs
from gensim.models.wrappers import FastText


def word_sim():
    output = open("{}-similarities.txt".format(model_name[:-4]), 'w')
    with open('word_set.csv', 'r') as csv_file:
        in_file = csv.reader(csv_file)
        for row in in_file:
            output.write(row[0] + " " + row[1] + " " + row[-1] + " " + str(model.similarity(row[0], row[1])))


def emoji_sim():
    output = open("{}-emoji_similarities.txt".format(model_name[:-4]), 'w')
    file = codecs.open('emoji_pairs.csv', 'r', encoding='unicode_escape')
    for row in file:
        line = row.strip().split(',')
        output.write(line[0] + " " + line[1] + " " + str(model.similarity(line[0], line[1])))


model_name = input("Enter model name:")
print("Loading vector model...")
model = FastText.load_fasttext_format(model_name)
print("Model loaded!!")

print("Creating output file..")
print("Generating similarities")
emoji_sim()
print("Done generating")
