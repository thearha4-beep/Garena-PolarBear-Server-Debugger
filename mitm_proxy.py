from mitmproxy import http
import json

def response(flow: http.HTTPFlow) -> None:
    # 1. تمام ٹارگٹ ہوسٹس کو فلٹر کریں
    target_hosts = ["connect.garena.com", "loginbp.ggpolarbear.com", "clientbp.ggpolarbear.com"]
    
    if any(host in flow.request.pretty_host for host in target_hosts):
        print(f"[*] Proxy Intercepted Traffic: {flow.request.pretty_host}{flow.request.path}")
        
        # 400, 401, 405 ایررز کو کیپچر کریں
        error_statuses = [400, 401, 405]
        if flow.response and flow.response.status_code in error_statuses:
            print(f"[!] Server Error {flow.response.status_code} detected. Overriding to 200 OK...")
            
            try:
                with open("config.json", "r") as f:
                    config = json.load(f)
                uid = config.get("target_uid", "11959685790")
            except:
                uid = "11959685790"

            # لوکل رسپانس مینیپولیشن
            flow.response.status_code = 200
            flow.response.reason = "OK"
            
            mock_data = {
                "access_token": "MOCK_POLARBEAR_SESSION_TOKEN_PK_778899",
                "token_type": "Bearer",
                "expires_in": 7200,
                "uid": uid,
                "region": "PK",
                "status": "success_via_mock"
            }
            
            flow.response.text = json.dumps(mock_data)
            flow.response.headers["Content-Type"] = "application/json"
