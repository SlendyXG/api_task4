import os

from dotenv import load_dotenv
from urllib.parse import urlparse
import requests


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    response.raise_for_status()
    image_links = response.json()['links']['flickr']['original']

    for image_number, url in enumerate(image_links, start=1):
        image_response = requests.get(url)
        image_response.raise_for_status()
        filename = 'spacex' + str(image_number) + '.png'
        file_path = os.path.join('images', filename)
        with open(file_path, 'wb') as file:
            file.write(image_response.content)


def fetch_nasa_day_photos(nasa_api_key):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': nasa_api_key,
        'count': 30
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    image_links = response.json()

    for image_number, url in enumerate(image_links):
        image_url = image_links[image_number]['url']
        image_response = requests.get(image_url, headers=headers)
        extension = get_extension(image_url)
        filename = 'nasa_apod_' + str(image_number + 1) + extension
        file_path = os.path.join('images', filename)
        with open(file_path, 'wb') as file:
            file.write(image_response.content)


def get_extension(url):
    parsed_url = urlparse(url)
    extension = os.path.splitext(parsed_url.path)[1]
    return extension


def get_epic_images():
    url = "https://epic.gsfc.nasa.gov/api/natural"
    params = {
        'api_key': 'DEMO_KEY',
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = response.json()

    for image_number, image in enumerate(images[:5], start=1):
        image_name = image['image']
        date_parts = image['date'].split()[0].replace('-', '/')
        image_url = (f"https://epic.gsfc.nasa.gov/archive/natural/{date_parts}/png/{image_name}.png")
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        filename = 'epic' + str(image_number) + '.png'
        file_path = os.path.join('images', filename)
        with open(file_path, 'wb') as file:
            file.write(image_response.content)


def main():
    if not os.path.exists('images'):
        os.mkdir('images')
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    fetch_spacex_last_launch()
    fetch_nasa_day_photos(nasa_api_key)
    get_epic_images()


if __name__ == '__main__':
    main()