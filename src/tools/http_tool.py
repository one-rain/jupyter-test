import requests


def query_match_info(query: str) -> list:
    """查询赛事信息"""
    api_url = "http://127.0.0.1:8000/api/chat/simple"
    try:
        response = requests.get(f"{api_url}?query={query}", timeout=30)
        response.raise_for_status()
        result = response.json()
        if result.get("code") != 200:
            print(f"访问数据服务API时发生异常。: {result}")
            #raise ValueError(f"访问数据服务API时发生异常。: {result}")
            return []
        return result.get("content", [])
    except requests.RequestException as e:
        print(f"数据服务API无法访问。: {e}")
        #raise ValueError(f"数据服务API无法访问。: {e}")
        return []
