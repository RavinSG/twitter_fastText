import pandas as pd
import csv

init_file = pd.read_csv("Similarities/100D-emoji.csv", names=["Emoji 1", "Emoji 2", "100D"])

files = ["Similarities/200D-emoji.csv", "Similarities/300D-emoji.csv"]
init_file["200D"] = pd.read_csv("Similarities/200D-emoji.csv",names=["Emoji 1", "Emoji 2", "200D"]).iloc[:,-1]
init_file["300D"] = pd.read_csv("Similarities/300D-emoji.csv",names=["Emoji 1", "Emoji 2", "300D"]).iloc[:,-1]
df = pd.DataFrame(init_file)
init_file.to_csv("Similarities/analyze_emoji.csv")
print(init_file.head())

def convert_to_csv(file_name, output_name):
    file = open(file_name, 'r', encoding='utf-8')
    output = open("{}.csv".format(output_name), 'w', newline='', encoding='utf-8')
    csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in file:
        csv_writer.writerow(row.strip().split(" "))

#convert_to_csv("Similarities/322M_Tweets-emoji_similarities.txt", "Similarities/300D-emoji")
#df = pd.read_csv("Similarities/detailed.csv")
#df["Google"] = pd.read_csv("Similarities/Google_Word2Vec-similarities.csv",names=["Word 1", "Word 2", "Human Score", "Google"]).iloc[:,-1]
#df.to_csv("Similarities/detailed.csv")
#print(df.head())