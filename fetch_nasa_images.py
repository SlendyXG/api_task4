import argparse
import os

import requests
from urllib.parse import urlparse
from dotenv import load_dotenv

from download_image import download_image


def get_extension(url):
    parsed_url = urlparse(url)
    extension = os.path.splitext(parsed_url.path)[1]
    return extension or '.jpg'


def fetch_nasa_day_photos(nasa_api_key, count=30):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': nasa_api_key,
        'count': count
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    images_data = response.json()

    os.makedirs('images', exist_ok=True)

    for image_number, image_info in enumerate(images_data, start=1):
        image_url = image_info['url']
        extension = get_extension(image_url)
        filename = f'nasa_apod_{image_number}{extension}'
        download_image(image_url, filename)


def main():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    fetch_nasa_day_photos(nasa_api_key)


if __name__ == "__main__":
    main()