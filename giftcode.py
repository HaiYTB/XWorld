from _requests import build_headers, post_json


def redeem(user_id: str, user_secret_key: str, code: str):
    """Nhập mã nhận thưởng"""
    url = "https://web3task.3games.io/v1/task/redcode/exchange"
    headers = build_headers(user_id, user_secret_key)
    data = {"code": code, "os_ver": "android", "platform": "h5"}
    result = post_json(url, headers, data)
    return result["data"]
