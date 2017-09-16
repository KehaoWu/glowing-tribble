# @Author: wukehao
# @Date:   2017-09-16T10:31:53+08:00
# @Last modified by:   wukehao
# @Last modified time: 2017-09-16T10:39:33+08:00
# 从picle加载数据

import _pickle as pickle

print("Load X")
X = pickle.load(open('../var/X.pkl', 'rb'))
print("Finish load X")
print("Load Y")
Y = pickle.load(open('../var/Y.pkl', 'rb'))
print("Finish load Y")
