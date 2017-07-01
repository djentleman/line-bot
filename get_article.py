# -*- coding: utf-8 -*-

from langdetect import detect_langs
import nltk
from twingly_search import Client

def do_twingly_search(search_terms):
   client = Client(api_key='ECB40E2E-C91F-47AF-9F4D-5BAB7B755C78')
   result = client.execute_query(search_terms)
   for post in result.posts:
       print post.url

def strip_stop_words(tokens):
    # english and japanese stop words are requires
    # 英語でも日本語でもいらない言葉を消す
    stop_words = ['i', 'you', 'blog',
                  'article',
                  u'私', u'俺', u'記事',
                  u'ブロク']

    return filter(lambda x: x.lower() not in stop_words, tokens)

def tokenize_english(text):
    sent_text = nltk.sent_tokenize(text)
    nouns = []
    for sentence in sent_text:
        tokenized_text = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokenized_text)
        print tagged
        nouns += [w[0] for w in tagged if 'NN' in w[1]]
    return nouns


def find_articles(text, lang):
    if lang == 'en':
        tokens = tokenize_english(text)
    else:
        print 'LEYS TOKENIZE JAPANESE!'
        tokens = []

    concatinated_terms = ' '.join(strip_stop_words(tokens))
    do_twingly_search(concatinated_terms)

def main():
    user_input = str(raw_input(">>>"))
    print "lets find a blog!"
    lang = detect_langs(user_input)[0].lang
    print user_input
    if lang in ['en', 'ja']:
        find_articles(user_input, lang)
    else:
        print 'not supported :('

if __name__ == '__main__':
    main()
