import requests
from configs import CONFIG_DICT
from route_config_sample import ROUTE_CONFIGS

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
BLUE = '\033[34m'


def register_routes_to_apisix():

    print("Starting to post route configurations...")
    print(f"{BLUE} Starting to post route configurations... {RESET}")


    for i, route_config in enumerate(ROUTE_CONFIGS, start=1):

        print(f"=======Starting to post for {i}\n=======")
        headers = {
            "X-API-KEY": CONFIG_DICT["X_API_KEY"],
            "Content-Type": "application/json"
        }
        url = f"{CONFIG_DICT['API_SIX_BASE_URL']}/apisix/admin/routes/{i}"
        
        dict_data = route_config
        try:
            response = requests.put(url, headers=headers, json=dict_data)
            
            if response.status_code in (200, 201):
                print(f"{GREEN}✅ Successfully posted configuration {i} to {url}{RESET}")

            else:
                print(f"{RED}❌ Failed to post configuration {i}. Status: {response.status_code}{RESET}")
                print(f"{RED}Response: {response.text}{RESET}")
                
        except requests.RequestException as e:
            print(f"{RED}⚠️ Error posting configuration {i}: {str(e)}{RESET}")

        print("=======End=======")

register_routes_to_apisix()

