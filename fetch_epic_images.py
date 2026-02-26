import os
from datetime import datetime

import requests

from download_image import download_image


def fetch_epic_photos():
    url = "https://epic.gsfc.nasa.gov/api/natural"
    params = {
        'api_key': 'DEMO_KEY',
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = response.json()

    os.makedirs('images', exist_ok=True)

    for image_number, image in enumerate(images[:5], start=1):
        image_name = image['image']
        date = datetime.fromisoformat(image['date'].replace('Z', '+00:00'))
        image_url = (f"https://epic.gsfc.nasa.gov/archive/natural/{date:%Y/%m/%d}/png/{image_name}.png")
        filename = f"epic{image_number}.png"
        download_image(image_url, filename)


def main():
    fetch_epic_photos()


if __name__ == '__main__':
    main()