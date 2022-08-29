import jieba  # 引入结巴库
import wordcloud


class cy:
    strLen = '无'
    Len = 0

    def __init__(self, words, Lent):
        """
        :param words: 欲生成的文本
        :param Lent: 欲展示的词组数
        """
        self.strLen = words
        self.Len = Lent

    def showWordCloud(self, filename):
        """
        :param filename: 欲存储到的文件地址
        :return: None
        """
        print(self.strLen)
        # 解析拆分词组  lcut的方法
        words = jieba.lcut(self.strLen)
        print(words)

        '''
        text = ''
        for i in range(len(words)):
            if i == 0:
                text = words[i] + '/'
            text = text + '/' + words[i]
        # 输出为 a/b/c...
        '''
        #    废弃用法

        # 通过键值对的形式存储词语及其出现的次数
        # 大括号表示 python的字典类型对应，
        # 键值对 key:value1 ,类似java的map对象和list
        counts = {}
        # 数组对象  用来接收需要传递给词云的内容
        chiyun = []
        for word in words:
            # == 1 单个词语不计算在内
            if len(word) < 2:
                continue
            else:
                # 遍历所有词语，每出现一次其对应的值加 1
                counts[word] = counts.get(word, 0) + 1

                # 将键值对转换成列表
        items = list(counts.items())

        # 根据词语出现的次数进行从大到小排序
        items.sort(key=lambda x: x[1], reverse=True)

        # 列标题 format
        #   print("{0:<5}{1:<8}{2:<5}".format('序号','词语', '频率'))

        # 需要显示的范围  10即显示前10个，0到9
        if len(items) >= self.Len:
            setLen = self.Len
        else:
            setLen = len(items)

        for i in range(setLen):
            word, count = items[i]
            print("{0:<5}{1:<8}{2:>5}".format(i + 1, word, count))
            chiyun.append(word)

        wl_space_split = " ".join(chiyun)

        w = wordcloud.WordCloud(font_path="simsun.ttc", width=1000, height=700, background_color="white").generate(wl_space_split)
        w.to_file(filename)
