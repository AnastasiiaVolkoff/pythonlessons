import os
from dotenv import load_dotenv
import requests

load_dotenv()
TOKEN = os.getenv("YOUGILE_TOKEN")
BASE_URL = "https://yougile.com/api-v2"

if not TOKEN:
    print("❌ Токен не найден в .env")
    exit()

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

print(f"Отправка запроса GET {BASE_URL}/projects")
resp = requests.get(f"{BASE_URL}/projects", headers=headers)
print(f"Статус: {resp.status_code}")
print(f"Ответ: {resp.text}")
