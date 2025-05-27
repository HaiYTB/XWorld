from _requests import build_headers, post_json


def user_info(user_id: str, user_secret_key: str):
    """Lấy thông tin tài khoản"""
    url = "https://nft.3games.io/api/sbt_nft/info"
    headers = build_headers(user_id, user_secret_key)
    data = {"user_id": user_id}
    result = post_json(url, headers, data)
    return result.get("sbt", {})


def wallet(user_id: str, user_secret_key: str):
    """Lấy thông tin ví"""
    url = "https://wallet.3games.io/api/wallet/user_asset"
    headers = build_headers(user_id, user_secret_key)
    data = {"source": "home", "user_id": user_id}
    result = post_json(url, headers, data)
    return result.get("user_asset", {})
