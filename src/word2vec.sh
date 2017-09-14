# @Author: Kehao Wu <wukehao>
# @Date:   2017-09-14T16:36:07+08:00
# @Last modified by:   wukehao
# @Last modified time: 2017-09-14T16:36:30+08:00



#!/bin/bash
TEXT_DATA=../var/word2vec.data
VECTOR_DATA=../var/word2vec.bin

word2vec -train $TEXT_DATA -output $VECTOR_DATA -cbow 0 -size 200 -window 5 -negative 0 -hs 1 -sample 1e-3 -threads 12 -binary 1
