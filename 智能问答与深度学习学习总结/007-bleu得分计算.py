"""

@file  : 007-bleu得分计算.py

@author: xiaolu

@time  : 2019-11-21

"""
import numpy as np
from collections import Counter


def BLEU(references, generated, max_grams=4, weights=None):
    '''
    BLEU(["The cat is on the mat", "There is a cat on the mat"], "The cat is on the mat", 3)
    :param references:
    :param generated:
    :param max_grams:
    :param weights:
    :return:
    '''
    ref_list = [ref.lower().split(" ") for ref in references]   # 比对的句子转小写并进行切分
    gen = generated.lower().split(" ")   # 生成句子转小写并进行切分
    cpn = np.empty((max_grams,), dtype=np.float32)
    for n in range(1, max_grams + 1):
        gen_gram = [" ".join(gen[i: i+n]) for i in range(0, len(gen) - n + 1)]
        refs_gram = [[" ".join(ref[i: i+n]) for i in range(0, len(ref) - n + 1)] for ref in ref_list]
        g_counter = Counter(gen_gram)
        r_counters = [Counter(ref_gram) for ref_gram in refs_gram]
        # print(gen_gram)
        # print(refs_gram)
        # print(g_counter)
        # print(r_counters)
        count_clip = 0
        for k, v in g_counter.items():
            count_clip += min(v, max([r.get(k, 0) for r in r_counters]))
        # print(count_clip)

        cpn[n-1] = count_clip/sum(g_counter.values())

    ls = len(gen)
    lc = max([len(ref) for ref in ref_list])

    brevity_penalty = 1 if lc > ls else np.exp(1-ls/lc)

    if weights is None:
        weights = np.ones_like(cpn)
    bleu = brevity_penalty * np.exp(np.mean(weights * np.log(cpn)))
    return bleu


if __name__ == '__main__':
    bleu = BLEU(["The cat is on the mat", "There is a cat on the mat"], "The cat is on the mat", 3)
    print(bleu)
