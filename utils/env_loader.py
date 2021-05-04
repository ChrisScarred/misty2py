from dotenv import load_dotenv
import os

load_dotenv()
MISTY_IP = os.environ.get("MISTY_IP_ADDRESS")
if not MISTY_IP:
    raise TypeError("Missing the environmental value MISTY_IP_ADDRESS")
