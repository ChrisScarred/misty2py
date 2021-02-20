import requests

MISTY_IP = "192.168.0.103"

def get_request(endpoint: str) -> dict:
    r = requests.get('http://%s/%s' % (MISTY_IP, endpoint))
    return r.json()

def post_request(endpoint: str, data: dict) -> dict:
    r = requests.post('http://%s/%s' % (MISTY_IP, endpoint), data = data)
    return r.json()

cols = {
    "red": "255",
    "green": "0",
    "blue": "0"
}
r = post_request('api/led', cols)
print(r)

r = get_request('api/blink/settings')
print(r)