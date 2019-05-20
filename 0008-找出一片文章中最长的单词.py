def find_length_word(article):
    # 1.首先按照空格将此段文字断开
    split_word = article.split(' ')
    print(split_word)
    most_len = 0
    most_word = ''
    for item in split_word:
        if len(item) > most_len:
            most_word = item
            most_len = len(item)
    return most_word, most_len


if __name__ == '__main__':
    article = 'In the community discovery algorithm, it is almost impossib' \
              'le to determine the number of communities first, so there mu' \
              'st be a measurement method to measure whether each result is' \
              ' relatively optimal in the process of calculation.'
    # 上面为一段文字  找出最长的单词
    most_word, most_len = find_length_word(article)
    print('最长的单词为:{}, 对应的长度为:{}'.format(most_word, most_len))
