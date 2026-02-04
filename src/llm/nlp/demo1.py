import jieba
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from rank_bm25 import BM25Okapi
from sklearn.metrics.pairwise import cosine_similarity


# 准备中文语料库（待处理文本列表）
corpus = [
    "Jieba是Python中最主流的中文分词包，支持精确模式、全模式和搜索引擎模式",
    "Rank-BM25是信息检索的经典算法，比TF-IDF更适合关键词匹配和文档检索",
    "sklearn中的TfidfVectorizer可快速实现TF-IDF特征提取，用于文本分类和聚类",
    "中文文本处理的核心步骤是分词，常用工具有Jieba、HanLP、PKUSeg等",
    "智能问答系统通常先通过BM25匹配FAQ，再用语义模型做精细回答"
]


def test_jieba():
    """
    测试分词
    """
    print("-"*50)
    # 精确模式（推荐通用场景）
    text = "在2025-09-06 20:23:00直播的 女足英超 第1轮：阿森纳VS伦敦城雌狮，对应的赛事ID是多少？"
    result = jieba.lcut(text)  # lcut 返回列表，cut 返回生成器
    print("精确模式：", result)

    print("-"*50)
    # 全模式（返回所有可能的组合，速度快但结果可能不那么准确）
    result = jieba.lcut(text, cut_all=True)
    print("全模式：", result)

    print("-"*50)
    # 搜索引擎模式（在精确模式基础上，对长词进行再切分，更符合搜索引擎需求）
    result = jieba.lcut_for_search(text)
    print("搜索引擎模式：", result)


def test_tfidf():
    """
    测试TF-IDF，（特征提取）
    """
    print("-"*50)
    # 1. 中文分词预处理：Jieba分词后用空格拼接（适配TfidfVectorizer的空格分词规则）
    def chinese_cut(text):
        # jieba.lcut 分词返回列表，join 用空格拼接为字符串
        return " ".join(jieba.lcut(text))

    # 对整个语料库做分词预处理
    corpus_cut = [chinese_cut(text) for text in corpus]
    print("分词后语料：", corpus_cut)

    # 2. 初始化TfidfVectorizer并拟合转换（一步完成词汇表构建+TF-IDF计算）
    tfidf_vec = TfidfVectorizer()
    # fit_transform：拟合语料（构建词汇表）+ 转换为TF-IDF特征矩阵
    tfidf_matrix = tfidf_vec.fit_transform(corpus_cut)

    # 3. 查看核心结果
    print("\n词汇表（所有分词后的不重复词汇）：", tfidf_vec.get_feature_names_out())
    print("TF-IDF特征矩阵形状：", tfidf_matrix.shape)  # 形状：(文档数, 词汇表大小)
    print("TF-IDF特征矩阵（稀疏矩阵转密集矩阵）：\n", tfidf_matrix.toarray()) # 小语料可直接查看，大语料不建议转换（占用内存）


def chinese_tokenize(text):
    """
    中文分词函数：将单篇文本分词为词汇列表（过滤空字符串，提升效果）
    """
    return [word for word in jieba.lcut(text) if word.strip()]


def test_bm25():
    """
    测试BM25，（文本检索 / 相似度匹配）
    """
    print("-"*50)
    # ---------------------- 步骤1：准备语料库并做中文分词处理 ----------------------
    # 语料库分词：转为【词汇列表的列表】（BM25Okapi要求的输入格式）
    corpus_tokenized = [chinese_tokenize(doc) for doc in corpus]

    # ---------------------- 步骤2：初始化BM25模型并拟合语料库 ----------------------
    bm25 = BM25Okapi(corpus_tokenized)  # 传入分词后的语料库，完成模型初始化
    # k1：取值范围一般为 [1.2, 2.0]，值越大，词频对得分的影响越显著；若语料中核心词出现次数少，可适当调大 k1（如 2.0），突出词频的作用；若语料中词汇重复度高（如广告文案），可适当调小 k1（如 1.2），避免词频过高占优。
    # b：取值范围一般为 [0.6, 0.8]，值越大，文档长度对得分的影响越显著；若文档长度差异大（如长文章 vs 短文章），可适当调大 b（如 0.8），突出文档长度的作用。
    #bm25 = BM25Okapi(corpus_tokenized, k1=1.8, b=0.6)

    # ---------------------- 步骤3：处理查询词，计算相关性得分并排序 ----------------------
    # 待查询的关键词/短句（可替换为任意用户查询）
    query = "BM25中文检索的用法"
    # 查询词分词（与语料库分词规则一致，关键！）
    query_tokenized = chinese_tokenize(query)

    # 计算查询词与语料库中所有文档的相关性得分
    # scores 是列表，长度=语料库文档数，元素为对应文档的BM25得分，得分越高相关性越强
    scores = bm25.get_scores(query_tokenized)

    # 直接获取前2个最相关的原始文档
    #top_n_docs = bm25.get_top_n(query_tokenized, corpus, n=2)

    # 按相关性得分【降序】排序，获取文档的索引
    # argsort()返回升序索引，[::-1]转为降序
    sorted_doc_indices = scores.argsort()[::-1]

    # ---------------------- 步骤4：输出匹配结果 ----------------------
    print(f"查询词：{query}\n")
    print("匹配结果（按相关性得分降序）：")
    for idx in sorted_doc_indices:
        print(f"得分：{scores[idx]:.4f} | 文档：{corpus[idx]}")

