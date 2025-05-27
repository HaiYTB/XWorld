import requests


def build_headers(user_id: str, user_secret_key: str) -> dict:
    return {  
        "Accept": "*/*",  
        "Accept-Encoding": "gzip, deflate, br",  
        "Accept-Language": "vi-VN,vi;q=0.9,en-VN;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5,en-US;q=0.4",  
        "Content-Type": "application/json",  
        "Country-Code": "vn",  
        "Origin": "https://xworld.info",  
        "Referer": "https://xworld.info/",  
        "Sec-Ch-Ua": '"Chromium";v="137", "Not/A)Brand";v="24"',  
        "Sec-Ch-Ua-Mobile": "?1",  
        "Sec-Ch-Ua-Platform": '"Android"',  
        "Sec-Fetch-Dest": "empty",  
        "Sec-Fetch-Mode": "cors",  
        "Sec-Fetch-Site": "cross-site",  
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",  
        "User-Id": user_id,  
        "User-Secret-Key": user_secret_key,  
        "Xb-Language": "vi-VN",  
    }


def post_json(url: str, headers: dict, data: dict) -> dict:
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        res_json = response.json()
    except Exception as e:
        raise RuntimeError(f"Lỗi khi gọi API: {e}")

    if res_json.get("code") != 0:
        message = res_json.get("message") or res_json.get("msg") or "Không rõ"
        raise ConnectionError(f"Lỗi từ máy chủ: {message}")

    return res_json
