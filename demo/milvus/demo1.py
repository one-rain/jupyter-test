from pymilvus import MilvusClient

client = MilvusClient(
    uri="http://localhost:19530",
    token="root:Milvus"
)

def create_database():
    client.create_database(
        db_name="test_sport",
        properties={
            "database.replica.number": 1
        }
    )

def describe_database():
    databases = client.list_databases()
    print(databases)
    
    db = client.describe_database(
        db_name="test_sport"
    )
    print(db)
    
describe_database()