def generate_ngram(text, n=2):
    """
    生成文本的字级N-gram集合（去重）
    :param text: 输入文本（关键词/语句）
    :param n: N-gram的N值，推荐2/3
    :return: 去重后的N-gram集合
    """
    # 去除文本中的空格、标点（可选，根据业务需求调整）
    text = text.replace(" ", "").replace("，", "").replace("。", "").replace("、", "").replace("：", "")
    # 生成连续N字片段
    ngrams = [text[i:i+n] for i in range(len(text) - n + 1)]
    # 转集合去重，返回集合（方便后续计算交集/并集）
    return set(ngrams)

def jaccard_similarity(set_a, set_b):
    """
    计算两个集合的Jaccard相似度。集合不重叠时，相似度为0，完全重叠时，相似度为1。
    :param set_a: 关键词N-gram集合
    :param set_b: 语句N-gram集合
    :return: Jaccard系数（0~1）
    """
    # 计算交集和并集
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    # 避免除零错误（当两个集合都为空时，相似度为0）
    return intersection / union if union > 0 else 0.0


def find_best_match_keyword(sentence, keywords, n=2):
    """
    从一批关键词中找出与语句N-gram相似度最高的关键词
    :param sentence: 目标语句
    :param keywords: 待匹配的关键词列表
    :param n: N-gram的N值
    :return: 排序后的关键词-相似度列表、最匹配的关键词
    """
    # 生成目标语句的N-gram集合（仅需计算1次，提升效率）
    sentence_ngram = generate_ngram(sentence, n=n)
    # 遍历所有关键词，计算相似度
    keyword_similarity = []
    for kw in keywords:
        kw_ngram = generate_ngram(kw, n=n)
        sim = jaccard_similarity(kw_ngram, sentence_ngram)
        keyword_similarity.append((kw, sim))
    # 按相似度降序排序
    keyword_similarity_sorted = sorted(keyword_similarity, key=lambda x: x[1], reverse=True)
    # 最匹配的关键词（处理全0相似度情况）
    best_kw = keyword_similarity_sorted[0][0] if keyword_similarity_sorted else None
    return keyword_similarity_sorted, best_kw

def test_ngram():
    """
    测试n-gram匹配。按照n-gram的长度，将文本转换为n-gram向量。
    """
    print("-"*50)
    texts = [
      "女欧冠",
      "女足欧冠",
      "欧洲女子冠军联赛"
    ]

    vectorizer = CountVectorizer(
        analyzer="char",   # char n-gram
        ngram_range=(2,3) # 2-gram 到 3-gram
    )

    x = vectorizer.fit_transform(texts)
    print(vectorizer.get_feature_names_out())
    print(x.toarray())

    print("-"*50)
    # 高频但没区分度的 n-gram 权重会变小。更适合 相似度 / 匹配
    tfidf = TfidfVectorizer(
        analyzer="char",
        ngram_range=(2, 3),
        min_df=1
    )
    x = tfidf.fit_transform(texts)
    print(tfidf.get_feature_names_out())
    print(x.toarray())

def test_similarity1(question, keywords):
    sorted, best_kw = find_best_match_keyword(question, keywords)
    print(sorted)
    print(best_kw)


def test_similarity2(question, keywords):
    """
    测试n-gram相似度匹配。
    :param question: 待匹配的问题/语句
    :param keywords: 待匹配的关键词列表
    :return: 关键词-相似度字典
    """
    print("-"*50)

    vectorizer = TfidfVectorizer(
        analyzer="char",
        ngram_range=(2, 3),  # 中文推荐
        min_df=1
    )

    keyword_vecs = vectorizer.fit_transform(keywords)
    question_vec = vectorizer.transform([question])
    # 计算余弦相似度
    sims = cosine_similarity(question_vec, keyword_vecs)[0]
    for idx, score in enumerate(sims):
        print(f"关键词: {keywords[idx]}, 相似度: {score:.4f}")


#test_jieba()
# test_bm25()
#test_ngram()

test_similarity1("24/25赛季，女子英超第1轮：阿森纳VS伦敦城雌狮，最终比分是多少？", ["英超", "英格兰超级联赛", "女英超", "英格兰女子超级联赛", "女欧冠", "欧洲女子冠军联赛"])

#test_similarity2("24/25赛季，女子英超第1轮：阿森纳VS伦敦城雌狮，最终比分是多少？", ["英超", "英格兰超级联赛", "女英超", "英格兰女子超级联赛", "女欧冠", "欧洲女子冠军联赛"])
