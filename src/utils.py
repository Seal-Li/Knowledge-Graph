from email import header
import os
import jieba
import argparse
import requests
import const
import json
from pyhanlp import HanLP

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root_path', type=str, default='data',
                        help='data path for read or write')

    return parser.parse_args()


def get_sentences(path):  # sourcery skip: inline-immediately-returned-variable
    filenames = os.listdir(f'{path}/chapters')
    all_sentences = []
    for filename in filenames:
        with open(f'{path}/chapters/{filename}', 'r', encoding='utf-8') as f:
            all_sentences.extend(iter(f))
    long_string = ''.join(all_sentences)
    return long_string


def get_words(long_string):
    words = jieba.lcut(long_string)
    end = 0
    for word in words:
        if word not in const.sign_replaced:
            words[end] = word
            end = end + 1
    return words[:end]


def ner(long_string):
    url = 'http://comdo.hanlp.com/hanlp/v1/ner/chineseName'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'token': '5201c343b2484397a82313007b1942951657724188005token'
    }
    data = {'text': long_string[:200]}
    result = requests.post(url, headers=headers, data=data)
    return result.text


if __name__ == '__main__':
    args = parse_args()
    long_string = get_sentences(args.root_path)
    # words = get_words(long_string)
    #print(words[:1000])
    # print(len(long_string))
    # res = ner(long_string)
    # print(res)
    res = HanLP.segment(long_string)
    print(res)