import aiohttp
import requests
from bs4 import BeautifulSoup

base_url = "https://animepahe.pw"

def search_anime(query):
    url = f"{base_url}/api?m=search&q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("data", [])
    return []

def get_episodes(anime_session):
    url = f"{base_url}/api?m=release&id={anime_session}&sort=episode_asc&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("data", [])
    return []

