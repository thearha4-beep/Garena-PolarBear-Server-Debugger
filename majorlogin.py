import requests
import json

def execute_major_login():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
            
        # گیسٹ ٹوکن گرانٹ اینڈ پوائنٹ
        url = f"https://{config['host_url']}/oauth/guest/token/grant"
        
        headers = {
            "Host": config['host_url'],
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Garena Free Fire/Android"
        }
        
        payload = {
            "uid": config["target_uid"],
            "password": config["target_password"],
            "response_type": "token",
            "client_type": "2",
            "client_secret": config["client_secret"],
            "client_id": config["client_id"]
        }
        
        print(f"[*] [majorlogin] Testing token grant at: {url}")
        response = requests.post(url, headers=headers, data=payload)
        return response.status_code, response.text
    except Exception as e:
        return 500, str(e)
