# @Author: wukehao
# @Date:   2017-09-16T07:01:28+08:00
# @Last modified by:   wukehao
# @Last modified time: 2017-09-16T07:33:11+08:00
# 读取数据

import numpy as np
from tqdm import tqdm
import _pickle as pickle
from gensim.models import KeyedVectors


## 加载生成X
def load_x():
    print("Begin to generate X vector.")
    model = KeyedVectors.load_word2vec_format('../var/word2vec.bin', binary=True)

    with open('../var/word2vec.data') as fp:
        x_txt = fp.readlines()

    X = []

    PADDING = np.array([0] * 200, dtype='float32')
    x_txt = list(filter(lambda item: item.strip() != '', x_txt))
    for txt in tqdm(x_txt):
        x = []
        for t in txt:
            if t in model:
                x.append(model[t])
            else:
                x.append(PADDING)
        X.append(x)


    with open('../var/X.pkl', 'wb') as fp:
        pickle.dump(X, fp)



## 加载生成Y
def load_y():
    print("Begin to generate Y vector.")
    def S2I(s):
        if s == 'B':
            return 0
        elif s == 'I':
            return 1
        elif s == 'E':
            return 2
        else:
            return 3
    with open('../var/BIOE_text.data') as fp:
        y_txt = fp.readlines()

    Y = []
    for txt in tqdm(y_txt):
        Y.append(np.array([S2I(i) for i in txt.strip()], dtype='float32'))

    with open('../var/Y.pkl', 'wb') as fp:
        pickle.dump(Y, fp)


if __name__ == "__main__":
    load_x()
    load_y()
