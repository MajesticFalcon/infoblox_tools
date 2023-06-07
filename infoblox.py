import requests
from urllib3.exceptions import InsecureRequestWarning

class Infoblox:
    def __init__(self, url, username, password):
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

        self.url = url
        self.username = username
        self.password = password
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        self.session = requests.Session()
        self.session.auth = (username, password)

    def get_dhcp_scopes(self):
        page_id = None
        while True:
            params = {
                "_max_results": 1000,
                "_page_id": page_id
            }
            response = self.session.get(self.url + "network", headers=self.headers, params=params, verify=False)
            response.raise_for_status()  # Raise an exception in case of error

            data = response.json()

            for item in data:
                yield item

            if response.headers.get("X-Page-Id"):
                page_id = response.headers["X-Page-Id"]
            else:
                break

    def get_dhcp_pools(self, scope):
        response = self.session.get(self.url + f"range?network={scope}", headers=self.headers, verify=False)
        response.raise_for_status()
        return response.json()

    def get_pool_usage(self, pool):
        response = self.session.get(self.url + f"{pool}?_return_fields=name,dhcp_utilization,network", headers=self.headers, verify=False)
        response.raise_for_status()
        return response.json()

    def print_high_usage_pools(self):
        for scope in self.get_dhcp_scopes():
            pools = self.get_dhcp_pools(scope['network'])
            for pool in pools:
                usage = self.get_pool_usage(pool['_ref'])
                if int(usage['dhcp_utilization']) > 900:
                    if 'name' in usage.keys():
                        print(f"Name: {usage['name']} Network: {usage['network']} Usage: {round(usage['dhcp_utilization']*0.1)}%")
                    else:
                        print(f"Network: {usage['network']} Usage: {usage['dhcp_utilization']}")
