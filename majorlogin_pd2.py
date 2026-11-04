import requests
import json

def execute_pd2_login():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
            
        # نئے پولر بیئر لاگ ان یو آر ایل کا استعمال
        url = f"{config['login_url']}api/v1/login"
        
        headers = {
            "Content-Type": "application/json",
            "X-Region": config["region"]  # PK ریجن
        }
        
        payload = {
            "uid": config["target_uid"],
            "client_id": config["client_id"],
            "server_endpoint": config["server_url"], # https://clientbp.ggpolarbear.com
            "region": config["region"]
        }
        
        print(f"[*] [majorlogin_pd2] Testing PolarBear Login Endpoint: {url}")
        response = requests.post(url, headers=headers, json=payload)
        return response.status_code, response.text
    except Exception as e:
        return 500, str(e)
