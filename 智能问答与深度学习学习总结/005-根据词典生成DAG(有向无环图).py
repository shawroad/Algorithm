"""

@file   : 005-根据词典生成DAG(有向无环图).py

@author : xiaolu

@time   : 2019-07-09

"""
# 构建词典
dictionary = dict({
    '刘': [10, 'nz'],
    '刘德': [10, 'nz'],
    '刘德华': [10, 'nz']
})


# 生成有向无环图
def get_DAG(sentence):
    DAG, N = {}, len(sentence)
    for k in range(N):
        suffix, i = [], k
        word = sentence[k]
        while i < N and word in dictionary:
            if dictionary[word][0] > 0:
                suffix.append(i)
            i += 1
            word = sentence[k: i+1]
        if len(suffix) == 0:
            suffix.append(k)
        DAG[k] = suffix
    return DAG


sentences = '刘德华动情的演唱了忘情水'
lis = [x for x in sentences]
print(" ".join(lis) + '\n' + str(get_DAG(sentences)))


