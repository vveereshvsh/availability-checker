import requests
import time

def check_endpoint(endpoint):
    url = endpoint["url"]
    method = endpoint.get("method", "GET")
    headers = {k.title(): v for k, v in endpoint.get("headers", {}).items()}
    body = endpoint.get("body", None)

    try:
        start = time.time()
        response = requests.request(method, url, headers=headers, data=body, timeout=5)
        latency = (time.time() - start) * 1000  # ms

        is_available = 200 <= response.status_code <= 299 and latency <= 500
        return {
            "available": is_available,
            "status": response.status_code,
            "latency": int(latency)
        }

    except requests.RequestException as e:
        return {
            "available": False,
            "status": "error",
            "latency": -1
        }
