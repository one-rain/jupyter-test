

def preprocess_text(text):
    """轻量预处理：仅去标点/空格，保留所有核心汉字（关键！）"""
    text = text.strip()
    # 仅去除无意义符号，保留中文、数字、字母
    punc = "，。、：；？！“”‘’（）[]{}《》@#￥%&*·~ "
    for p in punc:
        text = text.replace(p, "")
    return text
