import sys
import json
from majorlogin import execute_major_login
from majorlogin_pd2 import execute_pd2_login

def main():
    print("=== Garena & PolarBear Server Debugger (Region: PK) ===")
    
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
        print(f"[+] Loaded Config for UID: {config.get('target_uid')} | Region: {config.get('region')}")
    except FileNotFoundError:
        print("[-] Error: config.json missing.")
        sys.exit(1)

    print("\n[1] Run Connect Garena Login Request")
    print("[2] Run PolarBear Game Server Request")
    choice = input("Select an option (1 or 2): ")

    if choice == "1":
        status, response_text = execute_major_login()
        print(f"\n[Result] Status: {status}\n[Body]: {response_text}")
    elif choice == "2":
        status, response_text = execute_pd2_login()
        print(f"\n[Result] Status: {status}\n[Body]: {response_text}")
    else:
        print("[-] Invalid Selection.")

if __name__ == "__main__":
    main()
