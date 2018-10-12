from ekphrasis.classes.preprocessor import TextPreProcessor
from ekphrasis.classes.tokenizer import SocialTokenizer
from ekphrasis.dicts.emoticons import emoticons

text_processor = TextPreProcessor(
    # terms that will be normalized
    normalize=['url', 'email', 'percent', 'money', 'phone', 'user',
               'time', 'url', 'date', 'number'],
    # terms that will be annotated
    annotate={"hashtag", "repeated",
              'emphasis', 'censored'},
    fix_html=True,  # fix HTML tokens

    # corpus from which the word statistics are going to be used
    # for word segmentation
    segmenter="twitter",

    # corpus from which the word statistics are going to be used
    # for spell correction
    corrector="twitter",

    unpack_hashtags=False,  # perform word segmentation on hashtags
    unpack_contractions=True,  # Unpack contractions (can't -> can not)
    spell_correct_elong=False,  # spell correction for elongated words

    # select a tokenizer. You can use SocialTokenizer, or pass your own
    # the tokenizer, should take as input a string and return a list of tokens
    tokenizer=SocialTokenizer().tokenize,

    # list of dictionaries, for replacing tokens extracted from the text,
    # with other expressions. You can pass more than one dictionaries.
    dicts=[emoticons]
)


def get_file():
    input_file_name = input('Enter input file path: ')
    output_file_name = input('Enter output file path: ')
    file = open(input_file_name, encoding='utf-8')
    processed = open(output_file_name+'.txt', 'a', encoding='utf-8')
    counter = 0
    words = 0
    for s in file:
        counter = counter + 1
        tweet = s.split(',')[6]
        tweet = tweet.split(' ')
        words = words + len(tweet)
        processed_tweet = " ".join(text_processor.pre_process_doc(tweet))
        processed.write(processed_tweet+'\n')
        if counter % 10000 == 0:
            print("Processed number of tweets: ", counter)
            print("Processed number of words: ", words)


def ft_process(sentence):
   return " ".join(text_processor.pre_process_doc(sentence))
