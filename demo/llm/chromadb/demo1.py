import chromadb

# 内存模式
chroma_client = chromadb.Client() 

# 数据保存在磁盘
# chroma_client = chromadb.PersistentClient(path="./chromac")

# 服务等docker客户端模式
# chroma_client = chromadb.HttpClient(host="localhost", port=8000) 

# 创建或获取集合
collection = chroma_client.get_or_create_collection(name="test")

# 添加或修改数据
collection.add(
    documents=["2022年2月2号，美国国防部宣布：将向欧洲增派部队，应对俄乌边境地区的紧张局势.", 
               "2月17号，乌克兰军方称：东部民间武装向政府军控制区发动炮击，而东部民间武装则指责乌政府军先动用了重型武器发动袭击，乌东地区紧张局势持续升级"
               ],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2"]
)

# 查询数据
results = collection.query(
    query_texts=["This is a query document about florida"], # Chroma will embed this for you
    n_results=2 # how many results to return
)

print(results)


# https://medium.com/@lemooljiang/chroma%E5%90%91%E9%87%8F%E6%95%B0%E6%8D%AE%E5%BA%93%E5%AE%8C%E5%85%A8%E6%89%8B%E5%86%8C-4248b15679ea

