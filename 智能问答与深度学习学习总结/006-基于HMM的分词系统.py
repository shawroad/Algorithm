"""

@file   : 006-基于HMM的分词系统.py

@author : xiaolu

@time   : 2019-07-09

"""
import json
# from curses import ascii

OUT_OF_OBS = "_OOO_"

# 由字构词方法的分词系统
class Tokenizer:
    def __init__(self):
        self._hmm_meta = self.__load_metadata()    # 加载配置文件
        self.states = self._hmm_meta['pi']
        self.observations = self._hmm_meta['observations']
        # 各个词的初始概率，以及喷射，转移概率。我们的配置文件中都有
        self.pi = self._hmm_meta['pi']
        self.A = self._hmm_meta['A']
        self.B = self._hmm_meta['B']

    def __load_metadata(self):
        # 加载配置文件
        with open('./data/hmm.json', 'r', encoding='utf8') as f:

            return json.load(f)

    def __viterbi(self, obs):
        # 使用维特比算法进行解码
        V = [{}]
        path = {}
        for y in self.states:
            V[0][y] = self.pi[y] * self.B[y][obs[0]]
            path[y] = [y]

        # 沿着时间1, 2..t进行计算
        for t in range(1, len(obs)):
            V.append({})
            newpath = {}

            # 根据t-1时刻状态概率，观测概率矩阵和转移概率矩阵计算t时刻最大概率转态 记录路径
            for y in self.states:
                # 看前一个状态中, 那个状态转移到当前状态并且当前状态喷射出当前观测值的概率大， 谁大谁就做前一个状态
                (prob, state) = max([(V[t - 1][y0] * self.A[y0][y] * self.B[y][obs[t]], y0) for y0 in self.states])
                V[t][y] = prob
                newpath[y] = path[state] + [y]  # y状态概率最大: 前一个状态 和 当前能喷射出最大概率的状态
            path = newpath
        (prob, state) = max([(V[len(obs) - 1][y], y) for y in self.states])
        return (prob, path[state])

    def __decode_sbme(self, text, labels, punctuations=None):
        # 对编码序列进行解码输出
        def resolve_punctuation(i):
            if punctuations and i in punctuations:
                return punctuations[i]

        token = ''
        for index, label in enumerate(labels):
            if label == 'S':
                yield text[index]
            if label == 'B':
                token = text[index]
            if label == 'M':
                token += text[index]
            if label == 'E':
                token += text[index]
                yield ''.join(token)
                token = ''

            if index == (len(labels) - 1) and (labels[-1] != 'E') and token:
                yield token

            ps = resolve_punctuation(index+1)  # 处理标点符号
            if ps:
                for x in ps:
                    yield x

    def cut(self, sentence, punctuation=True):
        # 分词接口
        sentence = ''.join(sentence.split())
        text = []
        punctuations = {}
        for ch in sentence:

            if is_zh(ch):   # 判断当前字符是否为汉字
                if ch in self.observations:
                    # 如果当前的字是汉字并且在我们配置的状态中，则添加到text
                    text.append(ch)
                else:
                    text.append(OUT_OF_OBS)
            elif is_punct(ch):   # 判断当前字符是否为标点
                if not (len(text)) in punctuations:
                    punctuations[len(text)] = [ch]
                else:
                    punctuations[len(text)] += ch  # 这种情况针对有好几个标点连着的情形

        if len(text) > 0:
            prob, path = self.__viterbi(text)
            return self.__decode_sbme(text, path, punctuations if punctuation > 0 else None)

        if len(text) == 0 and len(punctuations.keys()) > 0:
            result = []
            for x in punctuations.values():
                [result.append(y) for y in x]
            return result
        return []


# 下面两个函数是判断当前字符是否为汉字 可忽略
def is_zhs(str):
    for i in str:
        if not is_zh(i):
            return False
    return True


def is_zh(ch):
    """return True if ch is Chinese character.
    full-width puncts/latins are not counted in.
    """
    x = ord(ch)
    # CJK Radicals Supplement and Kangxi radicals
    if 0x2e80 <= x <= 0x2fef:
        return True
    # CJK Unified Ideographs Extension A
    elif 0x3400 <= x <= 0x4dbf:
        return True
    # CJK Unified Ideographs
    elif 0x4e00 <= x <= 0x9fbb:
        return True
    # CJK Compatibility Ideographs
    elif 0xf900 <= x <= 0xfad9:
        return True
    # CJK Unified Ideographs Extension B
    elif 0x20000 <= x <= 0x2a6df:
        return True
    else:
        return False


# 下面函数是判断标点   可忽略
def is_punct(ch):
    x = ord(ch)
    # in no-formal literals, space is used as punctuation sometimes.
    if x < 127:   # and ascii.ispunct(x)
        return True
    # General Punctuation
    elif 0x2000 <= x <= 0x206f:
        return True
    # CJK Symbols and Punctuation
    elif 0x3000 <= x <= 0x303f:
        return True
    # Halfwidth and Fullwidth Forms
    elif 0xff00 <= x <= 0xffef:
        return True
    # CJK Compatibility Forms
    elif 0xfe30 <= x <= 0xfe4f:
        return True
    else:
        return False


if __name__ == "__main__":
    # 请输入你的语料
    text = "老子今天不上班，只剩下钢琴陪我弹了一天，安静的旧旧的。"
    T = Tokenizer()
    print(' '.join(T.cut(text)))


