import os
import argparse
import const

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root_path', type=str, default='data',
                        help='data path for read or write')
    parser.add_argument('--model_path', type=str, default=r'C:\Users\dell\Desktop\jiayan_models')

    return parser.parse_args()


def get_sentences(path):  # sourcery skip: inline-immediately-returned-variable
    filenames = os.listdir(f'{path}/chapters')
    all_sentences = []
    for filename in filenames:
        with open(f'{path}/chapters/{filename}', 'r', encoding='utf-8') as f:
            all_sentences.extend(line.replace('\n', '') for line in f)
    long_string = ''.join(all_sentences)
    return long_string


def get_persons(path):
    filename = f'{path}/persons.txt'
    persons = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            item = line.replace('\n', '').split('\t')
            name, other_name = item[0], item[1]
            persons[name] = other_name
    return persons


if __name__ == '__main__':
    args = parse_args()
    long_string = get_sentences(args.root_path)
    persons_dict = get_persons(args.root_path)
    print(persons_dict)