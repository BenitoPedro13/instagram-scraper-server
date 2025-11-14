import json
import httpx
import jmespath
from src.utils.parser import parse_user

client = httpx.Client(
    headers={
        # this is internal ID of an instegram backend app. It doesn't change often.
        "x-ig-app-id": "936619743392459",
        # use browser-like features
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
    }
)

def scrape_user(username: str):
    """Scrape Instagram user's data"""
    url = "https://i.instagram.com/api/v1/users/web_profile_info/"
    try:
        result = client.get(url, params={"username": username}, timeout=20.0)
    except httpx.RequestError as exc:
        raise RuntimeError(f"Erro de rede ao consultar Instagram: {exc}") from exc

    # Verifica status HTTP primeiro
    if result.status_code != 200:
        try:
            payload = result.json()
        except Exception:
            payload = {"body": result.text[:300]}
        message = payload.get("message") if isinstance(payload, dict) else None
        raise RuntimeError(f"Instagram retornou HTTP {result.status_code}{': ' + message if message else ''}")

    # Tenta decodificar JSON com segurança
    try:
        data = result.json()
    except json.JSONDecodeError:
        raise RuntimeError("Resposta do Instagram não é JSON válido.")

    # Tenta extrair usuário dos formatos mais comuns
    user = None
    if isinstance(data, dict):
        if isinstance(data.get("data"), dict) and isinstance(data["data"].get("user"), dict):
            user = data["data"]["user"]
        elif isinstance(data.get("user"), dict):
            user = data["user"]

    if not user:
        keys = list(data.keys()) if isinstance(data, dict) else type(data).__name__
        raise RuntimeError(f"Formato inesperado da resposta do Instagram. Chaves: {keys}")

    return user
