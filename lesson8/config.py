import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://yougile.com/api-v2"
TOKEN = os.getenv("YOUGILE_TOKEN")

if not TOKEN:
    raise ValueError(
        "YOUGILE_TOKEN не задан. Убедитесь, что файл .env находится в корне проекта."
    )
