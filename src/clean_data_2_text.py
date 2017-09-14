# @Author: Kehao Wu <wukehao>
# @Date:   2017-09-14T15:37:34+08:00
# @Last modified by:   wukehao
# @Last modified time: 2017-09-14T16:34:43+08:00
# 将boson的数据清洗成文本数据，并以空格分割成unigram数据

import os
import re

filename_self = os.path.realpath(__file__)
filepath_self = os.path.dirname(filename_self)
filename_boson = os.path.join(filepath_self, '../data/BosonNLP_NER_6C/BosonNLP_NER_6C.txt')

if not os.path.exists(os.path.join(filepath_self, '../var')):
    os.makedirs(os.path.join(filepath_self, '../var'))

with open(filename_boson) as fp:
    lines = fp.readlines()

tags = []
pure_text = []
BIOE_text = []
word2vec = []

for line in lines:
    line = line.replace('\\n', '')
    _tags = []
    # 取出所有标注
    pattern = re.search('\{\{(?P<tag>.+?):(?P<name>.+?)\}\}', line)
    while pattern:
        start = pattern.start()
        end = pattern.end()
        name = pattern.groupdict().get("name")
        tag = pattern.groupdict().get("tag")
        _tags.append({
            'start': start,
            'end': start + len(name),
            'name': name,
            'tag': tag
        })
        name = re.sub('\(', '\\\(', name)
        name = re.sub('\)', '\\\)', name)
        name = re.sub('\+', '\\\+', name)
        line = re.sub('\{\{' + tag + ':' + name + '\}\}', name, line)
        pattern = re.search('\{\{(?P<tag>.+?):(?P<name>.+?)\}\}', line)
    y = ['O'] * len(line)
    for tag in _tags:
        tag['line'] = line
        y[tag['start']:tag['end']] = ['I'] * len(tag['name'])
        y[tag['start']] = 'B'
        y[tag['end'] - 1] = 'E'
        tag['y'] = y
    word2vec.append(' '.join(line))
    pure_text.append(line)
    BIOE_text.append(''.join(y))

    tags.extend(_tags)
for index, tag in enumerate(tags):
    if tag.get('tag') != 'person_name':
        continue
    line = tag['line']
    y = tag['y']
    print(line[tag['start']:tag['end']], tag['name'])
    print(y[tag['start']:tag['end']], tag['name'])


with open(os.path.join(filepath_self, '../var/pure_text.data'), 'w') as fp:
    fp.write("\n".join(pure_text))

with open(os.path.join(filepath_self, '../var/BIOE_text.data'), 'w') as fp:
    fp.write("\n".join(BIOE_text))

with open(os.path.join(filepath_self, '../var/word2vec.data'), 'w') as fp:
    fp.write("\n".join(word2vec))
